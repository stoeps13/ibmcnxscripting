#!/bin/bash

export WAS_HOME=/opt/IBM/WebSphere/AppServer
export WAS_BCK_PATH=/mnt/data/wasbackup

cd $WAS_HOME/bin
if ./backupConfig.sh $WAS_BCK_PATH/websphere-config-`date +%Y%m%d-%H%M`.zip -nostop -username wasadmin -password password ; then
         echo "Backup successfully!"
         find $WAS_BCK_PATH/* -type f -mtime +3 -exec rm {} \;
else
        echo "Backup failed"
fi
