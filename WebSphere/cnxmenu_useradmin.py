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


class cnxMenu_useradmin:
    menuitems = []
        
    # Function to add menuitems
    def AddItem( self, text, function ):
        self.menuitems.append( {'text': text, 'func':function} )

    # Function for printing
    def Show( self ):
        c = 1
        print '\n\tWebSphere and Connections Administration - User Admin Tasks'
        print '\t----------------------------------------', '\n'
        for l in self.menuitems:
            print '\t',
            print c, l['text']
            c = c + 1
        print

    def Do( self, n ):
        self.menuitems[n]["func"]()
        

def cnxMemberCheckExIDByEmail():
    execfile( 'cnxMemberCheckExIDByEmail.py' )

def cnxMemberInactivateByEmail():
    execfile( 'cnxMemberInactivateByEmail.py' )

def cnxMemberDeactAndActByEmail():
    execfile( 'cnxMemberDeactAndActByEmail.py' )

def cnxMemberSyncAllByEXID():
    execfile( 'cnxMemberSyncAllByEXID.py' )

def cnxBackToMainMenu():
    execfile( 'cnxmenu.py')
	
def bye():
    print "bye"
    state = 'false'
    sys.exit( 0 )

if __name__ == "__main__":
    m = cnxMenu_useradmin()
    m.AddItem( 'Check External ID (all Apps & Profiles) (cnxMemberCheckExIDByEmail.py)', cnxMemberCheckExIDByEmail )
    m.AddItem( 'Deactivate and Activate a User in one step (cnxMemberDeactAndActByEmail.py)', cnxMemberDeactAndActByEmail )
    m.AddItem( 'Deactivate a User by email address (cnxMemberInactivateByEmail.py)', cnxMemberInactivateByEmail )
    m.AddItem( 'Synchronize ExtID for all Users in all Apps (cnxMemberSyncAllByEXID.py)', cnxMemberSyncAllByEXID )
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
                n = int ( raw_input('Enter your choice [1-6] : ') )
				
                if n < 7 and n > 0:
				    is_valid = 1 ## set it to 1 to validate input and to terminate the while..not loop
                else:
                    print ( "'%s' is not a valid menu option.") % n
        except ValueError, e :
                print ("'%s' is not a valid integer." % e.args[0].split(": ")[1])
   # n = input( "your choice> " )
    m.Do( n - 1 )