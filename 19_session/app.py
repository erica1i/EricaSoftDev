'''
Henali: Erica (hugo), Henry (e), Aahan (spikes)
19_Session
SoftDev
2022-11-03
time spent: 0.5 hr

DISCO:
QCC: 

'''
from flask import Flask, session
app.secret_key = 'foo'

@app.route("/")
def login():
    if 'username' in session:
        return render_template('welcome.html')
    return render_template('login.html')

@app.route("/welcome")
def welcome(): 
    if  

if __name__ == "__main__":
    app.debug = False
    app.run()