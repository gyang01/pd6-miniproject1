import pymongo

import mongo.py

def test():
	auth()
	addStory("Izzi Pays Adam 100 Dollars")
	addLine("Once upon a time, Izzi paid Adam 100 dollars.")
	print db.find()

	