from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/")
def index():
    zagolovok = "zzz"
    per1 = {"name": "Danya", "age": 13, "game": "CS:GO", "image": "res/sss.jpg"}
    per2 = {"name": "Aleksei", "age": 21, "game": "atomic", "image": "res/hhh.jpg"}
    per3 = {"name": "Misha", "age": 15, "game": "Dota2", "image": "res/ddd.jpg"}
    people = [per1, per2, per3]
    return render_template("index.html", zagolovok = zagolovok, data = people)

@app.route("/second")
def second():
    return render_template("second.html")