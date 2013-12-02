# menu-cnx.py
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de
# Blog: http://www.stoeps.de

dbs = ['FNOS', 'FNGCD', 'activities', 'blogs', 'communities', 'dogear', 'files', 'forum', 'homepage', 'metrics', 'mobile', 'news', 'oauth provider', 'profiles', 'search', 'wikis']    # List of all databases to check
for db in dbs:    # loop through databases
    ds = AdminConfig.getid( '/DataSource:' + db + '/' )
    try:
        checkDS = AdminControl.testConnection( ds )
        if checkDS == "WASX7217I: Connection to provided datasource was successful." :
            print 'Connect to %s was successful' % db
        else :
            print 'Error: %s is not available' % db
    except:
        print 'Error: %s is not installed.'



