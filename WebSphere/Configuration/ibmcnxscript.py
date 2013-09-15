# for better reuseability here i begin to put function
# 
# Author: Christoph Stoettner
# email: christoph.stoettner@stoeps.de

# Function to get the DataSource ID
# Used in cfgDataSource
def getDSId( dbName ):
    try:
        DSId = AdminConfig.getid( 'DataSource:' + dbName + '/' )
        return DSId
    except:
        print "Error when getting the DataSource ID!" 
        pass