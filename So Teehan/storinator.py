                                                                     
                                                                     
                                                                     
                                             
from pymongo import Connection
Connection=Connection('mongo.stuycs.org')
db = Connection.admin
res=db.authenticate('ml7','ml7')
db = Connection['SoTe-pd6']
db.stories.remove()
def addstory(story):
    entry= {"story":story, "text":[]}
    db.stories.save(entry)


addstory('the worst thing ever invented')
addstory('i dont know really')
addstory('arms and a man i sing')

def addcontent(story, line):
    for valjean in db.stories.find({'story':story}):
        array = valjean['text']
        array.append(line)
        db.stories.update({'story':story}, {'story': story,'text':array})

addcontent('the worst thing ever invented', 'was facebook')
addcontent('the worst thing ever invented', 'because of the procrastination')
def access_story(story):
    for javert in db.stories.find({'story':story}):
        ans = story
        for i in javert['text']:
            print i
            print str(i)
            mod = str(i)
            ans= ans+ " " + str(i) 
    print ans
access_story('the worst thing ever invented')



#for line in db.stories.find():
#            print str(line)
 #   db.stories.update({story
#for line in db.stories.find():
 #   print line

#for line in db.stories.find({"story":'the worst thing ever invented'}):
 #               print str(line)
  #              print str(line['text'])
  
