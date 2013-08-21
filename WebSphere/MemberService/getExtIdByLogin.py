# Script to sychronise User data from LDAP to application
# Call the script through wsadmin.sh|bat and give a uid as script parameter
#
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de
# example: wsadmin.sh -lang jython -f memberSyncByEmail.py cstoettner
#


LOGIN = sys.argv[0]
print "Syncing MemberService for " + LOGIN

# Loading Connections Administration Commands
execfile("activitiesAdmin.py")
execfile("blogsAdmin.py")
execfile("communitiesAdmin.py")
execfile("dogearAdmin.py")
execfile("filesAdmin.py")
execfile("forumsAdmin.py")
execfile("homepageAdmin.py")
execfile("newsAdmin.py")
#execfile("profilesAdmin.py")
execfile("wikisAdmin.py")

#try:
#   print "ExtId Profiles: ",
#   print ProfilesService.getMemberExtIdByLogin(LOGIN)
#except:
#   print 'No user with Login ' + LOGIN + ' found'

try:
   print "ExtId Activities: ",
   print ActivitiesMemberService.getMemberExtIdByLogin(LOGIN)
except:
   print 'No user with Login ' + LOGIN + ' found'

try:
   print "ExtId Blogs: ",
   print BlogsMemberService.getMemberExtIdByLogin(LOGIN)
except:
   print 'No user with Login ' + LOGIN + ' found'

try:
   print "ExtId Communities: ",
   print CommunitiesMemberService.getMemberExtIdByLogin(LOGIN)
except:
   print 'No user with Login ' + LOGIN + ' found'

try:
   print "ExtId Dogear: ",
   print DogearMemberService.getMemberExtIdByLogin(LOGIN)
except:
   print 'No user with Login ' + LOGIN + ' found'

try:
   print "ExtId Files: ",
   print FilesMemberService.getMemberExtIdByLogin(LOGIN)
except:
   print 'No user with Login ' + LOGIN + ' found'

try:
   print "ExtId Forums: ",
   print ForumsMemberService.getMemberExtIdByLogin(LOGIN)
except:
   print 'No user with Login ' + LOGIN + ' found'

try:
   print "ExtId News, Search, Homepage: ",
   print NewsMemberService.getMemberExtIdByLogin(LOGIN)
except:
   print 'No user with Login ' + LOGIN + ' found'

try:
   print "ExtId Wikis: ",
   print WikisMemberService.getMemberExtIdByLogin(LOGIN)
except:
   print 'No user with Login ' + LOGIN + ' found'

