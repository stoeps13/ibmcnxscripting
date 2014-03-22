# Author: Christop Stoettner
# E-Mail: info@stoeps.de
#

#import sys
#import os

# Load all jython commands, when they are not loaded
try:
    NewsActivityStreamService.listApplicationRegistrations()
except NameError:
    print "Connections Commands not loaded! Load now: "
    execfile("loadAll.py")


class cnxMenu_cfgtasks:
    menuitems = []

    # Function to add menuitems
    def AddItem( self, text, function ):
        self.menuitems.append( {'text': text, 'func':function} )

    # Function for printing
    def Show( self ):
        c = 1
        print '\n\tWebSphere and Connections Administration - Checks Tasks'
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

def cfgJVMCustProp():
    execfile( "cfgJVMCustProp.py" )

def cfgLogFiles():
    execfile( "cfgLogFiles.py" )

def cfgMonitoringPolicy():
    execfile( 'cfgMonitoringPolicy.py' )


def cnxBackToMainMenu():
    execfile( 'cnxmenu.py')

def bye():
    print "bye"
    state = 'false'
    sys.exit( 0 )

if __name__ == "__main__":
    m = cnxMenu_cfgtasks()
    m.AddItem( "Configure DataSources (cfgDataSource.py)", cfgDataSource )
    m.AddItem( 'Backup J2EE Roles of all Applications (cfgJ2EERoleBackup.py)', cfgJ2EERoleBackup )
    m.AddItem( 'Restore J2EE Roles of all Applications (cfgJ2EERoleRestore.py)', cfgJ2EERoleRestore )
    m.AddItem( 'Set J2EE Roles initially (restricted) (cfgJ2EERolesRestricted.py)', cfgJ2EERolesRestricted )
    m.AddItem( 'Set J2EE Roles initially (unrestricted) (cfgJ2EERolesUnrestricted.py)', cfgJ2EERolesUnrestricted )
    m.AddItem( 'Set J2EE Roles for Moderator Roles (cfgJ2EERoleGlobalModerator.py)', cfgJ2EERoleGlobalModerator )
    m.AddItem( 'Set J2EE Role for Metrics Reader (cfgJ2EERoleMetricsReader.py)', cfgJ2EERoleMetricsReader )
    m.AddItem( 'Set J2EE Role for Metrics Report Run (cfgJ2EERoleMetricsReportRun)', cfgJ2EERoleMetricsReportRun )
    m.AddItem( 'Set J2EE Role for SocialMail (cfgJ2EERoleSocialMail)', cfgJ2EERoleSocialMail )
    m.AddItem( 'Configure JVM Heap Sizes (cfgJVMHeap.py)', cfgJVMHeap )
    m.AddItem( 'Set Custom Parameter for Cache Issues in JVM (cfgJVMCustProp.py)', cfgJVMCustProp )
    m.AddItem( 'Configure SystemOut/Err Log Size (cfgLogFiles.py)', cfgLogFiles )
    m.AddItem( 'Configure Monitoring Policy (cfgMonitoringPolicy.py)', cfgMonitoringPolicy )
    m.AddItem( 'Work with Files Policies (cnxFilesPolicies.py)', cnxFilesPolicies )
    m.AddItem( 'Work with Libraries (cnxLibraryPolicies.py)', cnxLibraryPolicies )
    m.AddItem( 'Back to Main Menu (cnxmenu.py)', cnxBackToMainMenu )
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
                n = int ( raw_input('Enter your choice [1-16] : ') )

                if n < 17 and n > 0:
				    is_valid = 1 ## set it to 1 to validate input and to terminate the while..not loop
                else:
                    print ( "'%s' is not a valid menu option.") % n
        except ValueError, e :
                print ("'%s' is not a valid integer." % e.args[0].split(": ")[1])
   # n = input( "your choice> " )
    m.Do( n - 1 )
