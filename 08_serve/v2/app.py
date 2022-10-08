'''
Holi Goramali: Erica (hugo), Gordon (The Blueman)
SoftDev
v2 -- Intro to Flask
Time: 0.1 hr

PREDICTION:
It will print "about to print __name__..." in the terminal and then everything else
will be the same as the other app.py in v0.

EDITED:
It only printed "about to print__name__..." after I clicked the link to the site.
'''

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.run()
