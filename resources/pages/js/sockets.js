var socket = io();

socket.on("join", function() {
    socket.emit('my event', {data: "I'm connected!"});
    socket.emit("my event", {data: "I'm connected!"});
});

socket.on("push", function() {

})