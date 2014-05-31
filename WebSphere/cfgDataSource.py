# cfgDataSource.py
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de
#
# History:
# 20131230 stoeps Added Performance Tuning Addendum Parameters

# Import general functions from ibmcnxscript.py
import ibmcnxscript

# Recommandation for CCM?
# without tests i would set analog to files!

perf = {'activities':{'minConnections':1, 'maxConnections':50},
        'blogs':{'minConnections':1, 'maxConnections':250},
        'communities':{'minConnections':10, 'maxConnections':200},
        'dogear':{'minConnections':1, 'maxConnections':150},
        'files':{'minConnections':10, 'maxConnections':100},
        'FNOSDS':{'minConnections':75, 'maxConnections':200},
        'FNOSDSXA':{'minConnections':25, 'maxConnections':75},
        'forum':{'minConnections':50, 'maxConnections':100},
        'homepage':{'minConnections':20, 'maxConnections':100},
        'metrics':{'minConnections':1, 'maxConnections':75},
        'mobile':{'minConnections':1, 'maxConnections':100},
        'news':{'minConnections':50, 'maxConnections':75},
        'profiles':{'minConnections':1, 'maxConnections':100},
        'search':{'minConnections':50, 'maxConnections':75},
        'wikis':{'minConnections':1, 'maxConnections':100}}

statementCacheSize = 100    # change to 50 for oracle

print 'DataSource Parameters will be set to: '
print 'Database \t statementCacheSize \t minConnections \t maxConnections'
for db in perf.keys():
    print db.upper(),
    if len( db ) < 7:
        print '\t',
    print '\t\t' + str( statementCacheSize ),
    print '\t\t\t' + str( perf[db]['minConnections'] ),
    print '\t\t\t' + str( perf[db]['maxConnections'] )

answer = raw_input( 'Are you sure, that your parameters should be overwritten? (Yes|No) ' )
allowed_answer = ['yes', 'y', 'ja', 'j']

if answer.lower() in allowed_answer:
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
else:
    print '\t\tNothing changed! '
