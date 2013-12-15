# cfgLogFiles.py
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de
#
# ToDo:
#
# test if nodeagent and dmgr are in servers-list

maxLogSize = int( raw_input( '\tMax Logfile size in MB (1-50): ' ) )
maxLogHistory = int( raw_input( '\tMax Number of Backup Files (1-200): ' ) )

print "\nChanging the SystemOut & SystemErr log file rotation settings\n"

# Get a list of all servers in WAS cell (dmgr, nodeagents, AppServer, webserver)
servers = AdminTask.listServers().splitlines()
# Get a list of all webservers
webservers = AdminTask.listServers( '[-serverType WEB_SERVER]' ).splitlines()

# Remove webserver from servers list
for webserver in webservers:
    servers.remove( webserver )

for server in servers:
    # Print Node- and Servername
    print "Change log setting for: " + server.split( '(' )[1].split( '/' )[3] + ' ' + server.split( '(' )[1].split( '/' )[5].split( '|' )[0]
    try:

        # output and errorStream
        systemOut = AdminConfig.showAttribute( server, 'outputStreamRedirect' )
        systemErr = AdminConfig.showAttribute( server, 'errorStreamRedirect' )

        # modify settings for log Size and History
        AdminConfig.modify( systemOut, '[[rolloverSize ' + str( maxLogSize ) + '] [maxNumberOfBackupFiles ' + str( maxLogHistory ) + ']]' )
        AdminConfig.modify( systemErr, '[[rolloverSize ' + str( maxLogSize ) + '] [maxNumberOfBackupFiles ' + str( maxLogHistory ) + ']]' )

    except:
        print "Error on setting Log File Size"

# Save Configuration
AdminConfig.save()

