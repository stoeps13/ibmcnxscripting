# Create a Forums Post in IBM Connections

# Import Libs
from cookielib import LWPCookieJar
from urllib import urlencode, quote
import urllib2
import string
from xml.dom import minidom

# Set basic variables
SERVER_NAME = 'connect.stoeps.local'
USER_NAME = 'aconnections'
PASSWORD = 'password'

# Log in to IBM Connections
## Create authenticated server opener
cookieProcessor = urllib2.HTTPCookieProcessor(LWPCookieJar())
opener = urllib2.build_opener(cookieProcessor)

## encoded parameters sent in a POST method
encodedForm = urlencode({ "j_username" : USER_NAME, "j_password" : PASSWORD})

urlform = "https://" + SERVER_NAME + "/forums/j_security_check"
request = urllib2.Request(urlform, encodedForm)
opener.addheaders = [("User-agent","Mozilla/5.0")]

## Read the response from server
loggedIn = opener.open(request).read()
print loggedIn
