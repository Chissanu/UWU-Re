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

app.get('/', function(req, res, next) {
    res.render('login', { title: 'Login' });
});

app.get('/browse', function(req, res, next) {
    res.render('browse', { drinks: drinkList, userObj: user});
});

app.get('/favorite', function(req, res, next) {
    res.render('favorite');
});

app.get('/home', function(req, res, next) {
    res.render('index', { drinksName: drinkList.drinkname });
});

app.get('/register', function(req, res, next) {
    res.render('register');
});

app.get('/complete', function(req, res, next) {
    res.render('complete');
});

app.get('/test', function(req, res) {
    var dataToSend;
    var path = require('path');
    var x = path.join('src', 'PythonTkinter', 'dispense_drink.py');
    // spawn new child process to call the python script

    const python = spawn('python', [x, 14, "hello"]);
    // collect data from script
    python.stdout.on('data', function (data) {
     console.log('Pipe data from python script ...');
     dataToSend = data.toString();
    });
    // in close event we are sure that stream from child process is closed
    python.on('close', (code) => {
    console.log(`child process close all stdio with code ${code}`);
    // send data to browser
    res.send(dataToSend)
    });
 
});

apiRoute.post("/test2", (req, res) => {
    var dataToSend;
    var path = require('path');
    var x = path.join('src', 'PythonTkinter', 'dispense_drink.py');
    // spawn new child process to call the python script

    const python = spawn('python', [x, 14, "hello"]);
    // collect data from script
    python.stdout.on('data', function (data) {
     console.log('Pipe data from python script ...');
     dataToSend = data.toString();
    });
    // in close event we are sure that stream from child process is closed
    python.on('close', (code) => {
    console.log(`child process close all stdio with code ${code}`);
    // send data to browser
    console.log(res)
    res.send(dataToSend)
    });
});

const setDrinkList = (rows) => {
    drinkList = rows;
}

const setUserList = (rows) => {
    userList = rows;
}

client.connect()
client.query(`Select * from drink_tables`, (err, res) => {
    if (!err) {
        setDrinkList(res.rows);
    } else {
        console.log(err.message);
    }
    client.end;
});

client.query(`Select * from users`, (err, res) => {
    if (!err) {
        setUserList(res.rows);
    } else {
        console.log(err.message);
    }
    client.end;
});

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
        //console.log(userList.find)
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

var io = socket(server);
io.on('connection', (socket) => {
    console.log('a user connected');
    socket.on('disconnect', () => {
      console.log('user disconnected');
    });

    socket.on('order', function(data) {
        console.log(data);
    });
  });

module.exports = app;