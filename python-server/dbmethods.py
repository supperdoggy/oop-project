from methods import *

def addItem(db, item):
    db.session.add(item)
    db.session.commit()

def listAllTasksIdByOwner(username, Task):
    tasks = Task.query.all()
    m = ""
    for n in tasks:
        if n.employer_username == username:
            m+=f"{n.id},"
    return m

def listAllTasksIdByEmployee(username, Task):
    tasks = Task.query.all()
    m = ""
    for n in tasks:
        if n.employee_username == username:
            m+=f"{n.id},"
    return m

def createTask(db, Task, user_json, User):
    task = Task(name=user_json["name"], text=user_json["text"], 
    employer_username=user_json["employer_username"], employee_username=user_json["employee_username"]
    , employer_secret_key=getData(user_json["employer_username"], User)["user_secret_key"], 
    employee_secret_key=getData(user_json["employee_username"], User)["user_secret_key"], 
    task_secret_key=randomStringGenerator(24), importanceLevel=user_json["importanceLevel"], 
    deadline=user_json["deadline"])

    db.session.add(task)
    db.session.commit()