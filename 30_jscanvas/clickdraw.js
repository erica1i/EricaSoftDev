// retrieve node in DOM via ID
var c = document.getElementById("slate")

// instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

// init global state var
var mode = "rect";

//var toggleMode = function(e) {
var toggleMode = (e) => {
    console.log("toggling...");
    if(mode == "rect"){
        mode = "circ"
        bToggler.innerHTML = "Circle"
    }
    else{
        mode = "rect"
        bToggler.innerHTML = "Rect"
    }
}

var drawRect = function(e) {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);
    
    ctx.beginPath()
    ctx.fillStyle = 'turquoise'
    ctx.strokeRect(mouseX, mouseY,50,140)
    ctx.fillRect(mouseX, mouseY,50,140)
    ctx.stroke()
}

//var drawCircle = function(e) {
var drawCircle = (e) => {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);

    ctx.beginPath()
    ctx.fillStyle = 'yellow'
    ctx.arc(mouseX, mouseY, 40, 0, 2 * Math.PI, false)
    ctx.fill()
    ctx.stroke()
}

//var draw = function(){
var draw = (e) => {
    if (mode == "rect"){
        drawRect(e)
    }
    else{
        drawCircle(e)
    }
}

//var wipeCanvas = function(){
var wipeCanvas = () => {
    ctx.clearRect(0,0,c.width,c.height);
}

c.addEventListener("click", draw);
var bToggler = document.getElementById("buttonToggle") ;
bToggler.addEventListener("click", toggleMode) ;
var clearB = document.getElementById("buttonClear") ;
clearB.addEventListener("click", wipeCanvas) ;