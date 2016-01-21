#!/bin/bash

# Create a configuration backup of WebSphere Application Server

WASUSER=wasadmin
WASUSERPW=password
# Change to your WebSphere Root Folder
export WAS_HOME=/opt/IBM/WebSphere/AppServer
# Path to store backup
export WAS_BCK_PATH=/mnt/data/wasbackup

cd $WAS_HOME/bin
if ./backupConfig.sh $WAS_BCK_PATH/websphere-config-`date +%Y%m%d-%H%M`.zip -nostop -username $WASUSER -password $WASUSERPW ; then
         echo "Backup successfully!"
         find $WAS_BCK_PATH/websphere-config-* -type f -mtime +3 -exec rm {} \;
else
        echo "Backup failed"
fi
