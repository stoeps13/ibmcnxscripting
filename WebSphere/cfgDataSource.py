# cfgDataSource.py
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de

# Import general functions from ibmcnxscript.py
import ibmcnxscript

# Recommandation for CCM?
# without tests i would set analog to files!

perf = {'activities':{'minConnections':1, 'maxConnections':50},
        'blogs':{'minConnections':1, 'maxConnections':250},
        'communities':{'minConnections':10, 'maxConnections':200},
        'dogear':{'minConnections':1, 'maxConnections':150},
        'files':{'minConnections':10, 'maxConnections':100},
        'fnos':{'minConnections':10, 'maxConnections':100},
        'fngcd':{'minConnections':10, 'maxConnections':100},
        'forum':{'minConnections':50, 'maxConnections':100},
        'homepage':{'minConnections':20, 'maxConnections':100},
        'metrics':{'minConnections':1, 'maxConnections':75},
        'mobile':{'minConnections':1, 'maxConnections':100},
        'news':{'minConnections':50, 'maxConnections':75},
        'profiles':{'minConnections':1, 'maxConnections':100},
        'search':{'minConnections':50, 'maxConnections':75},
        'wikis':{'minConnections':1, 'maxConnections':100}}

statementCacheSize = 100    # change to 50 for oracle

for db in perf.keys():    # Looping through databases
    print 'Change DataSource parameters for: %s' % db.upper()
    try:
        t1 = ibmcnxscript.getDSId( db )
        print '\t\tstatementCacheSize: \t' + str( statementCacheSize )
        print '\t\tminConnections: \t' + str( perf[db]['minConnections'] )
        print '\t\tmaxConnections: \t' + str( perf[db]['maxConnections'] )
        AdminConfig.modify( t1, '[[statementCacheSize "' + str( statementCacheSize ) + '"]]' )
        AdminConfig.modify( t1, '[[connectionPool [[minConnections "' + str( perf[db]['minConnections'] ) + '"][maxConnections "' + str( perf[db]['maxConnections'] ) + '"]]]]' )
        AdminConfig.save()
        print 'Parameter for %s successfully set!' % db.upper()
    except:
        print '\tError can\'t set Performance parameter for' + db.upper() + '!'
