#!/usr/bin/python
import cgi, cgitb

membersDBpath = "../databases/members.csv"
topicsDBpath = "../databases/topic.csv"

# Returns an array containing the all the usernames of registered users
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

# Returns an array containing 10 or fewer posts from the friends associated to the
# passed username. If there are no posts, an empty array is returned
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

# Returns an array containing the usernames of the friends associated to the passed username
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

# Prints the list of existing users, latest posts, and the new friend/post creation forms
def main():
    form = cgi.FieldStorage()
    username = form.getvalue('username')
    posts = readFeed(username)
    members = retrieveUsernames()
    print "Content-type:text/html\r\n\r\n"
    print "<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>FEED</title>\n\t</head>\n\t<body bgcolor=\"#e2a483\">\n\n\t\t<center><h1>FEED</h1>\n\t\t<p><i>Logged in as: %s</i></p><br>\n\t\t<form action=\"createNewPost.py\" method=post>\n\t\t\t<input type=\"hidden\" name=\"username\" value=\"%s\">\n\t\t\tNew post:<br>\n\t\t\t<input type=\"text\" name=\"postData\">\n\t\t\t<input type=\"submit\" value=\"Post\">\n\t\t</form></center><br><br>\n\t\t" % (username, username)
    
    for post in posts:
        print "\t\t\t<p>&emsp;<b>%s: </b><i>%s</i></p>" % (post[0], post[1])

    print "\t\t<br></p>\n\t\t<h3>User list:</h3>\n\t\t\t<ul>\n\t\t\t\t"
    for member in members:
        print "\t\t\t\t<li>%s</li>" % (member)

    print "\t\t\t</ul><br><br>\n\t\t<form action=\"addNewFriend.py\" method=post>\n\t\t\t<input type=\"hidden\" name=\"username\" value=\"%s\">\n\t\t\t<fieldset><h3>Don't have a social life? Want to follow people just like you? Add a user below:</h3>\n\t\t\t&emsp;Username:<br>\n\t\t\t&emsp;<input type=\"text\" name=\"friendUsername\">\n\t\t\t<input type=\"submit\" value=\"Follow\"><br>\n\t\t\t</fieldset>\n\t\t\t<br>\n\t\t</form>\n\t<p><i><a href=\"../index.html\">Logout</a></i></p>\n\t</body>\n</html>" % (username)

main()
