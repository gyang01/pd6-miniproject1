from pymongo import *

global connection, db, res, collection

def connect():
     global connection, db, res, collection   
     
     connection = Connection('mongo.stuycs.org')
     db = connection.admin
     res = db.authenticate('ml7', 'ml7')
     db = connection['z-pd6']
     collection = db['sk']

#    New story
def addStory(title, line):    
     global collection
     collection.insert({'title': title, 'text': line})

#    Returns a list of stories
def getStories():
     global collection
     text = collection.find()
     stories = []
     for line in text:
          story = line['title'].encode('utf8')
          stories.append(story)
     print stories
     return stories

#    Returns the text of a story
def getText(story):
     global collection
     text = collection.find_one({'title': story})['text']
     return text

#    Adds a line to a story
def addLine(story, line):
     text = getText(story)
     text = text+'\n'+line
     collection.update({'title': story}, {'text': text})
     
connect()
addStory('Story1','Sam eats an apple.')
print 'STORY1:'
print getText('Story1')
addStory('Story2','The apple eats Sam.')
print 'STORY2:'
print getText('Story2')
addLine('Story2','He was delicious.')
getStories()
getText('Story1')
getText('Story2')
collection.drop()
