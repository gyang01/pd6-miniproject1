from pymongo import Connection

class DatabaseConnection(object):

    def __init__(self):
        self.db = self.get_db()
        self.stories = self.db["Stories"]

    def get_db(self):
        connection = Connection("mongo.stuycs.org")
        admin = connection.admin
        admin.authenticate("ml7", "ml7")
        return connection["JulesBrian"]

    def drop_stories(self):
        self.db.drop_collection("Stories")

    def add_story(self, name):
        if not self.stories.find({"name" : name}).count():
            self.stories.insert({"name" : name, "body" : []})

    def add_line(self, name, line):
        self.stories = self.db["Stories"]
        self.stories.update({"name" : name}, {"$push": {"body" : line}})
   
    def get_stories(self):
        return [story["name"] for story in self.stories.find()]

    def get_lines(self, name):
        self.stories = self.db["Stories"]
        return self.stories.find_one({"name" : name})["body"]


if __name__ == "__main__":
    db = DatabaseConnection()
    db.drop_stories()
