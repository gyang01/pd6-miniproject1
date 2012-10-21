from pymongo import Connection
Connection=Connection('mongo.stuycs.org')
db = Connection.admin
res=db.authenticate('ml7','ml7')
db = Connection['SoTe-pd6']
<<<<<<< HEAD
storycontent = ''

def addstory(story):
    db.stories.save({'story':['string']})
    
def addcontent(story, line):
    for line in res:
        if line['story'] == story
            line['string'] = line['string' + line]
=======
db.stories.remove()
def addstory(story):
    entry= {"story":story, "text":[]}
    db.stories.save(entry)


>>>>>>> updated addcontent
    

addstory('the worst thing ever invented')
addstory('i dont know really')
addstory('arms and a man i sing')

def addcontent(story, line):
    for valjean in db.stories.find({'story':story}):
        array = valjean['text']
        array.append([line])
        db.stories.update({'story':story}, {'story': story,'text':array})

addcontent('the worst thing ever invented', 'was facebook')
addcontent('the worst thing ever invented', 'because of the procrastination')
for line in db.stories.find():
            print str(line)
 #   db.stories.update({story
#for line in db.stories.find():
 #   print line

#for line in db.stories.find({"story":'the worst thing ever invented'}):
 #               print str(line)
  #              print str(line['text'])
  
