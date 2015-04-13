#!/usr/bin/python
import cgi, cgitb 

membersDBpath = "../databases/members.csv"
topicsDBpath = "../databases/topic.csv"

# Apepend the passed string to the beginning of the topics database
# This way we shift the old posts down the database
def line_prepender(line):
    with open(topicsDBpath, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

# Adds the user name and post information passed to the topics DB
def addNewPost(username, postData):
    line_prepender(postData)
    line_prepender(username)

# Executes post addition logic and prints the html for 'new post response'
def main():
    form = cgi.FieldStorage()
    username = form.getvalue('username')
    postData = form.getvalue('postData')
    addNewPost(username, postData)
    print "Content-type:text/html\r\n\r\n"
    print "<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>POST STATUS</title>\n\t</head>\n\t<body bgcolor=\"#e2a483\">\n\t\t<center><h1>POST CREATED SUCCESSFULLY</h1>\n\t\t<p>Your post below was successfully created:<br>\n\t\t\t<i>%s</i></p>\n\t\t<form action=\"MyFacebookPage.py\" method=post>\n\t\t\t<input type=\"hidden\" name=\"username\" value=\"%s\">\n\t\t\t<input type=\"submit\" value=\"Back to feed\">\n\t\t</form></center>\n\t</body>\n</html>" % (postData, username)
main()