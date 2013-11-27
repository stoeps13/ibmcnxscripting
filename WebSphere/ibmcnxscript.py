# ibmcnxscript.py
#
# functions which are used in multiple scripts
# use them with "import ibmcnxscript"
# call function with ibmcnxscript.getDSId( db )
#
# Author: Christoph Stoettner
# email: christoph.stoettner@stoeps.de

import os
# Function to get the DataSource ID
# Used in cfgDataSource
def getDSId( dbName ):
    try:
        DSId = AdminConfig.getid( '/DataSource:' + dbName + '/' )
        return DSId
    except:
        print "Error when getting the DataSource ID!"
        pass

# Function to synchronize all Nodes
def synchAllNodes():
    nodelist = AdminTask.listManagedNodes().splitlines()
    cell = AdminControl.getCell()
    for nodename in nodelist :
        print "Syncronizing node" + nodename
        repo = AdminControl.completeObjectName( 'type=ConfigRepository,process=nodeagent,node=' + nodename + ',*' )
        AdminControl.invoke( repo, 'refreshRepositoryEpoch' )
        sync = AdminControl.completeObjectName( 'cell=' + cell + ',node=' + nodename + ',type=NodeSync,*' )
        AdminControl.invoke( sync , 'sync' )
        print "----------------------------------------------------------------------------------------- "
        print "Full Resyncronization completed "
        print ""

# Function to check for a filepath and create it, when not present
def checkBackupPath( path ) :
     try :
         os.makedirs( path )
     except OSError :
         if not os.path.isdir( path ) :
             raise

# Function for Set Roles Script
def getAdmin( adminvar ):
    # function to ask for adminusers
    # return a list with admins
    # function is called for each admin type and each admin group type
    admins = []
    admin = ''
    adminstring = ''
    admindict = {
                 'connwasadmin':'Local WebSphere AdminUser',
                 'connadmin':'LDAP WebSphere and Connections AdminUser (searchAdmin)',
                 'connmoderators':'Moderator User',
                 'connmetrics':'Metrics Admin',
                 'connmobile':'Mobile Administrators',
                 'connadmingroup':'LDAP Admin Group',
                 'connmoderatorgroup':'Moderators Admin Group',
                 'connmetricsgroup':'Metrics Admin Group',
                 'connmobilegroup':'Mobile Admin Group'
    }
    print 'Type 0 when finished, uid is case sensitiv!'
    while admin != "0":
        admin = raw_input( 'Type uid for ' + admindict[adminvar] + ': ' )
        if admin != '0' and admin != '':
            admins.append( admin )
    adminstring = '|'.join( admins )
    return adminstring

# Set restricted j2ee roles
def j2eeRolesCmdRestricted( appName ):
    if( appName == 'Activities' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["everyone" Yes No "" ""] ["reader" Yes No "" ""] ["metrics-reader" No Yes "" ""] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["widget-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["bss-provisioning-admin" No No "" ""] ]]' )
    elif( appName == 'Blogs' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["everyone" Yes No "" ""] ["metrics-reader" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["global-moderator" No No "' + connwasadmin + '|' + connmoderators + '" "' + connmoderatorgroup + '"] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["widget-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["reader" No Yes "" ""] ["bss-provisioning-admin" No No "" ""]  ]]' )
    elif( appName == 'Common' ):
         AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["allAuthenticated" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["everyone" Yes No "" ""] ["metrics-report-run" No No "' + connmetrics + '" "' + connmetricsgroup + '"] ["global-moderator" No No "' + connmoderators + '" "' + connmoderatorgroup + '"] ["mail-user" No Yes "" ""] ["reader" Yes No "" ""]  ]]' )
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
        AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["everyone" Yes No "" ""] ["reader" Yes No "" ""] ["metrics-reader" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"]  ]]' )
    elif( appName == 'Metrics' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["everyone" Yes No "" ""] ["person" No Yes "" ""] ["reader" Yes No "" ""] ["everyone-authenticated" No Yes "" ""] ["community-metrics-run" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["metrics-report-run" No No "' + connmetrics + '" "' + connmetricsgroup + '"]  ]]' )
    elif( appName == 'Mobile' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["everyone" Yes No "" ""] ["reader" Yes No "" ""] ["person" No Yes "" ""]  ]]' )
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
        AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["allAuthenticated" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["everyone" Yes No "" ""] ["reader" Yes No "" ""] ["metrics-reader" No No "" ""] ["global-moderator" No No "' + connmoderators + '" "' + connmoderatorgroup + '"] ["mail-user" No Yes "" ""] ["trustedExternalApplication" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"]  ]]' )
    elif( appName == 'Wikis' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["everyone" Yes No "" ""] ["person" No Yes "" ""] ["reader" No Yes "" ""] ["metrics-reader" No Yes "" ""] ["everyone-authenticated" No Yes "" ""] ["wiki-creator" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["widget-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["bss-provisioning-admin" No No "" ""]  ]]' )
    elif( appName == 'connectionsProxy' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["allAuthenticated" No Yes "" ""] ["reader" Yes No "" ""] ["everyone" Yes No "" ""]  ]]' )
    else:
        print "Unknown Application: %s" % appName

# Set unrestricted j2ee roles
def j2eeRolesCmdUnrestricted( appName ):
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

# print DataSource Parameters
def showJdbcProviders():
    # Idea of this Function from https://webspherescript.wordpress.com
    # added some things
    providerEntries = AdminConfig.list( "JDBCProvider" ).splitlines()
    for provider in providerEntries:
        providerName = AdminConfig.showAttribute( provider, "name" )
        providerDescription = AdminConfig.showAttribute( provider, "description" )
        providerClasspath = AdminConfig.showAttribute( provider, "classpath" )
        providerImplementationClassName = AdminConfig.showAttribute( provider, "implementationClassName" )
        print "\t" + providerName
        print "Description: \t\t" + providerDescription
        print "Classpath: \t\t" + providerClasspath
        print "Class Name: \t\t" + providerImplementationClassName
        print  "\n"