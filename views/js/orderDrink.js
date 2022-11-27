var host = window.location.host;
var socket = io.connect('http://' + host);


function orderDrink(drinkID, userID) {
    socket.emit('order', { drinkID: drinkID, userID: userID })
}

function favDrink(drinkID, userID) {
    socket.emit('fav', { drinkID: drinkID, userID: userID })
}

function goHome() {
    window.location.replace("/home");
}

function goCreate() {
    window.location.replace("/create");
}

function goFavorite() {
    window.location.replace("/favorite");
}

function goBrowse() {
    window.location.replace("/browse");
}