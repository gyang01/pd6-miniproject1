from pymongo import Connection
global db
global res
global col
global Connection
Connection=Connection("mongo.stuycs.org")
def con():
    global db
    global res
    global col
    global Connection
    db = Connection.admin
    res=db.authenticate('ml7','ml7')
    db = Connection['SoTe-pd6']
def addstory(story):
    entry= {"story":story, "text":[]}
    for x in db.stories.find():
        if (x['story']==story):
            return
    db.stories.save(entry)
 
def getstories():
    array = []
    for x in db.stories.find():
        array.append(x['story'])
    print array
    return array
def addcontent(story, line):
    for valjean in db.stories.find({'story':story}):
        array = valjean['text']
        array.append(line)
        db.stories.update({'story':story}, {'story': story,'text':array})
def access_story(story):
    for javert in db.stories.find({'story':story}):
        ans = story
        for i in javert['text']:
            print i
            print str(i)
            mod = str(i)
            ans= ans+ " " + str(i) 
    return ans

def get_story(story):
    for javert in db.stories.find({'story':story}):
        ans = story
        for i in javert['text']:
            mod = str(i)
            ans= ans+ " " + str(i) 
    return ans
 

#for line in db.stories.find():
#            print str(line)
 #   db.stories.update({story
#for line in db.stories.find():
 #   print line
#for line in db.stories.find({"story":'the worst thing ever invented'}):
 #               print str(line)
  #              print str(line['text'])
