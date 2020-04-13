

def addItem(db, item):
    db.session.add(item)
    db.session.commit()