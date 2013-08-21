#!/bin/bash
#
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de

databases=$(db2 list database directory | grep alias | awk '{print $4}' | sort)

for database in ${databases[@]}
do
 echo $database
 db2 "connect to $database"
 db2 -tvf automaint.sql
 db2 "connect reset"
done

