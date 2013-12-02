# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de
# Blog: http://www.stoeps.de

# Check if applications are running
print "Getting application status of all installed applications..."

applications = AdminApp.list().splitlines();

for application in applications:
    applName = AdminControl.completeObjectName( 'type=Application,name=' + application + ',*' )
    if applName != '':
        aStatus = 'running';
    else:
        aStatus = 'stopped';
        print 'Application: ' + application + ' is ' + aStatus

# ToDo: Change Script to write Application name and status to a dictionary, then sort this dict and print
# grouped Applications, first running, after this stopped applications.

# If this works -> change DataSource Script to print grouped status.

# ToDo: Put this in a function, that function can be used in other scripts.
