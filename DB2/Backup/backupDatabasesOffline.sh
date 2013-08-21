#!/bin/bash
#
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de

databases=$(db2 list database directory | grep alias | awk '{print $4}' | sort)

for database in ${databases[@]}
do
 echo $database
 db2 backup database $database to /opt/db2backup COMPRESS
done

