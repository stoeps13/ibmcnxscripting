# getJVMCustProp.py
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de
# Usage: wsadmin -f getJvmCustProp.py

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
    print 'Actual setting: '

    print 'Setting JVM Custom Property'

    AdminConfig.create('Property', jvm, '[[validationExpression ""] [name "com.ibm.ws.cache.CacheConfig.filteredStatusCodes"] [description "Added for js load issue 2014-3-17"] [value "304 404 500 502"] [required "false"]]')

AdminConfig.save()
