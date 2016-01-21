#!/usr/bin/env python

import os,json,cgi

print "Content-type: text/html"
print
print "<HTML><H1>Yo</H1><BODY><P>Hello World!<P>"
print "<FORM method = 'POST'><INPUT name = 'x'></form>"
#print json.dumps(dict(os.environ), indent = 4)

form = cgi.FieldStorage()
 
print "<P> X was: " + cgi.escape(str(form.getvalue('x')))
print "<P></Body></HTML>"


