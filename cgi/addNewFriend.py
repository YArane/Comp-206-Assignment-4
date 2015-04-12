#!/usr/bin/python
import cgi, cgitb 

membersDBpath = "../databases/members.csv"
topicsDBpath = "../databases/topic.csv"

# Returns an array containing the usernames of the registered users
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

# Returns true if the username passed is a registered user, otherwise false
def validateFriend(friendUsername):
    names = retrieveUsernames();
    for name in names:
        if name == friendUsername:
            return True
    return False

# Returns true if the dbEntry passed already contains the friendUsername string passed.
# Used to prevent adding the same friend multiple times
def checkIfAlreadyFriends(dbEntry, friendUsername):
    i = 3
    if len(dbEntry) <= 3:
        return False
    while i < len(dbEntry):
        if dbEntry[i] == friendUsername:
            return True
        i += 1
    return False

# Adds the a new friend to the database entry associated with the passed username
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

# Outputs html for the 'friend addition response', and executes add friend logic
def main():
    form = cgi.FieldStorage()
    username = form.getvalue('username')
    friendUsername = form.getvalue('friendUsername')
    addedFriend = addNewFriend(username, friendUsername)
    print "Content-type:text/html\r\n\r\n"
    print "<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>ADD FRIEND STATUS</title>\n\t</head>\n\t<body>\n"
    
    if addedFriend == True:
        print "\t\t<center><h1>FRIEND REQUEST SUCCESSFUL</h1>\n\t\t<p>You will now see posts from <i>%s</i>.</p>\n" % (friendUsername)
    else:
        print "\t\t<center><h1>FRIEND REQUEST UNSUCCESSFUL</h1>\n\t\t<p>User <i>%s</i> does not exist, or you are already friends with them.</p>\n" % (friendUsername)
    
    print "\t\t<form action=\"MyFacebookPage.py\" method=post>\n\t\t\t<input type=\"hidden\" name=\"username\" value=\"%s\">\n\t\t\t<input type=\"submit\" value=\"Back to feed\">\n\t\t</form></center>\n\t</body>\n</html>" % (username)
main()