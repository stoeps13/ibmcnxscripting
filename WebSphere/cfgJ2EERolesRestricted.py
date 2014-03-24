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
# 20131124  Christoph Stoettner     Update with loop and try/except to handle errors, added group support
# 20140324  Christoph Stoettner     Changed all reader roles to "All authenticated", Ajax proxy security is configured with this role!

import ibmcnxscript

# Variables for Usermapping
connwasadmin = str( ibmcnxscript.getAdmin( 'connwasadmin' ) )
connadmin = str( ibmcnxscript.getAdmin( 'connadmin' ) )
connmoderators = str( ibmcnxscript.getAdmin( 'connmoderators' ) )
connmetrics = str( ibmcnxscript.getAdmin( 'connmetrics' ) )
connmobile = str( ibmcnxscript.getAdmin( 'connmobile' ) )

# Variables for Groupmapping
connadmingroup = str( ibmcnxscript.getAdmin( 'connadmingroup' ) )
connmoderatorgroup = str( ibmcnxscript.getAdmin( 'connmoderatorgroup' ) )
connmetricsgroup = str( ibmcnxscript.getAdmin( 'connmetricsgroup' ) )
connmobilegroup = str( ibmcnxscript.getAdmin( 'connmobilegroup' ) )

# Set restricted j2ee roles
def j2eeRolesCmdRestricted( appName, connwasadmin, connadmin, connmoderators, connmetrics, connmobile, connadmingroup, connmoderatorgroup, connmetricsgroup, connmobilegroup ):
    if( appName == 'Activities' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["everyone" Yes No "" ""] ["reader" No Yes "" ""] ["metrics-reader" No Yes "" ""] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["widget-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["bss-provisioning-admin" No No "" ""] ]]' )
    elif( appName == 'Blogs' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["everyone" Yes No "" ""] ["metrics-reader" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["global-moderator" No No "' + connwasadmin + '|' + connmoderators + '" "' + connmoderatorgroup + '"] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["widget-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["reader" No Yes "" ""] ["bss-provisioning-admin" No No "" ""]  ]]' )
    elif( appName == 'Common' ):
         AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["allAuthenticated" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["everyone" Yes No "" ""] ["metrics-report-run" No No "' + connmetrics + '" "' + connmetricsgroup + '"] ["global-moderator" No No "' + connmoderators + '" "' + connmoderatorgroup + '"] ["mail-user" No Yes "" ""] ["reader" No Yes "" ""]  ]]' )
    elif( appName == 'Communities' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["everyone" Yes No "" ""] ["reader" No Yes "" ""] ["person" No Yes "" ""] ["metrics-reader" No Yes "" ""] ["community-creator" No Yes "" ""] ["community-metrics-run" No Yes "" ""] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["global-moderator" No No "' + connwasadmin + '|' + connmoderators + '" "' + connmoderatorgroup + '"] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["dsx-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["widget-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["bss-provisioning-admin" No No "" ""]  ]]' )
    elif( appName == 'Dogear' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["everyone" Yes No "" ""] ["reader" No Yes "" ""] ["metrics-reader" No Yes "" ""] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"]  ]]' )
    elif( appName == 'FNCS' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["Authenticated" No Yes "" ""] ["Anonymous" Yes No "" ""] ]]' )
    elif( appName == 'Files' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["everyone" Yes No "" ""] ["person" No Yes "" ""] ["reader" No Yes "" ""] ["metrics-reader" No Yes "" ""] ["everyone-authenticated" No Yes "" ""] ["files-owner" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["widget-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["app-connector" No No "" ""] ["global-moderator" No No "' + connwasadmin + '|' + connmoderators + '" "' + connmoderatorgroup + '"] ["org-admin" No No "' + connadmin + '" "' + connadmingroup + '"] ["bss-provisioning-admin" No No "" ""]  ]]' )
    elif( appName == 'Forums' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["metrics-reader" No Yes "" ""] ["reader" No Yes "" ""] ["everyone" Yes No "" ""] ["discussThis-user" Yes No "" ""] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["widget-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["global-moderator" No No "' + connwasadmin + '|' + connmoderators + '" "' + connmoderatorgroup + '"] ["bss-provisioning-admin" No No "" ""] ["search-public-admin" No No "" ""]  ]]' )
    elif( appName == 'Homepage' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["everyone" Yes No "" ""] ["reader" No Yes "" ""] ["metrics-reader" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"]  ]]' )
    elif( appName == 'Metrics' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["everyone" Yes No "" ""] ["person" No Yes "" ""] ["reader" No Yes "" ""] ["everyone-authenticated" No Yes "" ""] ["community-metrics-run" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["metrics-report-run" No No "' + connmetrics + '" "' + connmetricsgroup + '"]  ]]' )
    elif( appName == 'Mobile' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["everyone" Yes No "" ""] ["reader" No Yes "" ""] ["person" No Yes "" ""]  ]]' )
    elif( appName == 'Mobile Administration' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["administrator" No No "' + connmobile + '" "' + connmobilegroup + '"] ["everyone" No Yes "" ""]  ]]' )
    elif( appName == 'Moderation' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["reader" No Yes "" ""] ["everyone-authenticated" No Yes "" ""] ["person" No Yes "" ""] ["global-moderator" No No "' + connmoderators + '" "' + connmoderatorgroup + '"]  ]]' )
    elif( appName == 'News' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["everyone" Yes No "" ""] ["reader" No Yes "" ""] ["sharebox-reader" Yes No "" ""] ["metrics-reader" No Yes "" ""] ["allAuthenticated" Yes No "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["widget-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["bss-provisioning-admin" No No "" ""]  ]]' )
    elif( appName == 'Profiles' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["everyone" Yes No "" ""] ["reader" No Yes "" ""] ["person" No Yes "" ""] ["allAuthenticated" No Yes "" ""] ["metrics-reader" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["dsx-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["org-admin" No No ' + connadmin + ' ""] ["bss-provisioning-admin" No No "" ""]  ]]' )
    elif( appName == 'Search' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["everyone" Yes No "" ""] ["reader" No Yes "" ""] ["metrics-reader" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["everyone-authenticated" No Yes "" ""]  ]]' )
    elif( appName == 'WebSphereOauth20SP' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["authenticated" No Yes "" ""] ["client manager" No No "" ""]  ]]' )
    elif( appName == 'WidgetContainer' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["allAuthenticated" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["everyone" Yes No "" ""] ["reader" No Yes "" ""] ["metrics-reader" No No "" ""] ["global-moderator" No No "' + connmoderators + '" "' + connmoderatorgroup + '"] ["mail-user" No Yes "" ""] ["trustedExternalApplication" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"]  ]]' )
    elif( appName == 'Wikis' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["everyone" Yes No "" ""] ["person" No Yes "" ""] ["reader" No Yes "" ""] ["metrics-reader" No Yes "" ""] ["everyone-authenticated" No Yes "" ""] ["wiki-creator" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["widget-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["bss-provisioning-admin" No No "" ""]  ]]' )
    elif( appName == 'connectionsProxy' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["allAuthenticated" No Yes "" ""] ["reader" No Yes "" ""] ["everyone" Yes No "" ""]  ]]' )
    else:
        print "Unknown Application: %s" % appName


apps = AdminApp.list()
appsList = apps.split( lineSeparator )
for app in appsList:
    print "Setting Security Roles for %s" % app.upper()
    try:
        j2eeRolesCmdRestricted( app, connwasadmin, connadmin, connmoderators, connmetrics, connmobile, connadmingroup, connmoderatorgroup, connmetricsgroup, connmobilegroup )
    except:
        print "Error occured on setting security roles for %s" % app.upper()

AdminConfig.save()
