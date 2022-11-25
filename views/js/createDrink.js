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

function randomRecipe() {
    socket.emit('randomRecipe')
}

function randomDrink() {
    socket.emit('randomDrink')
}