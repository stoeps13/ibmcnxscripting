# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de
# Blog: http://www.stoeps.de

runDB = []
errorDB = []
notInstDB = []

dbs = ['FNOS', 'FNGCD', 'IBM_FORMS_DATA_SOURCE', 'activities', 'blogs', 'communities', 'dogear', 'files', 'forum', 'homepage', 'metrics', 'mobile', 'news', 'oauth provider', 'profiles', 'search', 'wikis']    # List of all databases to check

for db in dbs:    # loop through databases
    ds = AdminConfig.getid( '/DataSource:' + db + '/' )
    try:
        checkDS = AdminControl.testConnection( ds )
        if checkDS == "WASX7217I: Connection to provided datasource was successful." :
            # print 'Connect to %s was successful' % db
            runDB.append( db )
        else :
            errorDB.append( db )
            # print 'Error: %s is not available' % db
    except:
        notInstDB.append( db )


runDB.sort()
errorDB.sort()
notInstDB.sort()

print ''
print '\tConnection to DataSource successful: \n'
try:
    for db in runDB:
        print '\t\t' + db
except:
    print '\t\tNo running DB'

print ''
print '\tDB not installed: \n'
try:
    for db in notInstDB:
        print'\t\t' + DB
except:
    print '\t\tAll DB checked'

print ''
print '\tERROR connecting to: \n'
try:
    for db in errorDB:
        print '\t\t' + db
except:
    print '\t\tAll DB running\n'
print ''

