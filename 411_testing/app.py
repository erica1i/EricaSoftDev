from flask import Flask, render_template
import requests # requires $ python -m pip install requests
import json

app = Flask(__name__)

@app.route('/')
def display():
  # No Key
  baseurl = "https://ghibliapi.herokuapp.com"
  endpoint = "films"
  filmID = "2baf70d1-42bb-4437-b551-e5fed5a87abe" # this is an arbitrary id from the film list
  url = f"{baseurl}/{endpoint}/{filmID}" #  url format
  # print(url)
  data = json.loads(requests.get(url).text)  # open the url and then using json.load to convert the page to a json file
  # print(data)
  return render_template('main.html', id=data["id"], title=data["title"], original_title=data["original_title"], description=data["description"], rt_score=data["rt_score"])

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()