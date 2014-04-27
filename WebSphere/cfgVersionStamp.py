# cfgVersionStamp.py
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de
#
# History: 
# 20140415  Christoph Stoettner     Initial Version

print "\nSet Version Stamp in LotusConnections-config.xml to actual Date and Time\n"

path = raw_input( "Path and Folder where config is temporarily stored: " )

execfile("connectionsConfig.py")
LCConfigService.checkOutConfig(path,AdminControl.getCell())
LCConfigService.updateConfig("versionStamp","")
LCConfigService.checkInConfig(path,AdminControl.getCell())
synchAllNodes()
