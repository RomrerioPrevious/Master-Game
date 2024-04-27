var divCell = '<div id=c$coord class="cell"></div>';
var divChip = '<div id=f$coord class="chip">$name</div>';
var socket = io();
var map = new Array(144);
var room_id = 0;

$(function () {
  start();
  console.log("board has been created");
});

function start() {
    createField();
    var cookie = document.cookie.split("=");
    var url = document.URL.split("/");
    room_id = url[url.length - 1];
    console.log(room_id);
    socket.emit("join", {"room_id": room_id, "user_id": cookie[0]});
}

function createField() {
    $(".field").html("");
    for (var i = 0; i != 144; i++)
        $(".field").append(divCell.replace("$coord", i));
}

socket.on("join", (data) => {
    if (data != undefined) {
        console.log(data);
        for (char_name in data) {
            coord = data[char_name]["coordinates"];
            console.log(coord);
            char_name = makeRequest("{character(id: $char) {name}}"
                    .replace("$char", 0));
            const getName = async () => {
                new_name = await char_name
                showChip(coord, new_name["data"]["character"]["name"]);
            }
            getName();
        }
    }
});

socket.on("add_character", (socket) => {
    if (data != undefined) {
        for (char_name in data) {
            coord = data[char_name]["coordinates"];
            console.log(coord);
            const getName = async () => {
                new_name = await char_name
                console.log(new_name)
                showChip(coord, new_name["data"]["character"]["name"]);
            }
            getName();
        }
    }
});

socket.on("push_character", (socket) => {
    console.log(socket)
    newCoord = socket["coordinates"];
    oldCoord = socket["old_coords"];
    console.log(newCoord, oldCoord);
    moveChipNoEmit(oldCoord, newCoord, socket["name"]);
});

socket.on("leave", (socket) => {
    coord = socket["coords"];
    deleteChip(coord);
});

function setDroppable() {
  $(".cell").droppable({
    drop: function (event, ui) {
      var chipCoord = ui.draggable.attr("id").substring(1);
      var endCord = this.id.substring(1);
      moveChip(chipCoord, endCord, "F");
      setDraggable();
    },
  });
}

function setDraggable() {
  $(".chip").draggable();
}

function moveChip(startCoord, newCoord) {
    console.log("move from " + startCoord + " to " + newCoord);
    chip = map[startCoord];
    showChip(newCoord, chip);
    deleteChip(startCoord);
    setDroppable();
    socket.emit("push_character", {"room": 1, "coordinates": newCoord, "character": chip, "old_coords": startCoord, "name": chip})
}

function moveChipNoEmit(startCoord, newCoord, chip_name) {
    console.log("move from " + startCoord + " to " + newCoord);
    chip = map[startCoord];
    showChip(newCoord, chip_name);
    deleteChip(startCoord);
    setDroppable();
}

function showChip(coord, name) {
    map[coord] = name;
    $("#c" + coord).html(divChip.replace("$coord", coord).replace("$name", name));
    setDraggable();
    setDroppable();
}

function deleteChip(coord) {
  $("#c" + coord).html("");
  console.log("delete");
}

function addCharacter(name) {
    emit("add_character", {room: room_id})
}
