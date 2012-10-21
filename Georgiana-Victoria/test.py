from pymongo import Connection
import db

add_story('Example', 'a')


res = stories.find()
for line in res:
    print line
