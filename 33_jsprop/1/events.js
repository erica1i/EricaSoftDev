// demo 1
// JS event propagation
// the code first gets all elements in cell form, and for each one you click, a popup appears with the clicked text in it

var tds = document.getElementsByTagName('td'); //gets elements tagged with td (data cell)

var clicky = function(e) {
  alert( this.innerHTML ); //alert function: displays text in popup
};

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky); //for each cell element you click, call clicky
}