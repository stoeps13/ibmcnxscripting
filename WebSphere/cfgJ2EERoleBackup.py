# securityRoleBackup.py
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de
#
# do not forget to place ibmcnxscript to the local folder,
# where you placed this script

import sys
# import errno
import ibmcnxscript

path = raw_input( "Please provide a path for your backup files: " )
ibmcnxscript.checkBackupPath( path )

apps = AdminApp.list()
appsList = apps.split( lineSeparator )
for app in appsList:
    filename = path + "/" + app + ".txt"
    print "Backup of %s security roles saved." % app.upper()
    my_file = open( filename, 'w' )
    my_file.write ( AdminApp.view( app, "-MapRolesToUsers" ) )
    my_file.flush
    my_file.close()

