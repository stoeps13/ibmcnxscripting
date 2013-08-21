# Script to sychronise User data from LDAP to application
# Call the script through wsadmin.sh|bat and give a mailaddress as script parameter
#
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de
#
# example: wsadmin.sh -lang jython -f updateUserByEmail.py mailaddress newloginID
#


MAILADDRESS = sys.argv[0]
LOGINID = sys.argv[1]

print "Updating User: " + MAILADDRESS

# Loading Connections Administration Commands
execfile("profilesAdmin.py")

ProfilesService.updateUser(MAILADDRESS, loginId=LOGINID)

ProfilesService.publishUserData(MAILADDRESS)
