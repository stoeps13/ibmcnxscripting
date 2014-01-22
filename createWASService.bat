cd %WAS_HOME%/bin
wasservice.bat -add Dmgr -serverName dmgr -profilePath D:\IBM\WebSphere\AppServer\profiles\Dmgr01 -encodeParams -restart true -startType automatic -stopArgs “-username wasadmin -password password”
wasservice.bat -add Node -serverName nodeagent -profilePath D:\IBM\WebSphere\AppServer\profiles\AppSrv01 -encodeParams -restart true -startType automatic -stopArgs '-username wasadmin -password password -stopservers'
