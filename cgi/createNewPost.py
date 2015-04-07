#!/usr/bin/python
import cgi, cgitb 

membersDBpath = "../databases/members.csv"
topicsDBpath = "../databases/topic.csv"

def line_prepender(line):
    with open(topicsDBpath, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

def addNewPost(username, postData):
  line_prepender(postData)
  line_prepender(username)

def main():
  form = cgi.FieldStorage()
  username = form.getvalue('username')
  postData = form.getValue('postData')
  addNewPost(username, postData)
  print "Content-type:text/html\r\n\r\n"
  print '<html>'
  print '<head>'
  print "<title>Post submission result</title>"
  print '</head>'
  print '<body>'
  print "<p>Your post was created successfully.</p>"
  print "<form action=\"MyFacebookPage.py\" method=post><fieldset><input type=\"hidden\" name=\"username\" value=\"%s\"><br><br><input type=\"submit\" value=\"Go to Feed Page\"></fieldset></form>" % (username)
  print '</body>'
  print '</html>'
