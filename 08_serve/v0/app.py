'''
Holi Goramali: Erica (hugo), Gordon (The Blueman)
SoftDev
v0 -- Intro to Flask
Time: 0.1 hr

PREDICTION:
We expect the terminal to print a link and once we click on the link,
it generates a website and the page says No hablo queso!

EDITED:
After clicking the link, the terminal prints "__main__" where main stands for the name?
'''

from flask import Flask
app = Flask(__name__) # ...

@app.route("/") # ...
def hello_world():
    print(__name__) # ...
    return "No hablo queso!"  # ...

app.run()  # ...
