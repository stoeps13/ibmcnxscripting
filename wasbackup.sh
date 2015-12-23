#!/bin/bash

export WAS_HOME=/opt/IBM/WebSphere/AppServer
export WAS_BCK_PATH=/mnt/data/wasbackup

cd $WAS_HOME/bin
./backupConfig.sh $WAS_BCK_PATH/websphere-config-`date +%Y%m%d`.zip -nostop -username wasadmin -password password
