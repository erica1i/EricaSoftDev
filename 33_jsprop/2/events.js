// demo 2
// JS event propagation

var tds = document.getElementsByTagName('td'); //gets data cells
var trs = document.getElementsByTagName('tr'); //gets row
var table = document.getElementsByTagName('table')[0]; //gets entire table

//popup
var clicky = function(e) {
  alert( this.innerHTML );
};

//in this order: 

//(1) for each data cell, if you click it, call clicky
for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky);
}

//(2) for each row, if you click it, call clicky (--> popup of entire row)
for (x=0; x < trs.length; x++) {
  trs[x].addEventListener('click', clicky);
}

//(3) if you click the table, call clicky
table.addEventListener('click', clicky);


// Q: When user clicks on a cell, in what order will the pop-ups appear?
// events happen in the order of most specific to least specific
// the order they show up in the code doesn't matter
// if you click on a cell, you're also clicking on a row, and also clicking on the table
