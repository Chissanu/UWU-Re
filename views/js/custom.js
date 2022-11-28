var host = window.location.host;
var socket = io.connect('http://' + host);


var pump1 = document.getElementById('pump1Val'),
    pump2 = document.getElementById('pump2Val'),
    pump3 = document.getElementById('pump3Val'),
    pump4 = document.getElementById('pump4Val'),
    pump5 = document.getElementById('pump5Val'),
    pump6 = document.getElementById('pump6Val'),
    totalVal = document.getElementById('totalMl')


var totalAmount = 0,
    p1 = 0,
    p2 = 0,
    p3 = 0,
    p4 = 0,
    p5 = 0,
    p6 = 0

function increase(pumpID) {
    if (pumpID == 1) {
        p1 += 1
        pump1.innerHTML = p1
    }
    if (pumpID == 2) {
        p2 += 1
        pump2.innerHTML = p2
    }
    if (pumpID == 3) {
        p3 += 1
        pump3.innerHTML = p3
    }
    if (pumpID == 4) {
        p4 += 1
        pump4.innerHTML = p4
    }
    if (pumpID == 5) {
        p5 += 1
        pump5.innerHTML = p5
    }
    if (pumpID == 6) {
        p6 += 1
        pump6.innerHTML = p6
    }
    totalAmount = p1 + p2 + p3 + p4 + p5 + p6
    totalVal.innerHTML = totalAmount + "/" + "10"
}

function decrease(pumpID) {
    if (pumpID == 1) {
        if (p1 > 0) {
            p1 -= 1
            pump1.innerHTML = p1
        }
    }
    if (pumpID == 2) {
        if (p2 > 0) {
            p2 -= 1
            pump2.innerHTML = p2
        }
    }
    if (pumpID == 3) {
        if (p3 > 0) {
            p3 -= 1
            pump3.innerHTML = p3
        }
    }
    if (pumpID == 4) {
        if (p4 > 0) {
            p4 -= 1
            pump4.innerHTML = p4
        }
    }
    if (pumpID == 5) {
        if (p5 > 0) {
            p5 -= 1
            pump5.innerHTML = p5
        }
    }
    if (pumpID == 6) {
        if (p6 > 0) {
            p6 -= 1
            pump6.innerHTML = p6
        }
    }
    totalAmount = [p1 + p2 + p3 + p4 + p5 + p6]
    totalVal.innerHTML = totalAmount + "/" + "10"
}

function getTotal() {
    data = [p1, p2, p3, p4, p5, p6]
    socket.emit('total', { totalVal: data })
    window.location.replace("/createCustom");
}

function save(username) {
    var name = document.getElementById('nameBox').value
    socket.emit('save', { userID: username, name: name })
}

function goHome() {
    window.location.replace("/home");
}