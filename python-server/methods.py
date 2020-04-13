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
 
def getTaskClass(sk, Task):
    tasks = Task.query.all()
    for n in tasks:
        if n.task_secret_key == sk:
            return n
    else:
        return False

def taskToJson(n):
    return {"id":n.id, "name": n.name, 
            "employer_username": n.employer_username, 
            "employee_username": n.employee_username,
            "employer_secret_key": n.employer_secret_key,
            "employee_secret_key": n.employee_secret_key, 
            "task_secret_key": n.task_secret_key, 
            "isDone": n.isDone,
            "importanceLevel": n.importanceLevel, 
            "deadline": n.deadline}

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
    return False

def getDataClass(username, User):
    users = User.query.all()
    for n in users:
        if n.username == username:
            return n
    return False

def getData(username, User):
    users = User.query.all()
    for n in users:
        if n.username == username:
            return userToJson(n)
    return False

def randomStringGenerator(stringLength):
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(stringLength))
