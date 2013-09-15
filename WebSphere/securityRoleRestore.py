# securityRoleRestore.py
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de
import os
import sys

# Restore Security Role from Textfile (created with j2eerolebackup

path = sys.argv[0]
if path == '':
    path = '../temp/j2eebackup'    # path where Backup is stored
    print "Setting path to %s!" % path

if not os.path.exists( path ):
    print "Path does not exists, please provide directory with your backup files!"
    sys.exit()

def convertFile2Dict( appname ):
    # function to convert backup txt files of Security Role Backup to a dictionary
    filename = path + '/' + appname + ".txt"
    myfile = open( filename, 'r' )

    count = 0
    dict = {}

    for line in myfile.readlines():
        # for loop through file to read it line by line
        if ( ':' in line ) and ( count > 12 ):
            value = line.split( ':' )[0]
            # cred = line.split(':')[1].strip('\n')
            cred = line.split( ':' )[1]
            # cred = cred.strip(' ')
            cred = cred.strip()
            if value == "Role":
                role = cred
                dict[role] = {}
            dict[role][value] = cred
        count += 1
    return dict

def setSecurityRoles( dictionary, appName ):
    strRoleChange = '['
    for role in dictionary.keys():
        # Loop through Roles
        strRoleChange += '[\"' + role + '\" '
        strRoleChange += dictionary[role]['Everyone?'] + ' '
        strRoleChange += dictionary[role]['All authenticated?'] + ' '
        strRoleChange += '\"' + dictionary[role]['Mapped users'] + '\" '
        strRoleChange += '\"' + dictionary[role]['Mapped groups'] + '\"] '
    strRoleChange += ']]'
    AdminApp.edit( appName, '[-MapRolesToUsers' + strRoleChange + ']' )
    print "Setting Roles and Users for %s" % appName
    AdminConfig.save()

apps = AdminApp.list()
appsList = apps.split( lineSeparator )
# Test with some Apps:
# appsList = ['Blogs','Activities','Wikis']
# or Single App:
# appsList = ['Blogs']
for app in appsList:
    # For testing: set app to example applicatio
    setSecurityRoles( convertFile2Dict( app ), app )
print "Restore of Security Roles finished!"
