'''
Henali: Erica (hugo), Henry (e), Aahan (spikes)
19_Session
SoftDev
2022-11-03
time spent: 2.5 hr

DISCO:
QCC:

'''
from flask import Flask, session, request, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = 'foo'

@app.route("/") #, methods = ['POST'])
def login():
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    return render_template('login.html')

@app.route("/welcome", methods = ['POST'])
def welcome():
    if request.method == "POST" :
        if request.form.get('username') == "Foo" and request.form.get('password') == "Bar" :
            session['username'] = request.form.get('username')
            return render_template('welcome.html', username=session['username'])
    return render_template('login.html', additional="Incorrect Username or Password")

@app.route("/logout", methods = ['POST'])
def logout():
    session.pop('username')
    return redirect(url_for('login'))

# @app.route("/test")
# def test():
#     return "test"

if __name__ == "__main__":
    app.debug = True
    app.run(port=1026)
