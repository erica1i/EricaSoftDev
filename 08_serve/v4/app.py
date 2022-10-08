'''
Holi Goramali: Erica (hugo), Gordon (The Blueman)
SoftDev
v3 -- Intro to Flask
Time: 0.1 hr

PREDICTION:
Same thing printed and linked as v3/app.py

EDITED:
Prediction was right :D
'''
from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
