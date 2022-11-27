var host = window.location.host;
var socket = io.connect('http://' + host);

function uwu(drinkID, userID) {
    socket.emit('uwuTime', { drinkID: drinkID, userID: userID })
}


function goHome() {
    window.location.replace("/home");
}