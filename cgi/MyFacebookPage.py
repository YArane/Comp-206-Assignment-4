#!/usr/bin/python
import cgi, cgitb

membersDBpath = "../databases/members.csv"
topicsDBpath = "../databases/topic.csv"

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
    if line1 in friends or line1 == username:
      retVal.append((line1, line2))
      postCount += 1
  return retVal

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
  posts = readFeed(username)
  members = retrieveUsernames()
  print "Content-type:text/html\r\n\r\n"
  print "<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>FEED</title>\n\t</head>\n\t<body>\n\n\t\t<center><h1>FEED</h1>\n\t\t<p><i>Logged in as: %s</i></p><br>\n\t\t<form action\"createNewPost.py\" method=post>\n\t\t\tNew post:<br>\n\t\t\t<input type=\"text\" name=\"post\">\n\t\t\t<input type=\"submit\" value=\"Submit\">\n\t\t</form><br><br>\n\t\t<p>" % (username)
  
  for post in posts:
    print "\t\t\t&emsp;&emsp;%s:&emsp;%s\n" % (post[0], post[1])

  print "\t\t</p></center>\n\t\t<p>User list:<br>\n\t\t\t"
  for member in members:
    print "\t\t\t&emsp;%s\n" % (member)

  print "\t\t<p>Don't have a social life? Want to follow people just like you? Add a user below:</p>\n\t\t<form action=\"addNewFriend.py\" method=post>\n\t\t\t&emsp;Username:<br>\n\t\t\t&emsp;<input type=\"text\" name=\"username\">\n\t\t\t<input type=\"submit\" value=\"Follow\">\n\t\t\t</fieldset>\n\t\t\t<br>\n\t\t</form>\n\t</body>\n</html>"

main()



















