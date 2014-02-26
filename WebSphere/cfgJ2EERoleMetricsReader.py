# cfgJ2EERoleGlobalModerator
#
# Author: Christoph Stoettner
# Blog: http://www.stoeps.de
# E-Mail: nospam@stoeps.de
#
# Description:
# Script is tested with IBM Connections 4.5 CR2, CR3
#
# You can enable and disable Metrics Reader through J2EE Roles with this script

# History:
# 20140225  Christoph Stoettner     Initial Version

# import ibmcnxscript

def setJ2EERole(appName,role_auth,role_users,role_groups):
    AdminApp.edit( appName, '[-MapRolesToUsers [["metrics-reader" ' + role_auth + ' "' + role_users + '" "' + role_groups + '" ]]]' )
        
def printMenu():
    state = ''
    while state != ( 'ENABLE' or 'DISABLE' or 'EXIT' ):
        state = raw_input( 'Do you want to enable or disable Metrics? (E|D|X)(ENABLE|DISABLE|EXIT)' ).upper()
        if state == 'E':
            state = 'ENABLE'
            break
        elif state == 'D':
            state = 'DISABLE'
            break
        elif state == 'X':
            state = 'EXIT'
            break
        else:
            continue
            
    if state == 'ENABLE':
        print 'Enable metrics-reader'
        auth = ''
        while auth != ( 'Y' or 'YES' or 'N' or 'NO'):
            auth = raw_input('Enable metrics-reader Role for \"All-Authenticated in Realm\"? (Y|N)(YES|NO)').upper()
            if auth == 'Y':
                role_auth = 'No Yes'
            else:
                role_auth = 'No No'
        role_users = raw_input('Enable metrics-reader Role for single Users? (Type casesensitiv uid, empty for none, multiple uids seperate by \"|\")')
        role_groups = raw_input('Enable metrics-reader Role for a Group? (Type casesensitiv Groupname, empty for no groups, multiple Groups seperated by \"|\")')
             
    elif state == 'DISABLE':
        print 'Disable metrics-reader'   
        role_auth='No No'
        role_users=''
        role_groups=''
        
    apps = ['Activities','Blogs','Communities','Dogear','Files','Forums','Homepage','News','Profiles','Search','WidgetContainer','Wikis']    
    for app in apps:     
        print "Setting Role for " + app
        setJ2EERole(app,role_auth,role_users,role_groups)
    
    AdminConfig.save()       
    

printMenu()
