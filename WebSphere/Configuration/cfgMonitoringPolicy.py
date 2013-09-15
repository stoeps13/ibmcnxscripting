# Script to set nodeRestartState of all Application Servers
# Author: Christoph Stoettner
# Email: christoph.stoettner@stoeps.de

import ibmcnxscript

# Check if a argv variable was used when calling the script
if len( sys.argv ) == 1:
	state = sys.argv[0]

# if no argv, then loop for a keyboard input
# You can use s,r,p or the whole word

else:
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

ibmcnxscript.synchAllNodes()
