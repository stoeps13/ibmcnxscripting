import os
import sys
from java.util import Properties

execfile("loadAll.py")

# add the jar to your classpath, then import it
# better to read WebSphere variable PROFILES_JDBC_DRIVER_HOME
sys.path.append( '/opt/IBM/JDBC/db2jcc4.jar' )
import com.ibm.db2.jcc.DB2Driver as Driver

# Change User and Password
props = Properties()
props.put( 'user', 'lcuser' )
props.put( 'password', 'password' )

# Change Hostname, Port and maybe DB Name
conn = Driver().connect( 'jdbc:db2://cnxdb2.stoeps.local:50000/PEOPLEDB', props )

stmt = conn.createStatement()

email = raw_input( "Mail address of profile you want to deactivate: " ).lower()

sql = 'select PROF_UID,PROF_MAIL,PROF_MAIL_LOWER,PROF_GUID from empinst.employee where PROF_MAIL_LOWER = \'' + email + '\' order by PROF_UID_LOWER'
rs = stmt.executeQuery( sql )

employeeList = []
while ( rs.next() ):
    row = {}
    row['PROF_UID'] = rs.getString( 1 )
    row['PROF_MAIL'] = rs.getString( 2 )
    row['PROF_MAIL_LOWER'] = rs.getString( 3 )
    row['PROF_GUID'] = rs.getString( 4 )
    employeeList.append( row )

rs.close()
stmt.close()
conn.close()

# print the result
for e in employeeList:
    # print e['PROF_UID_LOWER'] + "\t\t" + e['PROF_MAIL_LOWER'] + "\t\t" + e['PROF_GUID']
    # print e['PROF_MAIL']
    print 'Deactivate User with ExID: ' + e['PROF_GUID']

MAILADDRESS = e['PROF_MAIL']

try:
   print "Inactivate Activities ",
   ActivitiesMemberService.inactivateMemberByEmail( MAILADDRESS )
except:
   print 'No user with Email ' + MAILADDRESS + ' found'

try:
   print "Inactivate Blogs ",
   BlogsMemberService.inactivateMemberByEmail( MAILADDRESS )
except:
   print 'No user with Email ' + MAILADDRESS + ' found'

try:
   print "Inactivate Communities ",
   CommunitiesMemberService.inactivateMemberByEmail( MAILADDRESS.lower() )
except:
   print 'No user with Email ' + MAILADDRESS + ' found'

try:
   print "Inactivate Dogear ",
   DogearMemberService.inactivateMemberByEmail( MAILADDRESS )
except:
   print 'No user with Email ' + MAILADDRESS + ' found'

try:
   print "Inactivate Files ",
   FilesMemberService.inactivateMemberByEmail( MAILADDRESS )
except:
   print 'No user with Email ' + MAILADDRESS + ' found'

try:
   print "Inactivate Forums ",
   ForumsMemberService.inactivateMemberByEmail( MAILADDRESS )
except:
   print 'No user with Email ' + MAILADDRESS + ' found'

try:
   print "Inactivate News, Search, Homepage ",
   NewsMemberService.inactivateMemberByEmail( MAILADDRESS )
except:
   print 'No user with Email ' + MAILADDRESS + ' found'

try:
   print "Inactivate Wikis ",
   WikisMemberService.inactivateMemberByEmail( MAILADDRESS )
except:
   print 'No user with Email ' + MAILADDRESS + ' found'

try:
    print 'Inactivate Profiles ',
    ProfilesService.inactivateUser( MAILADDRESS )
except:
    print 'No user with Email ' + MAILADDRESS + ' found'

print 'Activate User: '

ProfilesService.activateUserByUserId( e['PROF_GUID'], email = e['PROF_MAIL'], uid = e['PROF_UID'] )
ProfilesService.publishUserData( MAILADDRESS )
