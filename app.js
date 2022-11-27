var createError = require('http-errors');
var express = require('express');
var path = require('path');
const { Client } = require('pg')
const bodyParser = require("body-parser");
const cookieParser = require("cookie-parser");
const { spawn } = require('child_process');
var socket = require('socket.io');
const fs = require('fs');
var path = require('path');
var pythonPath = path.join('src', 'PythonTkinter', 'dispense_drink.py');

const client = new Client({
    host: "localhost",
    user: "admin",
    port: 5432,
    password: "uwure",
    database: "uwure"
})

let drinkList;
let userList;
let users = [];
const apiRoute = express.Router();
var app = express();
var user;

var server = app.listen(4000, function() {
    console.log('listening for requests on port 4000,');
});

queryDrinks()
queryUsers()


// API
app.use(cookieParser());
app.use(bodyParser.urlencoded({ extended: true }));
app.use("/api", apiRoute);

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');

app.get('/', async function(req, res, next) {
    await queryDrinks()
    await queryUsers()
    res.render('login');
});

app.get('/browse', async function(req, res, next) {
    await queryDrinks()
    fs.readFile('user.json', (err, data) => {
        if (err) throw err;
        let user = JSON.parse(data);
        res.render('browse', { drinks: drinkList, userObj: user });
    });
});

app.get('/favorite', async function(req, res, next) {
    let user;
    let favdrinks;
    getFavDrinks()
    fs.readFile('fav.json', (err, data) => {
        if (err) throw err;
        data = JSON.parse(data);
        res.render('favorite', { drinks: data['drinks'], userObj: data['user'] }), 2000;
    });
});

app.get('/home', function(req, res, next) {
    res.render('index');
});

app.get('/register', function(req, res, next) {
    res.render('register');
});

app.get('/create', function(req, res, next) {
    fs.readFile('user.json', (err, data) => {
        if (err) throw err;
        let user = JSON.parse(data);
        res.render('create', { userObj: user });
    });
});

app.get('/recipe', function(req, res, next) {
    fs.readFile('DRINK.json', (err, data) => {
        if (err) throw err;
        let drink = JSON.parse(data);
        res.render('randomRecipe', { drink: drink['drink'][0] });
    });
});

app.get('/custom', function(req, res, next) {
    fs.readFile('DRINK.json', (err, data) => {
        if (err) throw err;
        let drink = JSON.parse(data);
        console.log(drink['drink'][1])
        res.render('randomDrink', { drink: drink['drink'] });
    });
});

app.get('/complete', function(req, res, next) {
    fs.readFile('DRINK.json', (err, data) => {
        if (err) throw err;
        let drink = JSON.parse(data);
        console.log(drink['drink'][0])
        res.render('display', { drink: drink['drink'][0] });
    });
});

// Call Python functions
// function callDrinkPython(data) {
//     // spawn new child process to call the python script
//     python = spawn('python', [pythonPath, 0, data['drinkID'], data['userID']]);

//     for (let i = 0; i < userList.length; i++) {
//         if (userList[i].userID == data['userID']) {
//             user = userList[i]
//         }
//     }
// }


// Database functions
client.connect()
async function getFavDrinks() {
    let tempArr = []
    fs.readFile('user.json', (err, data) => {
        if (err) throw err;
        let user = JSON.parse(data);
    });
    try {
        for (let i = 0; i < user.favdrinkid.length; i++) {
            sql = `select * from drink_tables where drinkid = ${user.favdrinkid[i]};`
            const res = await client.query(sql);
            tempArr.push(res.rows[0])
        }
        var combinedData = {
            'user': user,
            'drinks': tempArr
        }
        console.log(combinedData)
        const data = JSON.stringify(combinedData, null, 4);
        fs.writeFileSync('fav.json', data);
    } catch {
        console.log("Error on getting favorite drinks from DB")
    }
}

async function queryDrinks() {
    try {
        const res = await client.query(`Select * from drink_tables`);
        drinkList = res.rows
        console.log("Successfully retrieve data from DB")
    } catch {
        console.log("Error on getting drinks from DB")
    }
}

async function queryUsers() {
    try {
        const res = await client.query(`Select * from users`);
        userList = res.rows
        console.log("Successfully retrieve users from DB")
    } catch {
        console.log("Error on getting users from DB")
    }
}

const insertFavDrink = async(userID, drinkID) => {
    let sql = `UPDATE users SET favdrinkid = array_append(favdrinkid,${drinkID}) where userid = ${userID}`
        // console.log(sql)
    try { // gets connection
        await client.query(sql); // sends queries
        getFavDrinks()
        return true;
    } catch (error) {
        console.error(error.stack);
        return false;
    }
};

const insertUser = async(userName, userPass) => {
    try { // gets connection
        await client.query(
            `INSERT INTO "users" ("username", "userpass","usercoins")  
             VALUES ($1, $2, $3)`, [userName, userPass, 0]); // sends queries
        return true;
    } catch (error) {
        console.error(error.stack);
        return false;
    }
};


// API Functions
apiRoute.post("/register", (req, res) => {
    const { username, userpass } = req.body;
    console.log("Registering with with this data")
    if (!username || !userpass)
        return res.redirect("/?error=missing credentials");
    if (users.some((user) => username === user.username))
        return res.redirect("/?error=username already exists");
    insertUser(username, userpass).then(result => {
        if (result) {
            console.log('User inserted');
            userList.push(req.body)
        }
    });
    res.redirect("/");
});

apiRoute.post("/login", (req, res) => {
    const { username, userpass } = req.body;
    console.log("Loggin in with this data")
    queryUsers()
    if (!username || !userpass)
        return res.redirect("/?error=missing credentials");

    for (let i = 0; i < userList.length; i++) {
        if (username == userList[i].username && userpass == userList[i].userpass) {
            user = userList[i]
        }
    }
    if (!user) return res.redirect("/?error=invalid credentials");

    const data = JSON.stringify(user, null, 4);
    fs.writeFileSync('user.json', data);
    getFavDrinks()
    res.redirect("/home");
});

apiRoute.get("/logout", (req, res) => {
    res.redirect("/");
});


// Socket setup
var io = socket(server);
io.on('connection', (socket) => {
    console.log('a user connected');
    socket.on('disconnect', () => {
        console.log('user disconnected');
    });

    socket.on('order', function(data) {
        python = spawn('python', [pythonPath, 0, data['drinkID'], data['userID']]);
        python.on('exit', function() {
            process.exit()
        })
    });

    socket.on('fav', function(data) {
        insertFavDrink(data['userID'], data['drinkID'])
    });

    socket.on('randomRecipe', function(data) {
        console.log("User chose Random Recipe");
        python = spawn('python', [pythonPath, 2, data['drinkID'], data['userID']]);
        console.log("Completed")
    });

    socket.on('randomDrink', function(data) {
        console.log("User chose Random Drink");
        python = spawn('python', [pythonPath, 3, data['drinkID'], data['userID']]);
        console.log("Completed")
    });

    socket.on('uwuTime', function(data) {
        console.log("UwU");
        python = spawn('python', [pythonPath, 1, data['drinkID'], data['userID']]);
        console.log("Completed")
    });
});

module.exports = app;