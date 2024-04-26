var divCell = '<div id=c$coord class="cell"></div>'
var divChip = '<div id=f$coord class="chip">$name</div>'
var map;

$(function (){
    start();
    console.log("board has been created");
});

function start() {
    map = new Array(64);
    createField();
    showChip(1, "F");
    showChip(22, "N");
}

function createField() {
    $(".field").html("");
    for (var i = 0; i != 144; i++)
        $(".field").append(divCell.replace("$coord", i));
}

function setDroppable() {
    $(".cell").droppable({
        drop:   function (event, ui) {
                    var chipCoord = ui.draggable.attr("id").substring(1);
                    var endCord = this.id.substring(1);
                    moveChip(chipCoord, endCord, "F");
                    setDraggable();
                }
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
}

function showChip(coord, name) {
    map[coord] = name;
    $("#c" + coord).html(divChip
        .replace("$coord", coord)
        .replace("$name", name));
    setDraggable();
    setDroppable();
}

function deleteChip(coord) {
    $("#c" + coord).html("");
}