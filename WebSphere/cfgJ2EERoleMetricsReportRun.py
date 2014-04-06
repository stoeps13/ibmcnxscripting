# cfgJ2EERoleGlobalModerator
#
# Author: Christoph Stoettner
# Blog: http://www.stoeps.de
# E-Mail: nospam@stoeps.de
#
# Description:
# Script is tested with IBM Connections 4.5 CR2, CR3
#
# You can enable and disable Metrics Report Run through J2EE Roles with this script

# History:
# 20140225  Christoph Stoettner     Initial Version
# 20140406  Christoph Stoettner     Bug Fixing Line 36 - 44

def printMenu():
    state = ''
    while state != ( 'ENABLE' or 'DISABLE' or 'EXIT' ):
        state = raw_input( 'Do you want to enable or disable Metrics-report-run? (E|D|X)(ENABLE|DISABLE|EXIT)' ).upper()
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
        print 'Enable metrics-report-run'
        auth = ''
        while auth != ( 'Y' or 'YES' or 'N' or 'NO'):
            auth = raw_input('Enable metrics-report-run Role for \"All-Authenticated in Realm\"? (Y|N)(YES|NO)').upper()
            if auth == 'Y':
                role_auth = 'No Yes'
                break
            elif auth =='N':
                role_auth = 'No No'
                break
            else:
                continue
        role_users = raw_input('Enable metrics-report-run Role for single Users? (Type casesensitiv uid, empty for none, multiple uids seperate by \"|\")')
        role_groups = raw_input('Enable metrics-report-run Role for a Group? (Type casesensitiv Groupname, empty for no groups, multiple Groups seperated by \"|\")')

    elif state == 'DISABLE':
        print 'Disable metrics-report-run and community-metrics-run'
        role_auth='No No'
        role_users=''
        role_groups=''

    if state != 'EXIT':
        apps = ['Communities']
        roleName = 'community-metrics-run'
        for app in apps:
            print "Setting Role for " + app
            AdminApp.edit( app, '[-MapRolesToUsers [["' + roleName + '" ' + role_auth + ' "' + role_users + '" "' + role_groups + '" ]]]' )

        apps = ['Common','Metrics']
        roleName = 'metrics-report-run'
        for app in apps:
            print "Setting Role for " + app
            AdminApp.edit( app, '[-MapRolesToUsers [["' + roleName + '" ' + role_auth + ' "' + role_users + '" "' + role_groups + '" ]]]' )

        AdminConfig.save()


printMenu()
