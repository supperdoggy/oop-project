

def accessEnabled(user_json, db, User):
    users = User.query.all()
    for n in users:
        if n.username == user_json["username"] and n.password == user_json["password"]:
            return True
    return False

def getData(username, User):
    users = User.query.all()
    for n in users:
        if n.username == username:
            return {"id":n.id, "user_secret_key":n.user_secret_key,
                        "username":n.username, "password":n.password, 
                        "tasks":n.tasks, "date_created":n.date_created, "ok":True}
