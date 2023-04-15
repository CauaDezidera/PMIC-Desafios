from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/")
def quemsomos():
    return render_template("quemsomos.html")
     
@app.route("/")
def contato():
    return render_template("contato.html")
     
     
     
