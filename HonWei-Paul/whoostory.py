from pymongo import Connection
c = Connection('mongo.stuycs.org')
db = c.admin
res=db.authenticate('ml7','ml7')
db = c['KhorMa-pd6']
stories = db.storynator

def addstory(name):
    if not exists(name):
        stories.save({'Title':name,'Storytext':[]})
        
def exists(name):
    return str(stories.find_one({'Title':name}))!='None'

def getstory(name):
    return stories.find_one({'Title':name})

def getstorytext(name):
    a = getstory(name)[u'Storytext']
    for b in range(0,len(a)):
        a[b] = str(a[b])
    return a

def getstoryID(name):
    a = str(getstory(name)[u'_id'])
    return a
    
def addline(name,line):
    stories.update({'Title':name}, {'$push': {'Storytext':line}})

def getalltitles():
    a = stories.find()
    b = []
    for d in a:
        b.append(str(d[u'Title']))
    return b
def dropstories():
	stories.drop()
	
def dropspecstory(title):
	stories.remove({'Title':title})
