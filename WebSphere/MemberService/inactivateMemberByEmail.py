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
execfile("profilesAdmin.py")

try:
   print "Inactivate Activities"
   ActivitiesMemberService.inactivateMemberByEmail(MAILADDRESS)
except:
   print 'No user with Email' + MAILADDRESS + ' found'

try:
   print "Inactivate Blogs"
   BlogsMemberService.inactivateMemberByEmail(MAILADDRESS)
except:
   print 'No user with Email' + MAILADDRESS + ' found'

try:
   print "Inactivate Communities"
   CommunitiesMemberService.inactivateMemberByEmail(MAILADDRESS)
except:
   print 'No user with Email' + MAILADDRESS + ' found'

try:
   print "Inactivate Dogear"
   DogearMemberService.inactivateMemberByEmail(MAILADDRESS)
except:
   print 'No user with Email' + MAILADDRESS + ' found'

try:
   print "Inactivate Files"
   FilesMemberService.inactivateMemberByEmail(MAILADDRESS)
except:
   print 'No user with Email' + MAILADDRESS + ' found'

try:
   print "Inactivate Forums"
   ForumsMemberService.inactivateMemberByEmail(MAILADDRESS)
except:
   print 'No user with Email' + MAILADDRESS + ' found'

try:
   print "Inactivate News, Search, Homepage"
   NewsMemberService.inactivateMemberByEmail(MAILADDRESS)
except:
   print 'No user with Email' + MAILADDRESS + ' found'

try:
   print "Inactivate Wikis"
   WikisMemberService.inactivateMemberByEmail(MAILADDRESS)
except:
   print 'No user with Email' + MAILADDRESS + ' found'



