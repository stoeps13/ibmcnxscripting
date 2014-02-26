# Script to set nodeRestartState of all Application Servers
# Author: Christoph Stoettner
# Email: christoph.stoettner@stoeps.de

import ibmcnxscript

state = ''
while state != ( 'RUNNING' or 'STOPPED' or 'PREVIOUS' ):
    state = raw_input( 'Which state do you want to set? (S|R|P)(STOPPED|RUNNING|PREVIOUS)' ).upper()
    if state == 'R':
        state = 'RUNNING'
        break
    elif state == 'S':
        state = 'STOPPED'
        break
    elif state == 'P':
        state = 'PREVIOUS'
        break
    else:
        continue

# Get a list of all servers in the cell
servers = AdminTask.listServers( '[-serverType APPLICATION_SERVER]' ).splitlines()

for server in servers:
    print 'Set nodeRestartState for %s to: %s' % ( server.split( '(' )[0], state.upper() )
    monitoringPolicy = AdminConfig.list( "MonitoringPolicy", server )
    AdminConfig.modify( monitoringPolicy, '[[nodeRestartState ' + state.upper() + ']]' )

AdminConfig.save()

print "Synchronizing Nodes"
# ibmcnxscript.synchAllNodes()
