#!/bin/bash
#
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de

# Set Backup-Directory, change to your environment
export DBBACKUPPATH=/opt/db2backup
# get all databases of db2 instance
databases=$(db2 list database directory | grep alias | awk '{print $4}' | sort)

# Loop through list of databases:
for database in ${databases[@]}
do
 echo $database
db2 backup database $database to $DBBACKUPPATH
done
