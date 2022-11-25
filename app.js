var createError = require('http-errors');
var express = require('express');
var path = require('path');
var logger = require('morgan');
const { Client } = require('pg')
const bodyParser = require("body-parser");
const cookieParser = require("cookie-parser");
const { spawn } = require('child_process');
var socket = require('socket.io');

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
    res.render('login', { title: 'Login' });
});

app.get('/browse', async function(req, res, next) {
    await queryDrinks()
    res.render('browse', { drinks: drinkList, userObj: user});
});

app.get('/favorite', function(req, res, next) {
    res.render('favorite');
});

app.get('/home', function(req, res, next) {
    res.render('index');
});

app.get('/register', function(req, res, next) {
    res.render('register');
});

app.get('/complete', function(req, res, next) {
    res.render('complete');
});

// Call Python functions
function callDrinkPython(data) {
    console.log(data['drinkID'])
    var path = require('path');
    var pythonPath = path.join('src', 'PythonTkinter', 'dispense_drink.py');
    // spawn new child process to call the python script

    python = spawn('python', [pythonPath, data['drinkID'], data['userID']]);

    for (let i = 0; i < userList.lgenth; i++) {
        if (userList[i].userID == data['userID']) {
            user = userList[i]
        }
    }
    // res.redirect('/')

}

// Database functions
client.connect()
async function queryDrinks() {
    try {
        const res = await client.query(`Select * from drink_tables`);
        drinkList = res.rows
        console.log("Successfully retrive data from DB")
    } catch {
        console.log("Error on getting drinks from DB")
    }
}

async function queryUsers() {
    try {
        const res = await client.query(`Select * from users`);
        userList = res.rows
        console.log("Successfully retrive users from DB")
    } catch {
        console.log("Error on getting users from DB")
    }
}

const insertUser = async(userName, userPass) => {
    try { // gets connection
        await client.query(
            `INSERT INTO "users" ("username", "userpass","usercoins")  
             VALUES ($1, $2, $3)`, [userName, userPass, 0]); // sends queries
        return true;
    } catch (error) {
        console.error(error.stack);
        return false;
    } finally {
        await client.end(); // closes connection
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
        // console.log(data);
        callDrinkPython(data);
    });
  });

module.exports = app;