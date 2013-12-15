# Script to sychronise User data from LDAP to application
# Call the script through wsadmin.sh|bat and give a mailaddress as script parameter
#
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de
#
# example: wsadmin.sh -lang jython -f memberSyncByEmail.py cstoettner@fum.de
#
# Update 20131114 CST     Check function, i think there is a problem, when uid is not set within the deactived user


MAILADDRESS = sys.argv[0]
print "Activating User: " + MAILADDRESS

# Loading Connections Administration Commands
execfile( "profilesAdmin.py" )

ProfilesService.activateUserByUserId( MAILADDRESS )
ProfilesService.publishUserData( MAILADDRESS )

