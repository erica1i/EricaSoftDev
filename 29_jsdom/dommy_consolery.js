// Team Hair Investment Uncles :: Daniel He, Justin Mohabir, Sir, Alfred
// SoftDev pd2
// K28 -- Getting more comfortable with the dev console and the DOM
// 2023-04-05w
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
// f is a function of x
// variable j still remained 20 after running f
// f(j)=50
// f(i)='30hello'
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
// works like a disctionary with o[key]
// function can be stored, and can be called with o['key'](input)
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };

// interacts with <ol id="thelist"> tag
var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};

//removes the item specified by n
var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};

//makes the items with no specified color become red
var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};

// After using stripe red does not work
var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

//insert your implementations here for...
// FIB

function fib(n) {
  if (n==0){
    return 0
  }
  if (n==1){
    return 1
  }
  return fib(n-1) + fib(n-2);
}

//addItem("fib(5): " + fib(5))

// FAC
function fac(n) {
  if (n<2){
    return 1
  }
  return n * fac(n-1);
}

//addItem("fac(5): " + fac(5))

// GCD
function gcd(a,b) {
  if (a==b){
    return b
  }
  else if (a>b) {
    return gcd(a-b,b)
  }
  else {
    return gcd(b-a,a);
  }
}

//addItem("gcd(27,36): " + gcd(27,36))

//looks at button with the corresponding id
var button = document.getElementById("fib");
//second parameter needs to be wrapped in a function, or else it is called automatically when the DOm renders 
button.addEventListener('click', ()=>{
  addItem("fib(5): " + fib(5));
});
var button = document.getElementById("fac");
button.addEventListener('click', ()=>{
  addItem("fac(5): " + fac(5));
});
var button = document.getElementById("gcd");
button.addEventListener('click', ()=>{
  addItem("gcd(27,36): " + gcd(27,36));
});
// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
  // body
  return param1+param2;
};
