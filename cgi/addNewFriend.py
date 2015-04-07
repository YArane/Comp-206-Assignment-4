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

def addNewFriend(username, friendUsername):
  if not validateFriend(friendUsername):
    return False
  
  addedFriend = False
  fo = open(membersDBpath, "r+")
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
      addedFriend = True
      break;
    lineNum += 1
  fo.close();
  
  with open(membersDBpath, 'w') as fo:
  	fo.writelines(foText)
  return addedFriend;

def main():
  form = cgi.FieldStorage()
  username = form.getvalue('username')
  friendUsername = form.getvalue('friendUsername')
  addedFriend = addNewFriend(username, friendUsername)
  print "Content-type:text/html\r\n\r\n"
  print '<html>'
  print '<head>'
  print "<title>Friend request result</title>"
  print '</head>'
  print '<body>'
  if addedFriend == True:
    print "<p>You are now friends with %s</p>" % (friendUsername)
  else:
    print "<p>%s was not added to your friend list. You are already friends or he/she does not exist.</p>" % (friendUsername)
  print "<form action=\"MyFacebookPage.py\" method=post><fieldset><input type=\"hidden\" name=\"username\" value=\"%s\"><br><br><input type=\"submit\" value=\"Go to Feed Page\"></fieldset></form>" % (username)
  print '</body>'
  print '</html>'

main()



























