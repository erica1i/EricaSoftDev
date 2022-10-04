'''
JeLifish Trio: Jian Hong Li (JHL), Verit Li (Nibbles), Erica Li (Hugo)
Soft Dev
K07 -- Intro to Flask
2022-10-03
time spent:

'''

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?
                          # When declaring/intiating new objects (ie Stack<Integer> = new Stack())

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
                    # In python, '/' continues the next line to the current line
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
                    # It printed to the terminal itself and printed a new site/link.
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?
                                # "No hablo queso!" appeared on the screen when you clicked the link printed.
                                #  I knew this because I downloaded the Flask package and was able to print out
                                #  the proper link and clicked on it

app.run()  # Q5: Where have you seen similar constructs in other languages?
            # Java!


'''
DISCO:
- Flask will print/link links to new sites/pages

QCC: 
1. Stack in java? Is that related somehow?
2. What does the @ sign do?
3.Where is the name printed? Is it printed anymore? Does a name represent the link? 

...
INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''
