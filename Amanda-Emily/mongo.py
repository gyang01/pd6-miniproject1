from pymongo import Connection

Connection = Connection('mongo.stuycs.org')
db = Connection.admin
res= db.authenticate('ml7','ml7')
db = Connection['AmandaEmily-pd6']

