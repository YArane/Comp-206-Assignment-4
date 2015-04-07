#!/usr/bin/python
import cgi, cgitb 

membersDBpath = "../databases/members.csv"
topicsDBpath = "../databases/topic.csv"

def line_prepender(line):
    with open(topicsDBpath, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

def retrieveUsernames():
  fo = open(membersDBpath, "r")
  userData = []
  splitted = []
  for line in fo:
    splitted = line.split()
    if len(splitted) > 0:
      userData.append(splitted[1]) 
  fo.close()
  return userData

def readFeed(username):
  fo = open(topicsDBpath, "r")
  postCount = 0;
  retVal = []
  friends = getFriends(username)
  while postCount < 10:
    line1 = fo.readline().rstrip()
    line2 = fo.readline().rstrip()
    if not line2: break  # EOF
    if line1 in friends:
      retVal.append((line1, line2))
      postCount += 1
  return retVal

def addNewPost(username, postData):
  line_prepender(postData)
  line_prepender(username)

def getFriends(username):
  fo = open(membersDBpath, "r")
  splitted = []
  friends = []
  for line in fo:
    splitted = line.split()
    if splitted[1] == username:
      for i in range(3, len(splitted)):
        friends.append(splitted[i])
  return friends

def main():
  form = cgi.FieldStorage()
  username = form.getvalue('username')
  #username = "maca"
  posts = readFeed(username)
  members = retrieveUsernames()
  print "Content-type:text/html\r\n\r\n"
  print '<html>'
  print '<head>'
  print "<title>Hey there %s! Welcome to your feed</title>" % (username)
  print '</head>'
  print '<body>'
  print "<p> USER: %s </p>" % (username)
  for post in posts:
    print "<p>%s posted -> %s</p>" % (post[0], post[1])
  print "<p>The existing members are the following:</p>"
  for member in members:
    print "<p>%s</p>" % (member)
  print "<form action=\"addNewFriend.py\" method=post><fieldset><input type=\"hidden\" name=\"username\" value=\"%s\"><br><br>Add new Friend:<br><input type=\"text\" name=\"friendUsername\"><br><br><input type=\"submit\" value=\"Add Friend\"></fieldset></form>" % (username)
  print "<a href=\"../index.html\">Logout</a>"
  print '</body>'
  print '</html>'

main()



















