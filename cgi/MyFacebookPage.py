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

def validateFriend(friendUsername):
  names = retrieveUsernames();
  for name in names:
    if name == friendUsername:
      return True
  return False

def checkIfAlreadyFriends(dbEntry, friendUsername):
  i = 3
  if len(dbEntry) <= 3:
    return False
  while i < len(dbEntry):
    if dbEntry[i] == friendUsername:
      return True
    i += 1
  return False

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


def addNewFriend(username, friendUsername):
  if not validateFriend(friendUsername):
    return False
  
  fo = open(membersDBpath, "r")
  foText = fo.readlines()
  fo.seek(0,0)
  lineNum = 0;
  splitted = []
  while True:
    line = fo.readline().rstrip()
    if not line: break  # EOF
    splitted = line.split()
    if splitted[1] == username and not checkIfAlreadyFriends(splitted, friendUsername):
      foText[lineNum] = foText[lineNum].rstrip() + " " + friendUsername +"\n" 
      break;
    lineNum += 1
  fo.close();

  with open(membersDBpath, 'w') as fo:
    fo.writelines( foText )

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
  print "<a href=\"../index.html\">Logout</a>"
  print '</body>'
  print '</html>'

#x = retrieveUsernames()
#y = readFeed()
#print x
#print y
#addNewPost("yarden", "brett is my friend")
#addNewFriend("tt", "dan")
#getFriends("tt")
#x = readFeed("maca");
#print x
#y = retrieveUsernames()
#print y
#addNewFriend("ale", "maca")

main()



















