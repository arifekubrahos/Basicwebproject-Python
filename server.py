from flask import Flask
from flask import render_template
import json
import kelimeler
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api")
def api():
    mylist = [1,2,3,4]
    return render_template("index.html", mylist=mylist)

@app.route("/api/<kelime>")
def apiKelime(kelime):
    word = kelimeler.bolum(kelime)
    return json.dumps(word)

app.run(host='localhost', port=8000, debug=True)


