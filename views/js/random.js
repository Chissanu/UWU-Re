var host = window.location.host;
var socket = io.connect('http://' + host);

function uwu(drinkID, userID) {
    socket.emit('uwuTime', { drinkID: drinkID, userID: userID })
    window.location.replace("/save");
}

function save(username) {
    var name = document.getElementById('nameBox').value
    socket.emit('save', { userID: username, name: name })
}

function goHome() {
    window.location.replace("/home");
}