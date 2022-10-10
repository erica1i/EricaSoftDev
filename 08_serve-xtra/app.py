'''
Holi Goramali: Erica (Hugo), Gordon (The Blueman)
Soft Dev
K08 Serve - Creating Flask
2022-10-07
time spent:

'''
import random
from flask import Flask
from simple_colors import *

app = Flask(__name__)

occupations_file = open("occupations.csv", "r")
content = occupations_file.read()
library = {"Job Class":[],
           "Percentage":[]
                }
new_content = content.split('\n')

temp = []
library = {"Job Class":[],
           "Percentage":[]
                }
for i in range(len(new_content)-1):
    temp += (new_content[i].rsplit(",",1))

for i in range(2,len(temp)-2,2):
    library["Job Class"].append(temp[i])
    library["Percentage"].append(float(temp[i+1]))

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def choose_occupations():
    options = library["Job Class"]
    option_weights = library["Percentage"]
    o = (random.choices(options, weights=option_weights))
    return o

def job_lister():
    jobs = green('OCCUPATIONS', 'bold') + "<br/>"
    for values in library["Job Class"]:
        jobs += values + "<br/>"

    print (green('OCCUPATIONS', 'bold'))
    return jobs

@app.route("/")
def hello_world():
    print(__name__)
    printed = "Holi Goramali: Erica (Hugo), Gordon (The Blueman)" + "<br> <br>"
    occupation = choose_occupations()
    printed += occupation[0] + "<br/> <br/>"
    printed += job_lister()
    return printed

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
