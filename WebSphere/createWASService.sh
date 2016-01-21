#!/bin/bash
cd $WAS_HOME/bin
./wasservice.sh -add Dmgr -serverName dmgr -profilePath /opt/IBM/WebSphere/AppServer/profiles/Dmgr01 \
 -stopArgs '-username wasadmin -password password'
./wasservice.sh -add Node -serverName nodeagent -profilePath /opt/IBM/WebSphere/AppServer/profiles/AppSrv01 \
 -stopArgs '-username wasadmin -password password -stopservers'
chkconfig --levels 2345 --add Dmgr_was.init on
chkconfig --levels 2345 --add Node_was.init on
