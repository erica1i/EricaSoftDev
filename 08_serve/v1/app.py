'''
Holi Goramali: Erica (hugo), Gordon (The Blueman)
SoftDev
v1 -- Intro to Flask
Time: 0.1 hr

DISCO:

QCC:
We think that it will just return an ERROR. There will be nothing printed
and the website will be generated but we won't be given the link in terminal.

EDITED:
We were wrong. It printed the same thing as v0/app.py and generated the same site.
There was an absence of "__main__" printed on the terminal. 
'''

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

