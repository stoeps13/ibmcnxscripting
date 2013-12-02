# menu-cnx.py
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de
# Blog: http://www.stoeps.de

import sys
import ibmcnxscript

# Properties and Environment
properties = {
              'strTitle':'Administration of IBM Connections',
              'strPoint1':'(1). CellName',
              'strPoint2':'(2). Backup / Restore',
              'strPoint2a':'(2a). Backup Security Roles (all Apps)',
              'strPoint2b':'(2b). Restore Security Roles (all Apps)',
              'strPoint3':'(3). Configuration',
              'strPoint3a':'(3a). Set J2EE Roles initially (restricted)',
              'strPoint3b':'(3b). Set J2EE Roles initially (unrestricted)',
              'strPoint3c':'(3c). Performance Tuning DataSources',
              'strPoint3d':'(3d). Configure Monitoring Policy',
              'strPoint4':'(4). Documentation',
              'strPoint4a':'(4a). JVM Parameters',
              'strPoint4b':'(4b). WebSphere Variables',
              'strPoint4c':'(4c). DataSource Properties',
              'strPoint5':'(5). User Management',
              'strPoint5a':'(5a). User Management 1',
              'strPoint5b':'(5b). User Management 2',
              'strPoint6':'(6). Troubleshooting',
              'strPoint6a':'(6a). Check DB connections',
              'strPoint6a':'(6b). Check Application Status',
              'strPointE':'(E). Exit'
              }
menu = ''
# Set some values
try:
    cellname = AdminConfig.getCell()
except:
    cellname = '\t\tError: Not started in the right context.'
    print
    print '\t\tYou should run this within wsadmin!'
    print

def menucnx( menu ):
    print properties['strTitle']

    print
    print "\tWhich Operation You Want to process"
    print "\t-----------------------------------"
    print
    print '\t\t' + properties['strPoint1']
    print '\t\t' + properties['strPoint2']
    if menu == '2':
        print '\t\t\t' + properties['strPoint2a']
        print '\t\t\t' + properties['strPoint2b']
    print '\t\t' + properties['strPoint3']
    if menu == '3':
        print '\t\t\t' + properties['strPoint3a']
        print '\t\t\t' + properties['strPoint3b']
        print '\t\t\t' + properties['strPoint3c']
        print '\t\t\t' + properties['strPoint3d']
    print '\t\t' + properties['strPoint4']
    if menu == '4':
        print '\t\t\t' + properties['strPoint4a']
        print '\t\t\t' + properties['strPoint4b']
        print '\t\t\t' + properties['strPoint4c']
    print '\t\t' + properties['strPoint5']
    if menu == '5':
        print '\t\t\t' + properties['strPoint5a']
        print '\t\t\t' + properties['strPoint5b']
    print '\t\t' + properties['strPoint6']
    if menu == '6':
        print '\t\t\t' + properties['strPoint6a']
        print '\t\t\t' + properties['strPoint6b']
    print
    print '\t\t' + properties['strPointE']
    print

    name = raw_input( "\tWhich Operation You Want to process?  " )

    # Work with input values
    if   name == "1":
        print
        print '\tCellname: ' + cellname
        print
    elif name == "2":
        menu = '2'
        menucnx( menu )
        menu = ''
    elif name.lower() == "2a":
        execfile( "securityRoleBackup.py" )
        menu = ''
    elif name.lower == '2b':
            execfile( "securityRoleRestore.py" )
            menu = ''
    elif name == "3":
        menu = '3'
        menucnx( menu )
        menu = ''
    elif name.lower() == '3a':
        execfile( 'ConfigureConnectionsRolesRestricted.py' )
        menu == ''
    elif name.lower() == '3b':
        execfile( 'ConfigureConnectionsRolesUnrestricted.py' )
        menu == ''
    elif name.lower() == '3c':
        execfile( 'cfgDataSource.py' )
        menu == ''
    elif name.lower() == '3d':
        execfile( 'cfgMonitoringPolicy.py' )
        menu == ''
    elif name == "4":
        menu = '4'
        menucnx( menu )
        menu = ''
    elif name.lower() == '4a':
        execfile( "getJVMHeap.py" )
        menucnx( menu )
    elif name.lower() == '4b':
        print '4b'
    elif name.lower() == '4c':
        ibmcnxscript.showJdbcProviders()
        menucnx( menu )
    elif name == "5":
        menu = '5'
        menucnx( menu )
        menu = ''
    elif name.lower() == '5a':
        print '5a'
    elif name.lower() == '5b':
        print '5b'
    elif name == "6":
        menu = '6'
        menucnx( menu )
        menu = ''
    elif name.lower() == '6a':
        execfile( 'checkDataSource.py' )
        menucnx( menu )
    elif name.lower() == '6b':
        execfile( 'checkAppStatus.py' )
        menucnx( menu )
    elif name.lower() == "e":
        quit()

    menucnx( menu )

# Start of program
menucnx( menu )
