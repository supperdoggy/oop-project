from flask import Flask, jsonify, request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from methods import *
from constants import *
from dbmethods import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///main.db"
db = SQLAlchemy(app=app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_secret_key = db.Column(db.String(25), unique=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    tasks_to_do = db.Column(db.String, default="")
    tasks_created = db.Column(db.String, default="")
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repl__(self):
        return "<%s>"%self.username

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    text = db.Column(db.String)
    employer_username = db.Column(db.String)
    employee_username = db.Column(db.String)
    employer_secret_key = db.Column(db.String(25))
    emplouee_secret_key = db.Column(db.String(25))
    task_secret_key = db.Column(db.String, unique=True)


    def __repl__(self):
        return "<Task %s>"%self.id
    

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_json = request.get_json()
        if accessEnabled(user_json, db, User):
            return jsonify(getData(user_json["username"], User))
        else:
            return jsonify({"ok":False}) 
        
@app.route("/register", methods=["GET","POST"])
def reg():
    if request.method == "POST":
        user_json = request.get_json()
        new_user = User(user_secret_key=randomStringGenerator(24), username=user_json["username"], password=user_json["password"])
        addItem(db, new_user)
        return jsonify(getData(user_json["username"], User))
    else:
        return jsonify({"ok":False})

@app.route("<secret_key>/taskstodo", methods=["GET", "POST"])
def tasksToDo(secret_key):
    if verifySecretKey(secret_key, User):
        return jsonify(getDataBySK(secret_key, User))
    else:
        return jsonify({"ok":False})
@app.route("/")
def hello():
    return "Hello!"

if __name__ == '__main__':
    app.run(debug=True)