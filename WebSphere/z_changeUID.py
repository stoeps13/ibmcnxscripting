'''
  Script to change the UID of Users

  Author: Christoph Stoettner
  E-Mail: christoph.stoettner@stoeps.de

  example: wsadmin.sh -lang jython -f changeUID.py user.csv

  Format of CSV-File:
  uid;mailaddress
  don't mask strings with "

  This script can be used when switching LDAP servers within Connections and
  no equal values to hash are present. Please be very careful and know what
  you do!
'''

import sys
import os

# Check OS on windows .strip('\n') is not required

# Import Connections Admin Commands for Profiles
execfile( "profilesAdmin.py" )
print "\nReading from file: " + sys.argv[0]

myfile = open( sys.argv[0], 'r' )
for line in myfile.readlines():
    if( ";" in line ) :
        data = line.split( ";" )

    print "Working on user " + data[1]
    email = data[1].strip()
    uid = data[0].strip()
    ProfilesService.updateUser( str( email ), uid = str( uid ) )
    ProfilesService.publishUserData( email )

print '\nDONE \n'
