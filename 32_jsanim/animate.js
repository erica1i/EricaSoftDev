// access canvas and buttons via DOM 
var c = document.getElementById("playground"); // get canvas
var dotButton = document.getElementById("buttonCircle");// Get Dot button
var dvdButton = document.getElementById("dvd");
var stopbutton = document.getElementById("buttonStop");// Get stop button


// instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

ctx.fillStyle = 'turquoise'

var requestID; // init global var for use with animation frames

var clear = function(e) {
    //e.preventDefault(); // 
    ctx.clearRect(0,0,c.width,c.height)
};

var radius = 0;
var growing = true; 

var drawDot = () => {
    /*
    Wipe the canvas, 
    Repaint the circle, 
    ... and somewhere (where/when is the right time?)
    Update requestID to propagate the animation. 
    You will need
    window.cancelAnimationFrame()
    window.requestAnimationFrame()
    */

    clear();
   if(growing && radius > c.width/2){
    growing = false;
   }else if (!growing && radius <= 0){
    growing = true;
   }

   if (growing){
        radius++;  
    }else{
        radius--; 
    }

    ctx.beginPath();
    ctx.arc(c.width/2, c.height/2, radius, 0, 2 * Math.PI, false); 
    ctx.fill();

    window.cancelAnimationFrame(requestID);
    requestID = window.requestAnimationFrame(drawDot);
};

//var stopIt = function() {
var stopIt = () => {
    console.log("stopIt invoked...")
    console.log(requestID);    

    /* Your code here 
    ... to stop the animation
    You will need window.cancelAnimationFrame()
    */
    window.cancelAnimationFrame(requestID);
};

var dvdLogoSetup = function() {
    window.cancelAnimationFrame(requestID);

    var rectWidth = 60
    var rectHeight = 40

    var rectX = Math.random() * 500// construct for selecting random valid xcor
    var rectY = Math.random() * 500// construct for selecting random valid ycor

    var xVel = 1
    var yVel = 1

    var logo = new Image();
    logo.src = "logo_dvd.jpg"

    var dvdLogo = function() {
        ctx.clearRect(0,0, c.width, c.height);
        ctx.drawImage(logo, rectX, rectY, rectWidth, rectHeight);
        // bounce criterai
        if (rectX + rectWidth > c.width || rectX < 0){
            xVel = xVel * -1
        }
        if (rectY + rectHeight > c.height || rectY < 0){
            yVel = yVel * -1
        }
        rectX = rectX + xVel
        rectY = rectY + yVel
        requestID = window.requestAnimationFrame(dvdLogo);
    }
    dvdLogo();

}
dotButton.addEventListener("click", drawDot);
dvdButton.addEventListener("click", dvdLogoSetup)
stopbutton.addEventListener("click", stopIt);
