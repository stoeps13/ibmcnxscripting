# checkVariables.py
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de

# Get a list of all servers in WAS cell (dmgr, nodeagents, AppServer, webserver)
servers = AdminTask.listServers().splitlines()
# Get a list of all webservers
webservers = AdminTask.listServers( '[-serverType WEB_SERVER]' ).splitlines()

# Remove webserver from servers list
for webserver in webservers:
    servers.remove( webserver )

cell = AdminControl.getCell()

varMap = AdminConfig.list( "VariableMap" ).split()
varMap.sort()

for varlist in varMap:
    scope = str( varlist.split( '|' )[0].split( '(' )[1] )
    vars = AdminConfig.list( 'VariableSubstitutionEntry', varlist ).splitlines()
    if vars:
        print ''
        print 'SCOPE: ' + scope

    del dict
    dict = {}

    for var in vars:
        name = AdminConfig.showAttribute( var, 'symbolicName' )
        value = AdminConfig.showAttribute( var, 'value' )

        dict.update( {name : value} )

    variableList = dict.keys()
    variableList.sort()

    for variable in variableList:
        if len( variable ) > 28:
            tab = "\t"
        elif len( variable ) > 23:
            tab = "\t\t"
        elif len( variable ) > 15:
            tab = "\t\t\t"
        elif len( variable ) >= 8:
            tab = "\t\t\t\t"
        else:
            tab = "\t\t\t\t\t"

        print '\t' + str( variable ) + tab + str( dict[variable] )
