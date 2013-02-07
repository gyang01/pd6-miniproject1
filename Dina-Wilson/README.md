pd6-miniproject1
================

<h1>README:</h1>
<p>by Dina and Wilson</p>
<b>util.py</b>
--------------

<p>this will have the database stuff inside (using mongoDB)
methods:
<ul>
	<p>auth() -->authenticate the connection and make the collection/connect to the collection</p>
	<p>addStory(title) --->makes new story called title</p>
	<p>addLine(title, line) --->adds line to a story called title</p>
	<p>getStory(title) --->returns the story called title</p>
	<p>getAllStories() --->returns all stories</p>
	<p>getStoryLines(title) -----> returns the lines of the story</p>
	<p>getAllStoryLines() ---->returns all the lines of all stories</p>
+	add more to facilitate other functions 
</ul>
</p>

<b>web design stuff</b>
-----------------------

+	Put thluffy there
+	Have all the required buttons: Add story, Ok to read story, drop the stories...
+	Maybe add a special button: Scramble, which scrambles all the stories into 1, if there is more than 1 story
+	Drop down menu for the story selection	

<b> app.py </b>
---------------

+	Home page runs everything
+	Based on what button was pressed, and Get vs Post

