# cfgLogFiles.py
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de
#
# ToDo:
#
# test if nodeagent and dmgr are in servers-list

maxLogSize = int( raw_input( '\tMax Logfile size in MB (int): ' ) )
maxLogHistory = int( raw_input( '\tMax Number of Backup Files (int): ' ) )

print "\nChanging the SystemOut & SystemErr log file rotation settings\n"

# Get a list of all servers in WAS cell
servers = AdminTask.listServers( '[-serverType APPLICATION_SERVER]' ).splitlines()

for server in servers:
    # get ID of server
    serverID = AdminConfig.getid( server )

    # output and errorStream
    systemOut = AdminConfig.showAttribute( serverID, 'outputStreamRedirect' )
    systemErr = AdminConfig.showAttribute( serverID, 'errorStreamRedirect' )

    # modify settings for log Size and History
    AdminConfig.modify( systemOut, '[[rolloverSize ' + maxLogSize + '] [maxNumberOfBackupFiles ' + maxLogHistory + ']]' )
    AdminConfig.modify( systemErr, '[[rolloverSize ' + maxLogSize + '] [maxNumberOfBackupFiles ' + maxLogHistory + ']]' )

# Save Configuration
AdminConfig.save()

