#!/usr/bin/python

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
  return userData

def readFeed():
  fo = open(topicsDBpath, "r")
  postCount = 0;
  retVal = []
  while postCount < 10:
    line1 = fo.readline().rstrip()
    line2 = fo.readline().rstrip()
    if not line2: break  # EOF
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

def isAFriend(dbEntry, friendUsername):
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
  
  fo = open(membersDBpath, "r")
  foText = fo.readlines()
  fo.seek(0,0)
  lineNum = 0;
  splitted = []
  while True:
    line = fo.readline().rstrip()
    if not line: break  # EOF
    splitted = line.split()
    if splitted[1] == username and not isAFriend(splitted, friendUsername):
      foText[lineNum] = foText[lineNum].rstrip() + " " + friendUsername +"\n" 
      break;
    lineNum += 1
  fo.close;

  with open(membersDBpath, 'w') as fo:
    fo.writelines( foText )

#x = retrieveUsernames()
#y = readFeed()
#print x
#print y
#addNewPost("yarden", "brett is my friend")
addNewFriend("tt", "dan")


















