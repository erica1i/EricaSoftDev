'''
stevejobsghost: Verit Li (Nibbles), Erica Li (Hugo)
K20 - REST API
Soft Dev
2022-11-22
time spent:
'''

from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)

@app.route("/") #, methods = ['GET'])
def main(): 
    key = (open('key_nasa.txt')).read()
    url = "https://api.nasa.gov/planetary/apod?api_key=" + key
    json_url = urllib.request.urlopen(url)

if __name__ == "__main__":
    app.debug = True
    app.run(port=2528)