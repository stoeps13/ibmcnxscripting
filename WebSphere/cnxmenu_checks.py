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


class cnxMenu_checks:
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

def cnxBackToMainMenu():
    execfile( 'cnxmenu.py')
	
def bye():
    print "bye"
    state = 'false'
    sys.exit( 0 )

if __name__ == "__main__":
    m = cnxMenu_checks()
    m.AddItem( 'Check if all Apps are running (checkAppStatus.py)', checkAppStatus )
    m.AddItem( 'Check Database connections (checkDataSource.py)', checkDataSource )
    m.AddItem( 'Check JVM Heap Sizes (checkJVMHeap.py)', checkJVMHeap )
    m.AddItem( 'Check SystemOut/Err Log Sizes (checkLogFiles.py)', checkLogFiles )
    m.AddItem( 'Check / Show all used ports (checkPorts.py)', checkPorts )
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
                n = int ( raw_input('Enter your choice [1-7] : ') )
				
                if n < 8 and n > 0:
				    is_valid = 1 ## set it to 1 to validate input and to terminate the while..not loop
                else:
                    print ( "'%s' is not a valid menu option.") % n
        except ValueError, e :
                print ("'%s' is not a valid integer." % e.args[0].split(": ")[1])
   # n = input( "your choice> " )
    m.Do( n - 1 )