#!/bin/bash
# Script for IBM Connections remove scheduler
#
# copy this script in the path of your instance owner (db2inst1)
# e.g. /home/db2inst1
#
# Go to the Wizards-Directory/connections.sql/
# and call the script
#
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de
#
for db in activities blogs cognos communities dogear files forum libraries.gcd libraries.os metrics mobild wikis ; do
	db2 -td@ -vf $db/db2/clearScheduler.sql
done
for db in homepage profiles ; do
	db2 -tvf $db/db2/clearScheduler.sql
done
