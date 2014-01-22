#!/bin/bash
# Script for IBM Connections Database reorganisation
#
# copy this script in the path of your instance owner (db2inst1)
# e.g. /home/db2inst1
#
# Go to the Wizards-folder/connections.sql/
# and call the script
#
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de
#
# line end with @
for db in activities blogs cognos communities dogear files forum libraries.gcd libraries.os metrics mobile wikis ; do
	db2 -td@ -vf $db/db2/reorg.sql
done
# homepage and profiles use ; for line end
for db in homepage profiles ; do
	db2 -tvf $db/db2/reorg.sql
done
