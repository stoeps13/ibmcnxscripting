#!/bin/bash
# Script for IBM Connections Database reorganisation
#
# copy this script in the path of your instance owner (db2inst1)
# e.g. /home/db2inst1
#
# Go to the Connections_install/connections.sql/
# and call the script
#
# Connections_install/connections.sql only work when your db2 is installed on your
# connections / websphere host. You can copy the folder or use the Connections_Wizard
# directory instead
#
# Author: Christoph Stoettner, Klaus Bild
# E-Mail: christoph.stoettner@stoeps.de, klaus.bild@gmail.com
#
# line end with @
find . -name "reorg.sql" -print0 | while read -d $'\0' file
do
   if grep -q 'homepage\|profiles' <<<$file; then
      db2 -tvf $file
   else
      db2 -td@ -vf $file
   fi
done