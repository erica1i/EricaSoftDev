'''
Henali: Erica (hugo), Henry (e), Aahan (Spikes)
12_flask-forms - Figuring out POST
SoftDev
2022-10-17
time spent: 0.5 hr
'''

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
Some will work as written; other sections will not.
TASK: Predict which...
Devise some simple tests you can run to "take apart this engine," as it were.
Execute your tests.
Process results.

PROTIP: Insert your own in-line comments
 wherever they will help
  your future self and/or current teammates
   understand what is going on.
'''

@app.route("/" , methods = ['GET', 'POST'])
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app) #prints <Flask 'app' >
    print("***DIAG: request obj ***")
    print(request) #prints <Request 'http://127.0.0.1:5000/' [GET]>
    print("***DIAG: request.args ***")
    print(request.args) #prints ImmutableMultiDict([])
    print("***DIAG: request.args['username']  ***")
    # print(request.args['username']) #ERROR
    # print("***DIAG: request.headers ***") #ERROR
    print(request.headers)
    return render_template( 'login.html' )


@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app) #prints <Flask 'app'>
    print("***DIAG: request obj ***")
    print(request) #prints <Request 'http://127.0.0.1:5000/auth?username=eli30&sub1=Submit' [GET]>
    print("***DIAG: request.args ***")
    print(request.form) #prints ImmutableMultiDict([('username', 'eli30'), ('sub1', 'Submit')])
    print("***DIAG: request.args['username']  ***")
    print(request.form.get('username')) #prints eli30
    print("***DIAG: request.headers ***")
    print(request.headers)
    print("FORMS")
    print(request.form)
    if request.method == 'POST':
        return render_template( 'response.html', username = request.form.get('username'), method = request.method)


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
