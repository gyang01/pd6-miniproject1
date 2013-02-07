from pymongo import Connection

Conn = Connection('ds041367.mongolab.com',43487)
db = Conn['creativenonfiction']
res = db.authenticate('crtnonfic','615A')
mongo = db.CreativeNonFiction

def addWork(author,work,title,feedback):
    newWork = {'author':author,'work':work,'feedback':feedback,'title':title,'comments':[]}
    mongo.insert(newWork)

def getTitles():
    titles = []
    tmp = mongo.find()
    for piece in tmp:
        titles.append([str(piece['title']),str(piece['author'])])
    return titles

def getWork(title,author):
    tmp = mongo.find_one({'title':title, 'author':author})
    return [tmp['title'],tmp['author'],str(tmp['work']),tmp['comments'],tmp['feedback']]

def addComment(title,author,comment,commenter):
    tmp = mongo.find_one({'title':title, 'author':author})['comments']
    tmp.append([comment,commenter])
    mongo.update({'title':title, 'author':author},{'$set':{'comments':tmp}})

