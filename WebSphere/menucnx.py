# menu-cnx.py
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de
# Blog: http://www.stoeps.de

import sys
import ibmcnxscript

# Properties and Environment
properties = {
              'strTitle':'Administration of IBM WebSphere & IBM Connections',
              'strPoint1':'(1). CellName',
              'strPoint2':'(2). Backup / Restore',
              'strPoint2a':'(2a). Backup Security Roles (all Apps)',
              'strPoint2b':'(2b). Restore Security Roles (all Apps)',
              'strPoint3':'(3). Configuration',
              'strPoint3a':'(3a). Set J2EE Roles initially (restricted)',
              'strPoint3b':'(3b). Set J2EE Roles initially (unrestricted)',
              'strPoint3c':'(3c). Performance Tuning DataSources',
              'strPoint3d':'(3d). Configure Monitoring Policy',
              'strPoint3e':'(3e). Configure SystemOut/Err Log Size',
              'strPoint3f':'(3f). Configure JVM Heap Size',
              'strPoint4':'(4). Documentation',
              'strPoint4a':'(4a). JVM Parameters',
              'strPoint4b':'(4b). WebSphere Variables',
              'strPoint4c':'(4c). JVM Properties',
              'strPoint5':'(5). User Management',
              'strPoint5a':'(5a). Deactivate and Activate a User',
              'strPoint5a':'(5b). Deactivate a User by Email (all Apps)',
              'strPoint5c':'(5c). Sync all User in all Apps by Ext ID',
              'strPoint6':'(6). Troubleshooting',
              'strPoint6a':'(6a). Check DB connections',
              'strPoint6b':'(6b). Check Application Status',
              'strPoint6c':'(6c). Check External ID of a User',
              'strPoint7':'(7). Connections Administration',
              'strPoint7a':'(7a). Work with Files Policies',
              'strPoint7b':'(7b). Add Policies to Libraries',
              'strPointE':'(E). Exit'
              }
menu = ''
# Set some values
try:
    cellname = AdminControl.getCell()
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
        print '\t\t\t' + properties['strPoint3e']
        print '\t\t\t' + properties['strPoint3f']
    print '\t\t' + properties['strPoint4']
    if menu == '4':
        print '\t\t\t' + properties['strPoint4a']
        print '\t\t\t' + properties['strPoint4b']
        print '\t\t\t' + properties['strPoint4c']
    print '\t\t' + properties['strPoint5']
    if menu == '5':
        print '\t\t\t' + properties['strPoint5a']
        print '\t\t\t' + properties['strPoint5b']
        print '\t\t\t' + properties['strPoint5c']
    print '\t\t' + properties['strPoint6']
    if menu == '6':
        print '\t\t\t' + properties['strPoint6a']
        print '\t\t\t' + properties['strPoint6b']
        print '\t\t\t' + properties['strPoint6c']
    if menu == '7':
        print '\t\t\t' + properties['strPoint7a']
        print '\t\t\t' + properties['strPoint7b']
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
        execfile( "cfgJ2EERoleBackup.py" )
        menu = ''
    elif name.lower == '2b':
            execfile( "cfgJ2EERoleRestore.py" )
            menu = ''
    elif name == "3":
        menu = '3'
        menucnx( menu )
        menu = ''
    elif name.lower() == '3a':
        execfile( 'cfgJ2EERolesRestricted.py' )
        menu == ''
    elif name.lower() == '3b':
        execfile( 'cfgJ2EERolesUnrestricted.py' )
        menu == ''
    elif name.lower() == '3c':
        execfile( 'cfgDataSource.py' )
        menu == ''
    elif name.lower() == '3d':
        execfile( 'cfgMonitoringPolicy.py' )
        menu == ''
    elif name.lower() == '3e':
        execfile( 'cfgLogFiles.py' )
        menu == ''
    elif name.lower() == '3f':
        execfile( 'cfgJVMHeap.py' )
        menu == ''
    elif name == "4":
        menu = '4'
        menucnx( menu )
        menu = ''
    elif name.lower() == '4a':
        execfile( "checkJVMHeap.py" )
        menu = ''
    elif name.lower() == '4b':
		execfile( "checkVariables.py" )
		menu = ''
    elif name.lower() == '4c':
		execfile( "checkPorts.py" )
		menu = ''
    elif name == "5":
        menu = '5'
        menucnx( menu )
        menu = ''
    elif name.lower() == '5a':
        execfile( 'cnxMemberDeactAndActByEmail.py' )
        menu = ''
    elif name.lower() == '5b':
        execfile( 'cnxMemberInactivateByEmail.py' )
        menu = ''
    elif name.lower() == '5c':
        execfile( "cnxMemberSyncAllByEXID.py" )
        menu = ''
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
    elif name.lower() == '6c':
        execfile( 'cnxMemberCheckExIDByEmail.py' )
        menucnx( menu )
    elif name == "7":
        menu = '7'
        menucnx( menu )
        menu = ''
    elif name.lower() == '7a':
        execfile( 'cnxFilesPolicies.py' )
        menucnx( menu )
        menu = ''
    elif name.lower() == '7b':
        execfile( 'cnxLibraryPolicies.py' )
        menucnx( menu )
        menu = ''
    elif name.lower() == "e":
        quit()

    menucnx( menu )

# Start of program
menucnx( menu )
