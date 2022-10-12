'''
Holi Goramali: Erica (Hugo), Gordon (The Blueman)
Soft Dev
K09 Flask-Static 
2022-10-11
time spent:

DISCO: The web server serves the text in html.
<head> text here </head> changes the name of the tab to whatver is inside head.
QCC:
'''

from flask import Flask
app = Flask(__name__) 

@app.route("/")       
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
