from pymongo import Connection

#Comm-link established
#conn = Connection('mongo.stuycs.org')

#I am ADMIN
#db = conn.admin
#AUTHENTICATION = db.authenticate('ml7','ml7')

#Lets go period 6
#db = conn['z-pd6']

#Our storybook <3
#col = db["WinBall's StoryBook"]

class db:
    
    def __init__(self):
        self.conn = Connection('mongo.stuycs.org')
        self.db = self.conn.admin
        self.db.authenticate('ml7','ml7')
        self.db = self.conn['z-pd6']
        self.col = self.db["WinBall's StoryBook"]
        
    def newStory(self, name):
        self.col.insert({'name': name, 'lines': 0}) 

    def newStoryStart(self, name, start):
        self.col.save({'name': name, 'lines': 0, 'text':start}) 
    
    def continueStory(self, name, addition):
        self.col.update({'name':name}, {'$inc': {'lines':1}})
        self.col.update({'name':name}, {'$push': {'text':addition}})
    
    def printStory(self, name):
        entries = self.col.find({'name':name},{'text':1})[0]['text']
        for entry in entries:
            print entry;

    def getStoryNames(self):
        names = []
        for story in self.col.find():
            names.append(story['name'])
            return names

    def getText(self, name):
        return self.col.find({'name':name},{'text':1})[0]['text']

    def remove(self, name):
        self.col.remove({'name':name})

if __name__ == "__main__":
    
    mydb = db()
    
    mydb.newStory("Hello World!")
    mydb.newStory("Story2")
    mydb.continueStory("Hello World!","hallo")
    mydb.continueStory("Story2", "There once was a man from australia")
    mydb.continueStory("Story2", "Whose limericks were quite a failure")
    
    test = 5
    
    for line in mydb.col.find():
        print line
        
    print

    for name in mydb.getStoryNames():
        print name

    print
    print

    mydb.printStory('Story2')
    
    print
    print
    
    text = mydb.getText("Story2")
   # print text
    mydb.col.drop()
