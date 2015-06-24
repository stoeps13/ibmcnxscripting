#!/bin/bash
#
# Author: Klaus Bild
# E-Mail: klaus.bild@webgate.biz
# Kudos to Stickfight for the SQL code: http://www.stickfight.co.uk/blog/Connections-Db-Schema-Tip1-getting-a-version
error=0
db2 CONNECT TO OPNACT > /dev/null
activity=$(db2 -x SELECT DBSCHEMAVER FROM "ACTIVITIES"."OA_SCHEMA")
db2 CONNECT RESET > /dev/null
echo "Activity Schema Version: " $activity

db2 CONNECT TO BLOGS > /dev/null
blogs=$(db2 -x "SELECT DBMS_LOB.substr(VALUE, 3000) FROM "BLOGS"."ROLLER_PROPERTIES" where NAME = 'database.schema.version'")
db2 CONNECT RESET > /dev/null
echo "Blogs Schema Version: " $blogs

db2 CONNECT TO SNCOMM > /dev/null
community=$(db2 -x SELECT DBSCHEMAVER FROM "SNCOMM"."SNCOMM_SCHEMA")
db2 CONNECT RESET > /dev/null
echo "Community Schema Version: " $community

db2 CONNECT TO SNCOMM > /dev/null
calendar=$(db2 -x SELECT DBSCHEMAVER FROM "CALENDAR"."CA_SCHEMA")
db2 CONNECT RESET > /dev/null
echo "Calendar Schema Version: " $calendar

db2 CONNECT TO DOGEAR > /dev/null
dogear=$(db2 -x SELECT DBSCHEMAVER FROM "DOGEAR"."DOGEAR_SCHEMA")
db2 CONNECT RESET > /dev/null
echo "Dogear Schema Version: " $dogear

db2 CONNECT TO FILES > /dev/null
files=$(db2 -x SELECT SCHEMA_VERSION FROM "FILES"."PRODUCT")
db2 CONNECT RESET > /dev/null
echo "Files Schema Version: " $files

db2 CONNECT TO FILES > /dev/null
push=$(db2 -x SELECT SCHEMA_VERSION FROM "PNS"."PRODUCT")
db2 CONNECT RESET > /dev/null
echo "Push Notifications Schema Version: " $push

db2 CONNECT TO FORUM > /dev/null
forum=$(db2 -x SELECT DBSCHEMAVER FROM "FORUM"."DF_SCHEMA")
db2 CONNECT RESET > /dev/null
echo "Forum Schema Version: " $forum

db2 CONNECT TO HOMEPAGE > /dev/null
homepage=$(db2 -x SELECT DBSCHEMAVER FROM "HOMEPAGE"."HOMEPAGE_SCHEMA")
db2 CONNECT RESET > /dev/null
echo "Homepage Schema Version: " $homepage

db2 CONNECT TO METRICS > /dev/null
metrics=$(db2 -x SELECT SCHEMA_VERSION FROM "METRICS"."PRODUCT")
db2 CONNECT RESET > /dev/null
echo "Metrics Schema Version: " $metrics

db2 CONNECT TO MOBILE > /dev/null
mobile=$(db2 -x "SELECT VALUE FROM "MOBILE"."ROLLER_PROPERTIES" where NAME = 'database.schema.version'")
db2 CONNECT RESET > /dev/null
echo "Mobile Schema Version: " $mobile

db2 CONNECT TO PEOPLEDB > /dev/null
profiles=$(db2 -x SELECT DBSCHEMAVER FROM "EMPINST"."SNPROF_SCHEMA")
db2 CONNECT RESET > /dev/null
echo "Profiles Schema Version: " $profiles

db2 CONNECT TO WIKIS > /dev/null
wikis=$(db2 -x SELECT SCHEMA_VERSION FROM "WIKIS"."PRODUCT")
db2 CONNECT RESET > /dev/null
echo "Wikis Schema Version: " $wikis

if [ $homepage -eq 475 ]
then
    printf "\nLooks like you have a Connections 5 BASE Installation\n\n"
    if [ $activity -ne 69 ]; then echo "Activity Schema Version is wrong:" $activity " but should be 69"; error=1; fi
    if [ $blogs -ne 69 ]; then echo "Blogs Schema Version is wrong:" $blogs " but should be 69"; error=1; fi
    if [ $community -ne 93 ]; then echo "Community Schema Version is wrong:" $community " but should be 93"; error=1; fi
    if [ $calendar -ne 29 ]; then echo "Calendar Schema Version is wrong:" $calendar " but should be 29"; error=1; fi
    if [ $dogear -ne 22 ]; then echo "Dogear Schema Version is wrong:" $dogear " but should be 2"; error=1; fi
    if [ $files -ne 107 ]; then echo "Files Schema Version is wrong:" $files " but should be 107"; error=1; fi
    if [ $push -ne 4 ]; then echo "Push Notifications Schema Version is wrong:" $push " but should be 4"; error=1; fi
    if [ $forum -ne 35 ]; then echo "Forum Schema Version is wrong:" $forum " but should be 35"; error=1; fi
    if [ $metrics -ne 38 ]; then echo "Metrics Schema Version is wrong:" $metrics " but should be 38"; error=1; fi
    if [ $mobile -ne 7 ]; then echo "Mobile Schema Version is wrong:" $mobile " but should be 7"; error=1; fi
    if [ $profiles -ne 46 ]; then echo "Profiles Schema Version is wrong:" $profiles " but should be 46"; error=1; fi
    if [ $wikis -ne 107 ]; then echo "Wikis Schema Version is wrong:" $wikis " but should be 107"; error=1; fi
elif [ $homepage -eq 477 ]
then
    printf "\nLooks like you have a Connections 5 CR1 Installation\n\n"
    if [ $activity -ne 72 ]; then echo "Activity Schema Version is wrong:" $activity " but should be 72"; error=1; fi
    if [ $blogs -ne 70 ]; then echo "Blogs Schema Version is wrong:" $blogs " but should be 70"; error=1; fi
    if [ $community -ne 93 ]; then echo "Community Schema Version is wrong:" $community " but should be 93"; error=1; fi
    if [ $calendar -ne 30 ]; then echo "Calendar Schema Version is wrong:" $calendar " but should be 30"; error=1; fi
    if [ $dogear -ne 22 ]; then echo "Dogear Schema Version is wrong:" $dogear " but should be 22"; error=1; fi
    if [ $files -ne 107 ]; then echo "Files Schema Version is wrong:" $files " but should be 107"; error=1; fi
    if [ $push -ne 6 ]; then echo "Push Notifications Schema Version is wrong:" $push " but should be 6"; error=1; fi
    if [ $forum -ne 36 ]; then echo "Forum Schema Version is wrong:" $forum " but should be 36"; error=1; fi
    if [ $metrics -ne 38 ]; then echo "Metrics Schema Version is wrong:" $metrics " but should be 38"; error=1; fi
    if [ $mobile -ne 7 ]; then echo "Mobile Schema Version is wrong:" $mobile " but should be 7"; error=1; fi
    if [ $profiles -ne 46 ]; then echo "Profiles Schema Version is wrong:" $profiles " but should be 46"; error=1; fi
    if [ $wikis -ne 107 ]; then echo "Wikis Schema Version is wrong:" $wikis " but should be 107"; error=1; fi
elif [ $homepage -eq 478 ]
then
    printf "\nLooks like you have a Connections 5 CR2 Installation\n\n"
    if [ $activity -ne 72 ]; then echo "Activity Schema Version is wrong:" $activity " but should be 72"; error=1; fi
    if [ $blogs -ne 72 ]; then echo "Blogs Schema Version is wrong:" $blogs " but should be 72"; error=1; fi
    if [ $community -ne 98 ]; then echo "Community Schema Version is wrong:" $community " but should be 98"; error=1; fi
    if [ $calendar -ne 30 ]; then echo "Calendar Schema Version is wrong:" $calendar " but should be 30"; error=1; fi
    if [ $dogear -ne 22 ]; then echo "Dogear Schema Version is wrong:" $dogear " but should be 22"; error=1; fi
    if [ $files -ne 107 ]; then echo "Files Schema Version is wrong:" $files " but should be 107"; error=1; fi
    if [ $push -ne 6 ]; then echo "Push Notifications Schema Version is wrong:" $push " but should be 6"; error=1; fi
    if [ $forum -ne 36 ]; then echo "Forum Schema Version is wrong:" $forum " but should be 36"; error=1; fi
    if [ $metrics -ne 38 ]; then echo "Metrics Schema Version is wrong:" $metrics " but should be 38"; error=1; fi
    if [ $mobile -ne 7 ]; then echo "Mobile Schema Version is wrong:" $mobile " but should be 7"; error=1; fi
    if [ $profiles -ne 46 ]; then echo "Profiles Schema Version is wrong:" $profiles " but should be 46"; error=1; fi
    if [ $wikis -ne 107 ]; then echo "Wikis Schema Version is wrong:" $wikis " but should be 107"; error=1;  fi
else
    echo "Looks like you have NOT a Connections 5 Installation"
fi
if [ $error -eq 0 ]; then printf "Perfect, all Schema Versions are matching the installed Connections Version\n\n"; fi
