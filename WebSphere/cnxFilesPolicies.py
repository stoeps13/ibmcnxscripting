# cfgFilesPolicies.py
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de
# Blog: http://www.stoeps.de

import sys

execfile("filesAdmin.py")

#def loadFilesAdmin():
#    execfile( 'filesAdmin.py' )

def deletePolicy( uuid ):
    FilesPolicyService.delete( uuid )

def addPolicy( title, maxSize ):
    FilesPolicyService.add( title, maxSize * 1073741824.0 )

def editPolicy( uuid, title, maxSize ):
    FilesPolicyService.edit( uuid, title, maxSize )

def getPolicies():
    policies = FilesPolicyService.browse( "title", "true", 1, 25 )
    return policies

def printPolicies( policies ):
    state = ''
    print '# \tmax Size \t\t uuid \t\t\t\t\t title'
    print '----------------------------------------------------------------------------------------------------'
    for i in range( len( policies ) ):
        print str( i ) + '\t' + str( round( policies[i]['maximumSize'] / 1073741824.0, 2 ) ) + ' GB\t\t' + str( policies[i]['id'] ) + '\t\t' + str( policies[i]['title'] )
    print
    print '\t What do you want to do?'
    while state != ( 'MENU' or 'EXIT' ):
        state = raw_input( '(A)dd, (E)dit, (D)elete a policy, (M)enu or E(X)it for Policy Listing  ' ).upper()
        if state == 'A':
            state = 'ADD'
            title = raw_input( 'Title of Policy: ' )
            maxSize = float( raw_input( 'max Library Size in GB: ' ) )
            addPolicy( title, maxSize )
        elif state == 'E':
            state = 'EDIT'
            policy = int( raw_input( 'Policy ID to edit: ' ) )
            title = raw_input( 'New Title for Policy: ' )
            if title == '':
                title = policies[policy]['title']
            maxSize = raw_input( 'New max Size for Policy (GB): ' )
            if maxSize != '':
                maxSize = float( maxSize ) * 1073741824.0
            elif maxSize == '':
                maxSize = float( policies[policy]['maximumSize'] )
            editPolicy( policies[policy]['id'], title, maxSize )
        elif state == 'D':
            state = 'DELETE'
            policy = int( raw_input( 'Delete policy ID (#)? ' ) )
            deletePolicy( policies[policy]['id'] )
        elif state == 'M':
            state = 'MENU'
            execfile( 'cnxmenu.py' )
            break
        elif state == 'X':
            state = 'EXIT'
            break
        else:
            continue

#loadFilesAdmin()
policies = getPolicies()
printPolicies( policies )


