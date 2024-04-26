var divCell = '<div id=c$coord class="cell"></div>'

$(function (){
    create_field()
    console.log("board has been created");
});

function create_field() {
    $(".field").html("");
    for (var i = 0; i != 144; i++)
        $(".field").append(divCell.replace("$coord", i));
}