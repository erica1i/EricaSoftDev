## Predictions
Q0: Flask will not be able to render the templates folder, and thus
will return an error as it will not be able to access the code inside
the templates folder with html files.

Q1: http://127.0.0.1:5000/my_foist_template

Q2:
- render_template() looks for a template folder and renders it into use
- 'model_tmplt.html' goes into the file in the template folder named 'model_tmplt.html'
- foo="fooooo" access the {{ foo }} variable in HTML file in the template folder to
have the value of "fooooo" allowing for the title to be seen as "fooooo"
- collection = coll gives the {{ collection }} variable in the HTML file in the
template folder to have the value of "coll" allowing for the body to display
[0,1,1,2,3,5,8]
