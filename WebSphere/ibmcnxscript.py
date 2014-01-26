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
    print adminstring
    return adminstring

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

