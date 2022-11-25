var host = window.location.host;
var socket = io.connect('http://' + host);

function uwu(drinkID,userID) {
    socket.emit('randomRecipe', { drinkID: drinkID, userID:userID})
}
