# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de
# Blog: http://www.stoeps.de

# Check if applications are running
print "Getting application status of all installed applications..."

applications = AdminApp.list().splitlines();

runningApps = []
stoppedApps = []

for application in applications:
    applName = AdminControl.completeObjectName( 'type=Application,name=' + application + ',*' )
    if applName != '':
        aStatus = 'running';
        runningApps.append( application )
    else:
        aStatus = 'stopped';
        stoppedApps.append( application )

print ''
print '\tRUNNING APPLICATIONS: \n'
for app in runningApps:
    print '\t\t' + app

print ''
print '\tSTOPPED APPLICATIONS: \n'
for app in stoppedApps:
    print '\t\t' + app

print ''
