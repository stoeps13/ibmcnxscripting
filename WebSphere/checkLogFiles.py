# cfgLogFiles.py
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de
#

print "\nSystemOut & SystemErr log file rotation settings\n"

# Get a list of all servers in WAS cell (dmgr, nodeagents, AppServer, webserver)
servers = AdminTask.listServers().splitlines()
# Get a list of all webservers
webservers = AdminTask.listServers( '[-serverType WEB_SERVER]' ).splitlines()

# Remove webserver from servers list
for webserver in webservers:
    servers.remove( webserver )

print ''

for server in servers:
    try:

        nodename = server.split( '(' )[1].split( '/' )[3]
        servername = server.split( '(' )[1].split( '/' )[5].split( '|' )[0]

        if len( nodename ) < 10:
            tab = '\t\t\t'
        elif len( nodename ) > 10 and len( nodename ) < 15:
            tab = '\t\t'
        else:
            tab = '\t'

        # Print Node- and Servername
        print "\n\n\tLog setting for: " + nodename + tab + servername

        # output and errorStream
        systemOut = AdminConfig.showAttribute( server, 'outputStreamRedirect' )
        systemErr = AdminConfig.showAttribute( server, 'errorStreamRedirect' )

        logsettings = AdminConfig.show( systemOut ).splitlines()
        print '\n\t\tLogSettings SystemOut:'
        for logsetting in logsettings:
            print '\t\t  ' + logsetting

        logsettings = AdminConfig.show( systemErr ).splitlines()
        print '\n\t\tLogSettings SystemErr:'
        for logsetting in logsettings:
            print '\t\t  ' + logsetting

    except:
        print "Error occured"
