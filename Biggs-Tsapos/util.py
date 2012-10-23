from pymongo import Connection

Conn = Connection('mongo.stuycs.org')

db = Conn.admin
res = db.authenticate('ml7','ml7')
print res
#db = Conn['pd6']
#col = db.first_collection
#tmp = col.find()
#for line in tmp:
#    print line
