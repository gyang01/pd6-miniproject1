from pymongo import *

global connection, db, res, col

def auth():
     global connection, db, res, col   
     
     connection = Connection('mongo.stuycs.org')
     db = connection.admin
     res = db.authenticate('ml7', 'ml7')
     db = connection['z-pd6']
     col = db['sk']

#    New story
def addStory(title, line):    
     global col
     col.insert({'title': title, 'text': [line]})
     print col.find_one({'title': title})['text'][0].encode('utf8')

#    Returns a list of stories
def getStories():
     global col
     text = col.find()
     stories = []
     for line in text:
          story = line['title'].encode('utf8')
          stories.append(story)
     print stories
     return stories

#    Returns the text of a story
def getText(story):
     global col
     text = col.find_one({'title': story})['text']
     for line in text:
          print line
     return text

#    Adds a line to a story
def addLine(story, line):
     text = getText(story)
     text.append(line)
     print text
     col.update({'title': story}, {'text': text})
     
col.drop()
