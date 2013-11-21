# ibmcnxscript.py
#
# functions which are used in multiple scripts
# use them with "import ibmcnxscript"
# call function with ibmcnxscript.getDSId( db )
# 
# Author: Christoph Stoettner
# email: christoph.stoettner@stoeps.de

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

