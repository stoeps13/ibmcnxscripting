# To run this script with Windows or SLES, you have to modify setupCmdLine
#
# setupCmdLine.bat|sh
# add on line 40: "SET WAS_USER_SCRIPT=d:\ibm\wasuserscript.cmd"
#
# Create d:\ibm\wasuserscript.cmd:
# "SET WAS_EXT_DIRS=%WAS_EXT_DIRS%;c:\ibm\sqllib\java"
#

import os
import sys
from java.util import Properties

# Load all jython commands, when they are not loaded
try:
    test = Scheduler.listAllTasks()
    if test == '':
        raise Exception
except:
    print 'Load Connections Commands'
    execfile("loadAll.py")


# add the jar to your classpath, then import it
# better to read WebSphere variable PROFILES_JDBC_DRIVER_HOME

import com.ibm.db2.jcc.DB2Driver as Driver

# Change User and Password
props = Properties()
props.put( 'user', 'lcuser' )
props.put( 'password', 'password' )

# Change Hostname, Port and maybe DB Name
conn = Driver().connect( 'jdbc:db2://cnxdb2.stoeps.local:50000/PEOPLEDB', props )

stmt = conn.createStatement()

email = raw_input( "Mail address of profile you want to check: " ).lower()

sql = 'select PROF_UID_LOWER,PROF_MAIL_LOWER,PROF_GUID,PROF_MAIL from empinst.employee where PROF_MAIL_LOWER = \'' + email + '\' order by PROF_UID_LOWER'
rs = stmt.executeQuery( sql )

employeeList = []
while ( rs.next() ):
    row = {}
    row['PROF_UID_LOWER'] = rs.getString( 1 )
    row['PROF_MAIL_LOWER'] = rs.getString( 2 )
    row['PROF_GUID'] = rs.getString( 3 )
    row['PROF_MAIL'] = rs.getString( 4 )
    employeeList.append( row )

rs.close()
stmt.close()
conn.close()

# print the result
for e in employeeList:
    # print e['PROF_UID_LOWER'] + "\t\t" + e['PROF_MAIL_LOWER'] + "\t\t" + e['PROF_GUID']
    # print e['PROF_MAIL']
    print "Profiles:\t\t\t " + e['PROF_GUID']

LOGIN = e['PROF_MAIL']
try:
   print "Activities:\t\t\t",
   ActivitiesMemberService.getMemberExtIdByLogin( LOGIN )
except:
   print 'No user with Login ' + LOGIN + ' found'

try:
   print "Blogs:\t\t\t\t",
   BlogsMemberService.getMemberExtIdByLogin( LOGIN )
except:
   print 'No user with Login ' + LOGIN + ' found'

try:
   print "Communities:\t\t\t",
   CommunitiesMemberService.getMemberExtIdByLogin( LOGIN )
except:
   print 'No user with Login ' + LOGIN + ' found'

try:
   print "Dogear:\t\t\t\t",
   DogearMemberService.getMemberExtIdByLogin( LOGIN )
except:
   print 'No user with Login ' + LOGIN + ' found'

try:
   print "Files:\t\t\t\t",
   FilesMemberService.getMemberExtIdByLogin( LOGIN )
except:
   print 'No user with Login ' + LOGIN + ' found'

try:
   print "Forums:\t\t\t\t",
   ForumsMemberService.getMemberExtIdByLogin( LOGIN )
except:
   print 'No user with Login ' + LOGIN + ' found'

try:
   print "News, Search, Homepage:\t\t",
   NewsMemberService.getMemberExtIdByLogin( LOGIN )
except:
   print 'No user with Login ' + LOGIN + ' found'

try:
   print "Wikis:\t\t\t\t",
   WikisMemberService.getMemberExtIdByLogin( LOGIN )
except:
   print 'No user with Login ' + LOGIN + ' found'

