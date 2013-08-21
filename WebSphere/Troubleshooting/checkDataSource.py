dbs = ['activities','blogs','communities','dogear','files','forum','homepage','metrics','mobile','news','oauth provider','profiles','search','wikis'] #List of all databases to check
for db in dbs: #loop through databases
    ds = AdminConfig.getid('/DataSource:' + db + '/')
    print "Check database %s" % db,
    print AdminControl.testConnection(ds)
