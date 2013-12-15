# cfgLogFiles.py
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de
#

print "\nChanging the SystemOut & SystemErr log file rotation settings\n"

rollOverType = raw_input( '\tRolloverType (SIZE, BOTH): ' )
maxLogSize = int( raw_input( '\tMax Logfile size in MB (1-50): ' ) )
maxLogHistory = int( raw_input( '\tMax Number of Backup Files (1-200): ' ) )

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
        print "\tChange log setting for: " + nodename + tab + servername

        # output and errorStream
        systemOut = AdminConfig.showAttribute( server, 'outputStreamRedirect' )
        systemErr = AdminConfig.showAttribute( server, 'errorStreamRedirect' )

        if rollOverType == 'BOTH' or rollOverType.upper() == 'B':
            logSetting = '[[rolloverSize ' + str( maxLogSize ) + '] [rolloverPeriod 24] [maxNumberOfBackupFiles ' + str( maxLogHistory ) + ']]'
        else:
            logSetting = '[[rolloverSize ' + str( maxLogSize ) + '] [maxNumberOfBackupFiles ' + str( maxLogHistory ) + ']]'

        # modify settings for log Size and History
        AdminConfig.modify( systemOut, logSetting )
        AdminConfig.modify( systemErr, logSetting )

    except:
        print "Error on setting Log File Size"

# Save Configuration
AdminConfig.save()
print '\n\n'

