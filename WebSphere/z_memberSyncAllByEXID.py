# Script to sychronise User data from LDAP to application
# Call the script through wsadmin.sh|bat and give a EXID as script parameter
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de
#
# example: wsadmin.sh -lang jython -f memberSyncAllByEXID.py true|false
#

EmailMatch = sys.argv[0]

# Loading Connections Administration Commands
execfile( "loadAll.py" )

apps = ['Activities', 'Blogs', 'Communities', 'Dogear', 'Files', 'Forums', 'News', 'Wikis']

def memService( appname, EmailMatch ):
    if( "Activities" == appname ) :
        print "\tActivitiesMemberService.syncAllMembersByExtId"
        ActivitiesMemberService.syncAllMembersByExtId( {"updateOnEmailLoginMatch": EmailMatch } )
    elif( "Blogs" == appname ) :
        print "\tBlogsMemberService.syncAllMembersByExtId"
        BlogsMemberService.syncAllMembersByExtId( {"updateOnEmailLoginMatch": EmailMatch } )
    elif( "News" == appname ) :
        print "\tNewsMemberService.syncAllMembersByExtId"
        NewsMemberService.syncAllMembersByExtId( {"updateOnEmailLoginMatch": EmailMatch } )
    elif( "Dogear" == appname ) :
        print "\tDogearMemberService.syncAllMembersByExtId"
        DogearMemberService.syncAllMembersByExtId( {"updateOnEmailLoginMatch": EmailMatch } )
    elif( "Communities" == appname ) :
        print "\tCommunitesMemberService.syncAllMembersByExtId"
        CommunitiesMemberService.syncAllMembersByExtId( {"updateOnEmailLoginMatch": EmailMatch } )
    elif( "Files" == appname ) :
        print "\tFilesMemberService.syncAllMembersByExtId"
        FilesMemberService.syncAllMembersByExtId( {"updateOnEmailLoginMatch": EmailMatch } )
    elif( "Forums" == appname ) :
        print "\tForumsMemberService.syncAllMembersByExtId"
        ForumsMemberService.syncAllMembersByExtId( {"updateOnEmailLoginMatch": EmailMatch } )
    elif( "Wikis" == appname ) :
        print "\tWikisMemberService.syncAllMembersByExtId"
        WikisMemberService.syncAllMembersByExtId( {"updateOnEmailLoginMatch": EmailMatch } )
    else :
        print "\tUnknown application name '" + appname + "'"

for app in apps:
    print "Sync all Members by EXTID for " + app
    memService( app, EmailMatch )
