# securityrolebackup.py
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de

#path='/home/cstoettner/Dropbox/Devel/ibmcnxscripting/temp'
path='../temp'
apps = AdminApp.list()
appsList = apps.split(lineSeparator)
for app in appsList:
    filename = path + "/" + app + ".txt"
    print "Backup of %s security roles saved." % app.upper()
    my_file = open(filename,'w')
    my_file.write (AdminApp.view(app,"-MapRolesToUsers"))
    my_file.flush
    my_file.close()

