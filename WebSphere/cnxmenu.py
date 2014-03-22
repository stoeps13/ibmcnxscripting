# Author: Christop Stoettner
# E-Mail: info@stoeps.de
#

import sys
import os

# Load all jython commands, when they are not loaded
try:
    NewsActivityStreamService.listApplicationRegistrations()
except NameError:
    print "Connections Commands not loaded! Load now: "
    execfile("loadAll.py")

class cnxMenu:
    menuitems = []

    # Function to add menuitems
    def AddItem( self, text, function ):
        self.menuitems.append( {'text': text, 'func':function} )

    # Function for printing
    def Show( self ):
        c = 1
        print '\n\tWebSphere and Connections Administration'
        print '\t----------------------------------------', '\n'
        for l in self.menuitems:
            print '\t',
            print c, l['text']
            c = c + 1
        print

    def Do( self, n ):
        self.menuitems[n]["func"]()

def cfgDataSource():
    execfile( "cfgDataSource.py" )

def cfgJ2EERoleBackup():
    execfile( "cfgJ2EERoleBackup.py" )

def cfgJ2EERoleRestore():
    execfile( "cfgJ2EERoleRestore.py" )

def cfgJ2EERolesRestricted():
    execfile( "cfgJ2EERolesRestricted.py" )

def cfgJ2EERolesUnrestricted():
    execfile( "cfgJ2EERolesUnrestricted.py" )

def cfgJ2EERoleGlobalModerator():
    execfile( "cfgJ2EERoleGlobalModerator.py" )

def cfgJ2EERoleMetricsReader():
    execfile( "cfgJ2EERoleMetricsReader.py" )

def cfgJ2EERoleMetricsReportRun():
    execfile( "cfgJ2EERoleMetricsReportRun.py" )

def cfgJ2EERoleSocialMail():
    execfile( "cfgJ2EERoleSocialMail.py" )

def cfgJVMHeap():
    execfile( "cfgJVMHeap.py" )

def cfgLogFiles():
    execfile( "cfgLogFiles.py" )

def cfgMonitoringPolicy():
    execfile( 'cfgMonitoringPolicy.py' )

def checkAppStatus():
    execfile( 'checkAppStatus.py' )

def checkDataSource():
    execfile( 'checkDataSource.py' )

def checkJVMHeap():
    execfile( 'checkJVMHeap.py' )

def checkLogFiles():
    execfile( 'checkLogFiles.py' )

def checkPorts():
    execfile( 'checkPorts.py' )

def checkVariables():
    execfile( 'checkVariables.py' )

def cnxFilesPolicies():
    execfile( 'cnxFilesPolicies.py' )

def cnxLibraryPolicies():
    execfile( 'cnxLibraryPolicies.py' )

def cnxMemberCheckExIDByEmail():
    execfile( 'cnxMemberCheckExIDByEmail.py' )

def cnxMemberInactivateByEmail():
    execfile( 'cnxMemberInactivateByEmail.py' )

def cnxMemberDeactAndActByEmail():
    execfile( 'cnxMemberDeactAndActByEmail.py' )

def cnxMemberSyncAllByEXID():
    execfile( 'cnxMemberSyncAllByEXID.py' )

def cnxCommunitiesReparenting():
    execfile( 'cnxCommunitiesReparenting.py' )
	
def cnxmenu_cfgtasks():
	execfile( 'cnxmenu_cfgtasks.py' )

def cnxmenu_useradmin():
	execfile( 'cnxmenu_useradmin.py' )

def cnxmenu_comm():
	execfile( 'cnxmenu_comm.py' )

def cnxmenu_checks():
	execfile( 'cnxmenu_checks.py' )
	
def bye():
    print "bye"
    state = 'false'
    sys.exit( 0 )

if __name__ == "__main__":
    m = cnxMenu()
#    m.AddItem( "Configure DataSources (cfgDataSource.py)", cfgDataSource )
#    m.AddItem( 'Backup J2EE Roles of all Applications (cfgJ2EERoleBackup.py)', cfgJ2EERoleBackup )
#    m.AddItem( 'Restore J2EE Roles of all Applications (cfgJ2EERoleRestore.py)', cfgJ2EERoleRestore )
#    m.AddItem( 'Set J2EE Roles initially (restricted) (cfgJ2EERolesRestricted.py)', cfgJ2EERolesRestricted )
#    m.AddItem( 'Set J2EE Roles initially (unrestricted) (cfgJ2EERolesUnrestricted.py)', cfgJ2EERolesUnrestricted )
#    m.AddItem( 'Set J2EE Roles for Moderator Roles (cfgJ2EERoleGlobalModerator.py)', cfgJ2EERoleGlobalModerator )
#    m.AddItem( 'Set J2EE Role for Metrics Reader (cfgJ2EERoleMetricsReader.py)', cfgJ2EERoleMetricsReader )
#    m.AddItem( 'Set J2EE Role for Metrics Report Run (cfgJ2EERoleMetricsReportRun)', cfgJ2EERoleMetricsReportRun )
#    m.AddItem( 'Set J2EE Role for SocialMail (cfgJ2EERoleSocialMail)', cfgJ2EERoleSocialMail )
#    m.AddItem( 'Configure JVM Heap Sizes (cfgJVMHeap.py)', cfgJVMHeap )
#    m.AddItem( 'Configure SystemOut/Err Log Size (cfgLogFiles.py)', cfgLogFiles )
#    m.AddItem( 'Configure Monitoring Policy (cfgMonitoringPolicy.py)', cfgMonitoringPolicy )
#    m.AddItem( 'Check if all Apps are running (checkAppStatus.py)', checkAppStatus )
#    m.AddItem( 'Check Database connections (checkDataSource.py)', checkDataSource )
#    m.AddItem( 'Check JVM Heap Sizes (checkJVMHeap.py)', checkJVMHeap )
#    m.AddItem( 'Check SystemOut/Err Log Sizes (checkLogFiles.py)', checkLogFiles )
#    m.AddItem( 'Check / Show all used ports (checkPorts.py)', checkPorts )
#    m.AddItem( 'Show WebSphere Variables (checkVariables.py)', checkVariables )
#    m.AddItem( 'Work with Files Policies (cnxFilesPolicies.py)', cnxFilesPolicies )
#    m.AddItem( 'Work with Libraries (cnxLibraryPolicies.py)', cnxLibraryPolicies )
#    m.AddItem( 'Check External ID (all Apps & Profiles) (cnxMemberCheckExIDByEmail.py)', cnxMemberCheckExIDByEmail )
#    m.AddItem( 'Deactivate and Activate a User in one step (cnxMemberDeactAndActByEmail.py)', cnxMemberDeactAndActByEmail )
#    m.AddItem( 'Deactivate a User by email address (cnxMemberInactivateByEmail.py)', cnxMemberInactivateByEmail )
#    m.AddItem( 'Synchronize ExtID for all Users in all Apps (cnxMemberSyncAllByEXID.py)', cnxMemberSyncAllByEXID )
#    m.AddItem( 'Reparent/Move Communities (cnxCommunitiesReparenting.py)', cnxCommunitiesReparenting )
    m.AddItem( 'Menu - IBM Connections Configuration Tasks', cnxmenu_cfgtasks )
    m.AddItem( 'Menu - IBM Connections/WebSphere Check Tasks', cnxmenu_checks )
    m.AddItem( 'Menu - IBM Connections User Admin Tasks', cnxmenu_useradmin )
    m.AddItem( 'Menu - IBM Connections Community Admin Tasks', cnxmenu_comm )
    m.AddItem( "Exit", bye )

state = 'True'
while state == 'True':
    m.Show()

    ###########################
    ## Robust error handling ##
    ## only accept int       ##
    ###########################
    ## Wait for valid input in while...not ###
    is_valid=0
    while not is_valid :
        try :
                n = int ( raw_input('Enter your choice [1-5] : ') )
				
                if n < 6 and n > 0:
				    is_valid = 1 ## set it to 1 to validate input and to terminate the while..not loop
                else:
                    print ( "'%s' is not a valid menu option.") % n
        except ValueError, e :
                print ("'%s' is not a valid integer." % e.args[0].split(": ")[1])
   # n = input( "your choice> " )
    m.Do( n - 1 )