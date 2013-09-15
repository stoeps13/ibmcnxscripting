# Script to sychronise User data from LDAP to application
# Call the script through wsadmin.sh|bat and give a EXID as script parameter
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de
#
# example: wsadmin.sh -lang jython -f memberSyncByEmail.py 84A543FE-A27D-395A-C125-7B8F00665563
#


EXID = sys.argv[0]
print "Syncing MemberService for " + EXID

# Loading Connections Administration Commands
execfile( "loadAll.py" )

try:
   print "Sync Activities"
   ActivitiesMemberService.syncMemberByExtId( EXID )
except:
   print 'No user with ExtId ' + EXID + ' found'

try:
   print "Sync Blogs"
   BlogsMemberService.syncMemberByExtId( EXID )
except:
   print 'No user with ExtId ' + EXID + ' found'

try:
   print "Sync Communities"
   CommunitiesMemberService.syncMemberByExtId( EXID )
except:
   print 'No user with ExtId ' + EXID + ' found'

try:
   print "Sync Dogear"
   DogearMemberService.syncMemberByExtId( EXID )
except:
   print 'No user with ExtId ' + EXID + ' found'

try:
   print "Sync Files"
   FilesMemberService.syncMemberByExtId( EXID )
except:
   print 'No user with ExtId ' + EXID + ' found'

try:
   print "Sync Forums"
   ForumsMemberService.syncMemberByExtId( EXID )
except:
   print 'No user with ExtId ' + EXID + ' found'

try:
   print "Sync News, Search, Homepage"
   NewsMemberService.syncMemberByExtId( EXID )
except:
   print 'No user with ExtId ' + EXID + ' found'

try:
   print "Sync Wikis"
   WikisMemberService.syncMemberByExtId( EXID )
except:
   print 'No user with ExtId ' + EXID + ' found'

