# Create a WebSphere documentation
#

import ibmcnxscript

# Function to print WebSphere Variables
def websphereVariables( scope ):
    # Check scope (Cell, Node, Server)
    if scope.split( '/' ):
        tab = '\t'

# Declaration
cell = AdminControl.getCell()
nodes = AdminConfig.list( 'Node' ).splitlines()

# Get nodeName of WebServer (exception for log settings)
webserverNodeName = AdminTask.listServers( '[-serverType WEB_SERVER]' ).split( '/' )[3]


vars = AdminConfig.list( 'VariableSubstitutionEntry', AdminConfig.getid( scope ) )
for var in vars:
    name = AdminConfig.showAttribute( var, 'symbolicName' )
    value = AdminConfig.showAttribute( var, 'value' )
    print "\t%s = %s" % ( name, value )

# Print WebSphere Variables (better put in a function, because it is called 3 times
print '\n\nWebSphere Variables CELL SCOPE:'
vars = AdminConfig.list( 'VariableSubstitutionEntry', AdminConfig.getid( '/Cell:' + cell + '/' ) ).splitlines()
for var in vars:
    name = AdminConfig.showAttribute( var, 'symbolicName' )
    value = AdminConfig.showAttribute( var, 'value' )
    print "\t%s = %s" % ( name, value )


for node in nodes:
    nodeName = AdminConfig.showAttribute( node, "name" )

    serverEntries = AdminConfig.list( "ServerEntry", node ).splitlines()

    for serverEntry in serverEntries:

        serverName = AdminConfig.showAttribute( serverEntry, "serverName" )
        server = AdminConfig.getid( '/Cell:' + cell + '/Node:' + nodeName + '/Server:' + serverName + '/' )
        jvm = AdminConfig.list( 'JavaVirtualMachine', server )

        print '\n' + nodeName + '\n'

        # Print WebSphere Variables
        vars = AdminConfig.list( 'VariableSubstitutionEntry', AdminConfig.getid( '/Cell:' + cell + '/Node:' + nodeName + '/' ) ).splitlines()
        print '  WebSphere Variables:\n'
        for var in vars:
            name = AdminConfig.showAttribute( var, 'symbolicName' )
            value = AdminConfig.showAttribute( var, 'value' )
            print "\t%s = %s" % ( name, value )

        print '\n\t' + serverName + '\n'
        # Print WebSphere Variables
        vars = AdminConfig.list( 'VariableSubstitutionEntry', AdminConfig.getid( '/Cell:' + cell + '/Node:' + nodeName + '/Server:' + serverName + '/' ) ).splitlines()
        print '\t  WebSphere Variables:\n'
        for var in vars:
            name = AdminConfig.showAttribute( var, 'symbolicName' )
            value = AdminConfig.showAttribute( var, 'value' )
            print "\t\t%s = %s" % ( name, value )

        print '\n\t\tJavaVirtualMachine Settings'
        print '\t\t  initialHeapSize: ' + AdminConfig.showAttribute( jvm, 'initialHeapSize' ) + ' MB'
        print '\t\t  maximumHeapSize: ' + AdminConfig.showAttribute( jvm, 'maximumHeapSize' ) + ' MB\n'
        print '\t\tPORTS'

        namedEndPoints = AdminConfig.list( "NamedEndPoint", serverEntry ).splitlines()

        for namedEndPoint in namedEndPoints:
            endPointName = AdminConfig.showAttribute( namedEndPoint, 'endPointName' )
            endPoint = AdminConfig.showAttribute( namedEndPoint, 'endPoint' )
            host = AdminConfig.showAttribute( endPoint, 'host' )
            port = AdminConfig.showAttribute( endPoint, 'port' )
            print '\t\t  ' + endPointName + ':' + host + ':' + port

        if nodeName != webserverNodeName:
            log = AdminConfig.showAttribute( server, 'outputStreamRedirect' )
            logsettings = AdminConfig.show( log ).splitlines()
            print '\n\t\tLogSettings:'
            for logsetting in logsettings:
                print '\t\t  ' + logsetting
        else:
            log = ''
            logsettings = ''


