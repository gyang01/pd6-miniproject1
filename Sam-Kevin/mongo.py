from pymongo import *

connection = Connection('mongo.stuycs.org')

def connect():
     db = connection.admin
     res = db.authenticate('ml7', 'ml7')

#    New story
def addStory(title):    
     db = connection['z-pd6']
     stories = db.first_collection
     story = {'title':title, 'text':['']}
     stories.insert(story)

#    Returns a list of stories
def getStories():
     db = connection['z-pd6']
     stories = db.first_collection
     titles = [story['title'] for story in stories.find()]
     return titles

#    Returns the text of a story
def getText(title):
     db = connection['z-pd6']
     stories = db.first_collection
     for line in stories.find():
          if line['title']==title:
               return line['text']

#    Adds a line to a story
def addLine(title, text):
     db = connection['z-pd6']
     stories = db.first_collection
     for line in stories.find():
          if line['title']==title:
               story = line['text']
               story.append(text)
               stories.update({'title':title},{'title':title, 'text':story})
