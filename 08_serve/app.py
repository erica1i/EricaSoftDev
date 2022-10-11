'''
Holi Goramali: Erica (Hugo), Gordon (The Blueman)
Soft Dev
K08 Serve - Creating Flask
2022-10-07
time spent:

DISCO:
1. <br/> allows a line break
2. app.debug enable auto-reload upon code change
3. @app.route() must be after all the functions or else the site
will not generate

QCC:
How can you change up the color generated on the site?
Is there a way to add a background to the site?
'''
import random
from flask import Flask

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

def choose_occupations(): #chooses the occupation based on the weight
    options = library["Job Class"]
    option_weights = library["Percentage"]
    o = (random.choices(options, weights=option_weights))
    return o

def job_lister(): #lists all the jobs neatly through line breaks
    jobs = ""
    for values in library["Job Class"]:
        jobs += values + "<br/>"
    return jobs

@app.route("/")
def hello_world():
    print(__name__)
    printed = "TNPG: Holi Goramali: Erica (Hugo), Gordon (The Blueman) <br/> <br/>"
    occupation = choose_occupations()
    printed += occupation[0] + "<br/> <br/>"
    printed += job_lister()
    return printed

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = False        # enable auto-reload upon code change
    app.run()
