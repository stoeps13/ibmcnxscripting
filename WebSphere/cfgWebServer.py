# cfgWebServer.py
# Author: Klaus Bild
# E-Mail: klaus.bild@gmail.com
# Blog: http://kbild.ch
# Description: Add webserver to all app/modules

nodes = AdminTask.listNodes().splitlines()
for node in nodes:
 webservers = AdminTask.listServers('[-serverType WEB_SERVER -nodeName ' + node + ']').splitlines()
 for webserver in webservers:
  srv = webserver.split( '/' )
  cell = srv[1]
  node = srv[3]
  webserverName = AdminConfig.showAttribute(webserver, 'name')
  fullWebServerName="WebSphere:cell=" + cell + ",node=" + node + ",server=" + webserverName

def getServerList( app, webserver):
   addServer="NEW"
   addedServers=""
   mapServers=AdminApp.view('Activities', '-MapModulesToServers').splitlines()
   for mapServer in mapServers:
     servers=mapServer.splitlines()
     for server in servers:
       if not server.find("Server:") == -1:
         if  addedServers.find(addServer) == -1:
           addedServers+="+" + server[9:]
         addServer=server[9:]
   if addedServers.find(webserver) == -1:
     addedServers+="+" + webserver
   return addedServers[1:]


def getCommand ( app):
   addServers=getServerList(app, fullWebServerName)

   module_ids = AdminApp.listModules(app).splitlines()
   command = "AdminApp.edit(app, '[ -MapModulesToServers ["
   for module_id in module_ids:
     start = module_id.find('#')
     module_id = module_id[start+1:].replace("+", ",")
     endpoint = AdminApp.view(app).find(module_id)
     startpoint = AdminApp.view(app).rfind('Module:', 0, endpoint)
     module_name = AdminApp.view(app)[startpoint+9:endpoint-8]
     module_name = '"' + module_name + '"'
     command += "[ " + module_name + " " + module_id + " " + addServers + " ]"
   command += "]]' )"
   return command

apps = AdminApp.list().splitlines()
for app in apps:
  exec getCommand(app)

AdminConfig.save()
