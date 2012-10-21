from pymongo import Connection
global connection
global db
global res
global col

def auth():
    global connection
    global db
    global res
    global col
    connection = Connection('mongo.stuycs.org')
    db = connection.admin
    res = db.authenticate ('ml7', 'ml7')
    db = connection['z-pd6']
    col = db['DLWS']

def 
