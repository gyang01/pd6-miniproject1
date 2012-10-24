from pymongo import Connection

class mongo:
    def __init__(self):
        self.connection = Connection('mongo.stuycs.org')
        self.db = self.connection.admin
        self.db.authenticate('ml7','ml7')
        self.db = self.connection['Sofia-Sarah']
        self.db.stories.drop()

    def newStory(self, title):
        self.db.stories.insert({'title':title,'lines':[]})

    def getStories(self):
        return [x['title'] for x in self.db.stories.find()]

    def newLine(self,title,line):
        s = self.db.stories
        story = [x for x in s.find({'title':title})]
        if len(story) != 1:
            return
        l = story[0]
        l['lines'].append(line)
        s.update({'title':title},l)

    def getLines(self,title):
        return self.db.stories.find({'title':title})[0]['lines']

if __name__ == '__main__':
    db1 = mongo()
    db1.newStory("Pride and Prejudice")
    db1.newStory("The Picture of Dorian Grey")
    print db1.getStories()
    db1.newLine("Pride and Prejudice","It is a truth universally acknowledged")
    print db1.getLines("Pride and Prejudice")
    
        
