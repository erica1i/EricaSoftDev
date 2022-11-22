'''
stevejobsghost: Verit Li (Nibbles), Erica Li (Hugo)
K20 - REST API
Soft Dev
2022-11-22
time spent: 0.5 hr
'''

import requests
from flask import Flask, render_template

app = Flask(__name__)


with open('key_nasa.txt') as f:
    key = f.read()

#print(key)
nasa_url = "https://api.nasa.gov/planetary/apod?api_key=" + key
print(nasa_url) #prints the nasa_url with key to the console
res = requests.get(nasa_url) 
pic_url = json["url"] #finds the key named url in the json file 

@app.route("/")
def picture():
    return render_template('main.html', url=pic_url)
    
if __name__ == "__main__":
    app.debug = True
    app.run()
