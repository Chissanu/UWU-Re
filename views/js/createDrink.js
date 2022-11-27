var host = window.location.host;
var socket = io.connect('http://' + host);

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

function randomRecipe(drinkID, userID) {
    socket.emit('randomRecipe', { drinkID: drinkID, userID: userID })
    window.location.replace("/recipe");
}

function randomDrink(drinkID, userID) {
    socket.emit('randomDrink', { drinkID: drinkID, userID: userID })
    window.location.replace("/randomDrink");
}