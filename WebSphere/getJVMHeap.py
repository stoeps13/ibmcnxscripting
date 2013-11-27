# getJVMHeap.py
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de
# Usage: wsadmin -f getJvmHeap.py

servers = AdminTask.listServers( '[-serverType APPLICATION_SERVER]' ).splitlines()

for server in servers:
    jvm = AdminConfig.list( 'JavaVirtualMachine', server )
    srv = server.split( '/' )
    cell = srv[1]
    node = srv[3]
    servername = srv[5].split( '|' )[0]
    print "%s - %s - %s" % ( cell, node, servername )
    print '\t initialHeapSize: ' + AdminConfig.showAttribute( jvm, 'initialHeapSize' )
    print '\t maximumHeapSize: ' + AdminConfig.showAttribute( jvm, 'maximumHeapSize' )
    print ' '
