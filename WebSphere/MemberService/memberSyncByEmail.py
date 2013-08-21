# Script to sychronise User data from LDAP to application
# Call the script through wsadmin.sh|bat and give a mailaddress as script parameter
#
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de
#
# example: wsadmin.sh -lang jython -f memberSyncByEmail.py cstoettner@fum.de
#


MAILADDRESS = sys.argv[0]
print "Syncing MemberService for " + MAILADDRESS

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
   ActivitiesMemberService.syncMemberExtIdByEmail(MAILADDRESS)
except:
   print 'No user with Email ' + MAILADDRESS +' found'

try:
   print "Sync Blogs"
   BlogsMemberService.syncMemberExtIdByEmail(MAILADDRESS)
except:
   print 'No user with Email ' + MAILADDRESS +' found'

try:
   print "Sync Communities"
   CommunitiesMemberService.syncMemberExtIdByEmail(MAILADDRESS)
except:
   print 'No user with Email ' + MAILADDRESS +' found'

try:
   print "Sync Dogear"
   DogearMemberService.syncMemberExtIdByEmail(MAILADDRESS)
except:
   print 'No user with Email ' + MAILADDRESS +' found'

try:
   print "Sync Files"
   FilesMemberService.syncMemberExtIdByEmail(MAILADDRESS)
except:
   print 'No user with Email ' + MAILADDRESS +' found'

try:
   print "Sync Forums"
   ForumsMemberService.syncMemberExtIdByEmail(MAILADDRESS)
except:
   print 'No user with Email ' + MAILADDRESS +' found'

try:
   print "Sync News, Search, Homepage"
   NewsMemberService.syncMemberExtIdByEmail(MAILADDRESS)
except:
   print 'No user with Email ' + MAILADDRESS +' found'

try:
   print "Sync Wikis"
   WikisMemberService.syncMemberExtIdByEmail(MAILADDRESS)
except:
   print 'No user with Email ' + MAILADDRESS +' found'

