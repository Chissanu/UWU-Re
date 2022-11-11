var createError = require('http-errors');
var express = require('express');
var path = require('path');
var logger = require('morgan');
const { Client } = require('pg')

const client = new Client({
    host: "localhost",
    user: "admin",
    port: 5432,
    password: "uwure",
    database: "uwure"
})

let drinkList;
var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');

app.get('/', function(req, res, next) {
    res.render('index', { title: 'Express' });
});

app.get('/home', function(req, res, next) {
    res.render('test', { title: 'Express' });
});

app.get('/favorite', function(req, res, next) {
    console.log(drinkList);
    res.render('favorite', { drinks: drinkList });
});

const setDrinkList = (rows) => {
    drinkList = rows;
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
module.exports = app;