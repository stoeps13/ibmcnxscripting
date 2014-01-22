# cnxLibraryPolicies.py
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de
# Blog: http://www.stoeps.de

execfile( "filesAdmin.py" )

import sys

def printLibs( libraries ):
    for i in range( len( libraries ) ):
        print str( i ) + '\t',
        print str( round( libraries[i]['maximumSize'] / 1073741824.0, 2 ) ) + ' GB\t',
        print str( round( libraries[i]['percentUsed'], 2 ) ) + ' %\t',
        print str( libraries[i]['id'] ) + '\t',
        print str( libraries[i]['title'] )

def printPolicies( policies ):
    state = ''
    print '# \tmax Size \t\t uuid \t\t\t\t\t title'
    print '----------------------------------------------------------------------------------------------------'
    for i in range( len( policies ) ):
        print str( i ) + '\t' + str( round( policies[i]['maximumSize'] / 1073741824.0, 2 ) ) + ' GB\t\t' + str( policies[i]['id'] ) + '\t\t' + str( policies[i]['title'] )
    print
    return policies

def combineMaps( personalList, communityList ):
    pLen = len( personalList )
    cLen = len( communityList )
    print
    for i in range( pLen ):
       print str( i ) + '\t',
       print str( round( personalList[i]['maximumSize'] / 1073741824.0, 2 ) ) + ' GB\t',
       print str( round( personalList[i]['percentUsed'], 2 ) ) + ' %\t',
       print str( personalList[i]['id'] ) + '\t',
       print str( personalList[i]['title'] )
    print
    for i in range( cLen ):
       print str( i + pLen ) + '\t',
       print str( round( communityList[i]['maximumSize'] / 1073741824.0, 2 ) ) + ' GB\t',
       print str( round( communityList[i]['percentUsed'], 2 ) ) + ' %\t',
       print str( communityList[i]['id'] ) + '\t',
       print str( communityList[i]['title'] )
    print
    return pLen, cLen

# Combine personal and community FilesLibrary List
personalList = FilesLibraryService.browsePersonal( "title", "true", 1, 100 )
communityList = FilesLibraryService.browseCommunity( "title", "true", 1, 100 )

pLen, cLen = combineMaps( personalList, communityList )

# print 'Libraries: '
# printLibs( libraryList )
# print ''

print 'Available Policies: '
policies = printPolicies( FilesPolicyService.browse( "title", "true", 1, 25 ) )

libraryID = int( raw_input( 'Which library should be changed? (0 - %s) ' % str( pLen + cLen - 1 ) ) )
if libraryID >= pLen:
    libraryID = libraryID - pLen
    libraryType = 'community'
else:
    libraryType = 'personal'

policyID = int( raw_input( 'Which policy do you want to assign? ' ) )

if libraryType == 'personal':
    libraryUUID = personalList[libraryID]['id']
elif libraryType == 'community':
    libraryUUID = communityList[libraryID]['id']
else:
    print "Error can't find Library UUID"

policyUUID = policies[policyID]['id']

FilesLibraryService.assignPolicy( libraryUUID, policyUUID )
