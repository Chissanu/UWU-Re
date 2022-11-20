// function orderDrink(orderID,userID) {
//     //window.location.href = '/api/test2';
//     const data = "HELLLLLLLLLLLLLLLLLLL"
//     fetch('/api/test2', {
//     method: 'POST',
//     body: JSON.stringify({ data }),
//     headers: { 'Content-Type': 'application/json' }
//     })
//     .then(response => response.text())
//     .then(data => console.log(data))
//     .catch(err => console.log(err))
//     console.log(`${userID} ordered ${orderID}`)
// }

var host = window.location.host;
var socket = io.connect('http://' + host);


function orderDrink(drinkID,userID) {
    socket.emit('order', { drinkID: drinkID, userID:userID})
}

