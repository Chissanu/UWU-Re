var createError = require('http-errors');
var express = require('express');
var path = require('path');
var logger = require('morgan');
const { Client } = require('pg')
const bodyParser = require("body-parser");
const cookieParser = require("cookie-parser");
const jwt = require("jsonwebtoken");

const client = new Client({
    host: "localhost",
    user: "admin",
    port: 5432,
    password: "uwure",
    database: "uwure"
})

const SECRET = "TOKEN_SECRET";

let drinkList;
let userList;
let users = [];
const apiRoute = express.Router();
var app = express();


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
    res.render('browse', { drinks: drinkList });
});

app.get('/favorite', function(req, res, next) {
    res.render('favorite', { drinksName: drinkList.drinkname });
});

app.get('/home', function(req, res, next) {
    res.render('index', { drinksName: drinkList.drinkname });
});

app.get('/register', function(req, res, next) {
    res.render('register');
});

app.get('/test', function(req, res, next) {
    console.log(drinkList)
    res.render('test',{ drinks: drinkList });
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
    const token = jwt.sign({ data: { username } }, SECRET);
    res.cookie("token", token, { httpOnly: true });
    res.redirect("/");
});

apiRoute.post("/login", (req, res) => {
    const { username, userpass } = req.body;
    let user;
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
    const token = jwt.sign({ data: { username: username } }, SECRET);
    res.cookie("token", token, { httpOnly: true });
    res.redirect("/home");
});

apiRoute.get("/logout", (req, res) => {
    res.clearCookie("token");
    res.redirect("/");
});

function authMiddleware(req, res, next) {
    const token = req.cookies.token;
    if (token)
        jwt.verify(token, SECRET, (err, decoded) => {
            req.user = err || decoded.data;
        });
    next();
}
app.use(authMiddleware);
module.exports = app;