'''
JeLifish Trio: Jian Hong Li (JHL), Verit Li (Nibbles), Erica Li (Hugo)
Soft Dev
K07 -- Intro to Flask
2022-10-03
time spent:

'''

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
QCC:
0. When declaring/intiating new objects (ie Stack<Integer> = new Stack())
1. In python, '/' continues the next line to the current line
2. What Flask(_name_) is?

1. Stack in java? Is that related somehow?
2. What is app? What does the @ sign do? 
...
INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''
