#!/bin/bash
# Script for IBM Connections Database reorganisation
#
# copy this script in the path of your instance owner (db2inst1)
# e.g. /home/db2inst1
#
# Go to the Connections_Install/connections.sql/
# and call the script
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