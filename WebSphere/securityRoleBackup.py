# securityRoleBackup.py
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de
import os
# path='/home/cstoettner/Dropbox/Devel/ibmcnxscripting/temp'
path = sys.argv[0]
if path == '':
    path = '../temp/j2eebackup'    # path where Backup is stored
    print "Setting path to %s!" % path
else :
    print "%s is used to store the backup!" % path

if not os.path.exists( path ):
    print "Path does not exist, script creates it!"
    os.makedirs( path )

apps = AdminApp.list()
appsList = apps.split( lineSeparator )
for app in appsList:
    filename = path + "/" + app + ".txt"
    print "Backup of %s security roles saved." % app.upper()
    my_file = open( filename, 'w' )
    my_file.write ( AdminApp.view( app, "-MapRolesToUsers" ) )
    my_file.flush
    my_file.close()

