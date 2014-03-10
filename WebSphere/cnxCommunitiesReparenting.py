# cnxCommunitiesReparenting.py
# Author: Klaus Bild
# E-Mail: klaus.bild@gmail.com
# Blog: http://kbild.ch
# Description: Move IBM Connections Communities

execfile( 'communitiesAdmin.py' )
state = ''

def getUUID( comm_name ):
    allComm = CommunitiesService.fetchAllComm()
    result = CommunitiesListService.filterListByName(allComm, comm_name)
    if not result:
        print 'There is NO Community with this name\nPlease try again ----------->'
        return (0,0,0)
    else:
        comm_id = str(result)[str(result).find('uuid=')+5:str(result).find('uuid=')+41]
        parent = str(result).find('parentUuid=')
        return (comm_id, parent, 1)

while state != ( 'EXIT' ):
        state = raw_input( '\nPress C for moving a community, M for Menu or X for Exit \n' ).upper()
        if state == 'X':
            state = 'EXIT'
            break
        elif state == 'M':
            state = 'MENU'
            execfile( 'cnxmenu.py' )
            break
        elif state =='C':
            comm_name = raw_input('What is the name of the community which you want to move? ')
            comm_id, parent, noresult = getUUID(comm_name)
            if noresult == 0:
                continue
            if parent > 0:
                decision = raw_input('\nDo you really want to move the subcommunity ' + comm_name + ' (y) ? ')
                if decision == 'y':
                    CommunitiesService.moveSubcommunityToCommunity(comm_id)
                    print '\nSuccessful moved Community ' + comm_name + '\n'
                    continue
                else:
                    print '\nCommunity ' + comm_name + ' was NOT moved\n'
                    continue
            else:
                goBack = ''
                while goBack != ( 'TRUE' ):
                    comm_name_parent = raw_input('\nWhat is the name of the community which should be the parent? ')
                    comm_id_parent, parent2, state = getUUID( comm_name_parent )
                    if state == 0:
                        continue
                    if parent2 > 0:
                        print '\n' + comm_name_parent + ' is already a subcommunity, please use a Community which is NOT a subcommunity\n'
                        continue
                    else:
                        decision = raw_input('\nDo you really want to move the subcommunity ' + comm_name + ' into ' + comm_name_parent + ' (y) ? ')

                        if decision == 'y':
                            CommunitiesService.moveCommunityToSubcommunity(comm_id_parent, comm_id)
                            goBack = 'TRUE'
                            print '\nSuccessful moved Community ' + comm_name + '\n'
                        else:
                            print '\nCommunity ' + comm_name + ' was NOT moved\n'
                    continue
        else:
            continue
