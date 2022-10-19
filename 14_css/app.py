'''
Henali: Erica (hugo), Henry (e), Aahan (Spikes)
14_css - Using Flask & Dev Console
SoftDev
2022-10-19
time spent: 0.2 hr
'''

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def first_proj(): 
    return render_template( 'index.html' )

if __name__ == "__main__":
    app.debug = True
    app.run()