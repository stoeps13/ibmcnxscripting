#!/bin/bash
# 
#  Start Skript as instance owner!
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de

if [ -z "$1" ]; then
	echo "USAGE: `basename $0` mailaddress"
	exit ;
fi


MAIL=$1

db2 -x "connect to peopledb" | grep alias | awk '{print $5}'
db2 -x "SELECT PROF_GUID, PROF_MAIL FROM EMPINST.EMPLOYEE WHERE PROF_MAIL_LOWER = '${MAIL,,}'"
db2 -x "connect reset" > /dev/null 
while true; do
    printf "Which email address should be used for Lookup?\n"
    read  MAIL
    break
done
db2 -x "connect to OPNACT"| grep alias | awk '{print $5}'
db2 -x "select EXID from activities.oa_memberprofile where email = '$MAIL'"
db2 -x "connect reset" > /dev/null
db2 -x "connect to BLOGS"| grep alias | awk '{print $5}'
db2 -x "select EXTID from blogs.rolleruser where EMAILADDRESS = '$MAIL'"
db2 -x "connect reset" > /dev/null
db2 -x "connect to SNCOMM"| grep alias | awk '{print $5}'
db2 -x "select DIRECTORY_UUID from SNCOMM.MEMBERPROFILE where email = '${MAIL,,}'"
db2 -x "connect reset" > /dev/null
db2 -x "connect to dogear"| grep alias | awk '{print $5}'
db2 -x "select MEMBER_ID from DOGEAR.PERSON where email = '${MAIL,,}'"
db2 -x "connect reset" > /dev/null
db2 -x "connect to files"| grep alias | awk '{print $5}'
db2 -x "select DIRECTORY_ID from FILES.USER where email = '$MAIL'"
db2 -x "connect reset" > /dev/null
db2 -x "connect to forum" | grep alias | awk '{print $5}'
db2 -x "select EXID from FORUM.DF_MEMBERPROFILE where email = '$MAIL'"
db2 -x "connect reset" > /dev/null
db2 -x "connect to Homepage"| grep alias | awk '{print $5}'
db2 -x "select EXID from HOMEPAGE.PERSON where USER_MAIL = '$MAIL'"
db2 -x "connect reset" > /dev/null
db2 -x "connect to wikis"| grep alias | awk '{print $5}'
db2 -x "select DIRECTORY_ID from WIKIS.USER where email = '$MAIL'" | grep "-"
db2 -x "connect reset" > /dev/null
