var host = window.location.host;
var socket = io.connect('http://' + host);

function randomRecipe(drinkID,userID) {
    window.location.replace("/recipe");
    socket.emit('randomRecipe', { drinkID: drinkID, userID:userID})
}
