Hon Wei Khor and Paul Ma Pd-6

DATABASE FUNCTION LIBRARY
------------
whoostory.py
------------
def addstory(name): #adds a story to the db if an exact same title isn't there already
def exists(name): #checks to see if a title already exists
def getstory(name): #gets the dictionary corresponding to a story
def getstorytext(name): #returns a list of strings corresponding to a story's lines, no unicode
def addline(name,line): #appends a line to the end of a currently existing story
def getalltitles(): #returns a list of story titles in db
