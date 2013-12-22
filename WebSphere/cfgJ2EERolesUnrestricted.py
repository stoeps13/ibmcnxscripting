# cfgJ2EERolesRestricted
#
# Author: Klaus Bild
# Blog: http://www.kbild.ch
# E-Mail:
#
# Description:
# Script is tested with IBM Connections 4.5 CR2
# You have to edit the variables and set them to your administrative Accounts

# History:
# 20131124  Christoph Stoettner    Update with loop and try/except to handle errors, added group support
# 20131201  Christoph Stoettner    Add menu to ask for parameters

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

def j2eeRolesCmdUnrestricted( appName, connwasadmin, connadmin, connmoderators, connmetrics, connmobile, connadmingroup, connmoderatorgroup, connmetricsgroup, connmobilegroup ):
    if( appName == 'Activities' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["everyone" Yes No "" ""] ["reader" Yes No "" ""] ["metrics-reader" Yes No "" ""] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["widget-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["bss-provisioning-admin" No No "" ""] ]]' )
    elif( appName == 'Blogs' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["everyone" Yes No "" ""] ["metrics-reader" Yes No "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["global-moderator" No No "' + connwasadmin + '|' + connmoderators + '" ""] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["widget-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["reader" Yes No "" ""] ["bss-provisioning-admin" No No "" ""]  ]]' )
    elif( appName == 'Common' ):
         AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["allAuthenticated" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["everyone" Yes No "" ""] ["metrics-report-run" No No ' + connmetrics + ' ""] ["global-moderator" No No "' + connmoderators + '" "' + connmoderatorgroup + '"] ["mail-user" No Yes "" ""] ["reader" Yes No "" ""]  ]]' )
    elif( appName == 'Communities' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["everyone" Yes No "" ""] ["reader" Yes No "" ""] ["person" No Yes "" ""] ["metrics-reader" Yes No "" ""] ["community-creator" Yes No "" ""] ["community-metrics-run" No Yes ' + connmetrics + ' ""] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["global-moderator" No No "' + connwasadmin + '|' + connmoderators + '" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["dsx-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["widget-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["bss-provisioning-admin" No No "" ""]  ]]' )
    elif( appName == 'Dogear' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["everyone" Yes No "" ""] ["reader" Yes No "" ""] ["metrics-reader" Yes No "" ""] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"]  ]]' )
    elif( appName == 'FNCS' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["Authenticated" Yes No "" ""] ["Anonymous" Yes No "" ""] ]]' )
    elif( appName == 'Files' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["everyone" Yes No "" ""] ["person" No Yes "" ""] ["reader" Yes No "" ""] ["metrics-reader" Yes No "" ""] ["everyone-authenticated" No Yes "" ""] ["files-owner" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["widget-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["app-connector" No No "" ""] ["global-moderator" No No "' + connwasadmin + '|' + connmoderators + '" ""] ["org-admin" No No "" ""] ["bss-provisioning-admin" No No "" ""]  ]]' )
    elif( appName == 'Forums' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["metrics-reader" Yes No "" ""] ["reader" Yes No "" ""] ["everyone" Yes No "" ""] ["discussThis-user" Yes No "" ""] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["widget-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["global-moderator" No No "' + connwasadmin + '|' + connmoderators + '" ""] ["bss-provisioning-admin" No No "" ""] ["search-public-admin" No No "" ""]  ]]' )
    elif( appName == 'Homepage' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["everyone" Yes No "" ""] ["reader" Yes No "" ""] ["metrics-reader" Yes No "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"]  ]]' )
    elif( appName == 'Metrics' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["everyone" Yes No "" ""] ["person" No Yes "" ""] ["reader" Yes No "" ""] ["everyone-authenticated" No Yes "" ""] ["community-metrics-run" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["metrics-report-run" No No ' + connmetrics + ' ""]  ]]' )
    elif( appName == 'Mobile' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["everyone" Yes No "" ""] ["reader" Yes No "" ""] ["person" No Yes "" ""]  ]]' )
    elif( appName == 'Mobile Administration' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["administrator" No No "' + connmobile + '" "' + connmobilegroup + '"] ["everyone" No Yes "" ""]  ]]' )
    elif( appName == 'Moderation' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["reader" Yes No "" ""] ["everyone-authenticated" No Yes "" ""] ["person" No Yes "" ""] ["global-moderator" No No "' + connmoderators + '" "' + connmoderatorgroup + '"]  ]]' )
    elif( appName == 'News' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["everyone" Yes No "" ""] ["reader" Yes No "" ""] ["sharebox-reader" Yes No "" ""] ["metrics-reader" Yes No "" ""] ["allAuthenticated" Yes No "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["widget-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["bss-provisioning-admin" No No "" ""]  ]]' )
    elif( appName == 'Profiles' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["everyone" Yes No "" ""] ["reader" Yes No "" ""] ["person" No Yes "" ""] ["allAuthenticated" No Yes "" ""] ["metrics-reader" Yes No "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["dsx-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["org-admin" No No "' + connadmin + '" "' + connadmingroup + '"] ["bss-provisioning-admin" No No "" ""]  ]]' )
    elif( appName == 'Search' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["everyone" Yes No "" ""] ["reader" Yes No "" ""] ["metrics-reader" Yes No "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["everyone-authenticated" No Yes "" ""]  ]]' )
    elif( appName == 'WebSphereOauth20SP' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["authenticated" No Yes "" ""] ["client manager" No No "" ""]  ]]' )
    elif( appName == 'WidgetContainer' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["allAuthenticated" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["everyone" Yes No "" ""] ["reader" Yes No "" ""] ["metrics-reader" No No "" ""] ["global-moderator" No No "' + connmoderators + '" "' + connmoderatorgroup + '"] ["mail-user" No Yes "" ""] ["trustedExternalApplication" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"]  ]]' )
    elif( appName == 'Wikis' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["everyone" Yes No "" ""] ["person" No Yes "" ""] ["reader" Yes No "" ""] ["metrics-reader" Yes No "" ""] ["everyone-authenticated" No Yes "" ""] ["wiki-creator" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["widget-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["bss-provisioning-admin" No No "" ""]  ]]' )
    elif( appName == 'connectionsProxy' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["allAuthenticated" No Yes "" ""] ["reader" Yes No "" ""] ["everyone" Yes No "" ""]  ]]' )
    else:
        print "Unknown Application: %s" % appName


apps = AdminApp.list()
appsList = apps.split( lineSeparator )
for app in appsList:
    print "Setting Security Roles for %s" % app.upper()
    try:
        j2eeRolesCmdUnrestricted( app, connwasadmin, connadmin, connmoderators, connmetrics, connmobile, connadmingroup, connmoderatorgroup, connmetricsgroup, connmobilegroup )
    except:
        print "Error occured on setting security roles for %s" % app.upper()

AdminConfig.save()