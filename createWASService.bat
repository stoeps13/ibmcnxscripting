cd %WAS_HOME%/bin
wasservice.exe -add Dmgr -serverName dmgr -profilePath D:\IBM\WebSphere\AppServer\profiles\Dmgr01 -userid serviceaccount - password password  -encodeParams -restart true -startType automatic -stopArgs "-username wasadmin -password password"
wasservice.exe -add Node -serverName nodeagent -profilePath D:\IBM\WebSphere\AppServer\profiles\AppSrv01 -userid serviceaccount - password password -encodeParams -restart true -startType automatic -stopArgs "-username wasadmin -password password -stopservers"
