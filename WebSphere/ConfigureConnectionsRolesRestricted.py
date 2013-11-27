# ConfigureConnectionsRolesRestricted
#
# Author: Klaus Bild
# Blog: http://www.kbild.ch
# E-Mail:
#
# Description:
# Script is tested with IBM Connections 4.5 CR2
# You have to edit the variables and set them to your administrative Accounts

# History:
# 20131124  Christoph Stoettner     Update with loop and try/except to handle errors, added group support

import ibmcnxscript

# Variables for Usermapping
connwasadmin = ibmcnxscript.getAdmin( 'connwasadmin' )
connadmin = ibmcnxscript.getAdmin( 'connadmin' )
connmoderators = ibmcnxscript.getAdmin( 'connmoderators' )
connmetrics = ibmcnxscript.getAdmin( 'connmetrics' )
connmobile = ibmcnxscript.getAdmin( 'connmobile' )

# Variables for Groupmapping
connadmingroup = ibmcnxscript.getAdmin( 'connadmingroup' )
connmoderatorgroup = ibmcnxscript.getAdmin( 'connmoderatorgroup' )
connmetricsgroup = ibmcnxscript.getAdmin( 'connmetricsgroup' )
connmobilegroup = ibmcnxscript.getAdmin( 'connmobilegroup' )

apps = AdminApp.list()
appsList = apps.split( lineSeparator )
for app in appsList:
    print "Setting Security Roles for %s" % app.upper()
    try:
        ibmcnxscript.j2eeRolesCmdRestricted( app )
    except:
        print "Error occured on setting security roles for %s" % app.upper()

AdminConfig.save()