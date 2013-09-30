#!/bin/bash
#
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de
# 
# ToDo: Testing new if statement, if Toolsdb is left out!

databases=$(db2 list database directory | grep alias | awk '{print $4}' | sort)

for database in ${databases[@]}
do
 if [$database != "TOOLSDB" | $database != "toolsdb"] ; then
    echo $database
    db2 "connect to $database"
    db2 -tvf automaint.sql
    db2 "connect reset"
 else
    echo "Skip $database" 
 fi
done

