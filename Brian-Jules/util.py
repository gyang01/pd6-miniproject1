from pymongo import Connection

class DatabaseConnection(object):

    def __init__(self):
        self.db = self.get_db()

    def get_db():
        connection = Connection("mongo.stuycs.org")
        admin = connection.admin
        admin.authenticate("ml7", "ml7")
        return connection["JulesBrian"]

    def add_story(self):
        pass

    def add_line(self, story):
        pass
