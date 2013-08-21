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
execfile("activitiesAdmin.py")
execfile("blogsAdmin.py")
execfile("communitiesAdmin.py")
execfile("dogearAdmin.py")
execfile("filesAdmin.py")
execfile("forumsAdmin.py")
execfile("homepageAdmin.py")
execfile("newsAdmin.py")
execfile("profilesAdmin.py")
execfile("wikisAdmin.py")

try:
   print "Sync Activities"
   ActivitiesMemberService.inactivateMemberByExtId(EXID)
except:
   print 'No user with ExtId ' + EXID + ' found'

try:
   print "Sync Blogs"
   BlogsMemberService.inactivateMemberByExtId(EXID)
except:
   print 'No user with ExtId ' + EXID + ' found'

try:
   print "Sync Communities"
   CommunitiesMemberService.inactivateMemberByExtId(EXID)
except:
   print 'No user with ExtId ' + EXID + ' found'

try:
   print "Sync Dogear"
   DogearMemberService.inactivateMemberByExtId(EXID)
except:
   print 'No user with ExtId ' + EXID + ' found'

try:
   print "Sync Files"
   FilesMemberService.inactivateMemberByExtId(EXID)
except:
   print 'No user with ExtId ' + EXID + ' found'

try:
   print "Sync Forums"
   ForumsMemberService.inactivateMemberByExtId(EXID)
except:
   print 'No user with ExtId ' + EXID + ' found'

try:
   print "Sync News, Search, Homepage"
   NewsMemberService.inactivateMemberByExtId(EXID)
except:
   print 'No user with ExtId ' + EXID + ' found'

try:
   print "Sync Wikis"
   WikisMemberService.inactivateMemberByExtId(EXID)
except:
   print 'No user with ExtId ' + EXID + ' found'

try:
   print "Inactivate Profiles"
   ProfilesService.inactivateUser(EXID)
except:
   print 'No user with ExtId ' + EXID + ' found'

