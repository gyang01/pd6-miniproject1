# Mini project 1 plan

Sarah Robinson and Jasmine Li

## util.py explanation

Util controls all of the database-related functions, aka the mongodb stuff.

+    auth() connects to the admin database and logs in
+    start() is kinda useless but calls auth() and could also initiate stuff
+    add_story(str) takes a string as an input and adds a new story to the database
+    get_story(str) takes a story title and, if it exists, returns a list of the lines in the story
+    add_line(str,str) takes a story title and a new line and adds the line to the story specified
+    del_story(str) deletes all stories with the specified title
+    get_story_titles() returns a list of unique story titles (it checks for repeats)

## web page plan

(nothing here yet)