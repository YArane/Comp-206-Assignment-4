#!/usr/bin/python
import cgi, cgitb 

def main():
  form = cgi.FieldStorage()
  username = form.getvalue('username')
  print "Content-type:text/html\r\n\r\n"
  print '<html>'
  print '<head>'
  print "<title>Hey there %s! Welcome to your feed</title>" % (username)
  print '</head>'
  print '<body>'
  print '</body>'
  print '</html>'

main()