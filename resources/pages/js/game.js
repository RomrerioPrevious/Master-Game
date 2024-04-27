var divCell = '<div id=c$coord class="cell"></div>';
var divChip = '<div id=f$coord class="chip">$name</div>';
var socket = io();
var map = new Array(144);

$(function () {
  start();
  console.log("board has been created");
});

function start() {
    createField();
    var cookie = document.cookie.split("=");
    socket.emit("join", {"room_id": 1, "user_id": cookie[0]});
}

function createField() {
    $(".field").html("");
    for (var i = 0; i != 144; i++)
        $(".field").append(divCell.replace("$coord", i));
}

socket.on("join", (data) => {
    if (data != undefined) {
        for (char_name in data) {
            coord = data[char_name]["coord"];
            console.log(coord);
            char_name = makeRequest("{character(id: $char) {name}}"
                    .replace("$char", char_name));
            showChip(coord, char_name[0]);
        }
    }
});

socket.on("add_character", (socket) => {
    coords = element["coords"];
    char = element["character"];
    char_name = makeRequest("{character(id: $char) {name}}"
        .replace("$char", char));
    showChip(coord, char_name[0]);
});

socket.on("push_character", (socket) => {
    newCoord = element["new-coords"];
    oldCoord = element["old-coords"];
    char_name = makeRequest("{character(id: $char) {name}}"
        .replace("$char", char));
    deleteChip(oldCoord)
    showChip(newCoord, char);
});

socket.on("leave", (socket) => {
    coord = element["coords"];
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
    socket.emit("push_character", {"room": 1, "coordinates": newCoord, "character": chip, "old_coords": oldCoord})
}

function showChip(coord, name) {
    map[coord] = name;
    $("#c" + coord).html(divChip.replace("$coord", coord).replace("$name", name));
    setDraggable();
    setDroppable();
}

function deleteChip(coord) {
  $("#c" + coord).html("");
}
