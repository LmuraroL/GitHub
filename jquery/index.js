$("h1").addClass("big-title");/*removeClass works in other way .hasClass search if the function has a specigy class*/
$("h1").text("Bye")/*change text*/
$("h1").click(function(){
    $("h1").css("color","red")
} /*addind a event listener*/)
$(document).keypress(function (event) { 
 $("h1").text(event.key)   
});/*show in h1 what key was press*, the tag "document" select all the html file*/
$("h1").mouseover(function () { 
    $("h1").css("color","gray")
});/*when the mouse is over, change color of h1*/