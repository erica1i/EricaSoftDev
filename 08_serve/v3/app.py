'''
Holi Goramali: Erica (hugo), Gordon (The Blueman)
SoftDev
v3 -- Intro to Flask
Time: 0.1 hr

DISCO:
QCC:
What is debug? What does app being in debug mode mean?
When debug mode is on, there is no WARNING printed. 

EDITED:
The website generated cannot be reached when the link is clicked.
Maybe the debug mode is to let the creator first make sure the code works before
launching it onto the website and making it live for other users.
What is a module? 

'''

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.debug = True
app.run()
