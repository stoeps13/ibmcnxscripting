# getJVMHeap.py
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de
# Usage: wsadmin -f getJvmHeap.py

# Get a list of all servers in WAS cell (dmgr, nodeagents, AppServer, webserver)
servers = AdminTask.listServers().splitlines()
# Get a list of all webservers
webservers = AdminTask.listServers( '[-serverType WEB_SERVER]' ).splitlines()

# Remove webserver from servers list
for webserver in webservers:
    servers.remove( webserver )

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
