import random, string

def accessEnabled(user_json, db, User):
    users = User.query.all()
    for n in users:
        if n.username == user_json["username"] and n.password == user_json["password"]:
            return True
    return False

def userToJson(n):
    return {"id":n.id, "user_secret_key":n.user_secret_key,
            "username":n.username, "password":n.password, 
            "tasks_to_do":n.tasks_to_do,"tasks_created":n.tasks_created, 
            "date_created":n.date_created, "ok":True}
 

def verifySecretKey(key, User):
    users = User.query.all()
    for n in users:
        if n.user_secret_key == key:
            return True
    return False

def getDataBySK(key, User):
    users = User.query.all()
    for n in users:
        if n.user_secret_key == key:
            return userToJson(n)

def getData(username, User):
    users = User.query.all()
    for n in users:
        if n.username == username:
            return userToJson(n)
            
def randomStringGenerator(stringLength):
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(stringLength))
