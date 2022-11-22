'''
stevejobsghost: Verit Li (Nibbles), Erica Li (Hugo)
K20 - REST API
Soft Dev
2022-11-22
time spent:
'''

from flask import Flask, session, request, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = 'foo'

@app.route("/") #, methods = ['POST'])
def main page(): 
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    return render_template('login.html')