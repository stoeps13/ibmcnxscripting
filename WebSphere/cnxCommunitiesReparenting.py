# cnxCommunitiesReparenting.py
# Author: Klaus Bild
# E-Mail: klaus.bild@gmail.com
# Blog: http://kbild.ch
# Description: Move IBM Connections Communities

execfile( 'communitiesAdmin.py' )
state = ''

def checkParent( comm_id):
   resultparent = CommunitiesService.fetchAllComm()
   resultparent = str(resultparent)
   countparent = resultparent.count('parentUuid='+comm_id)
   return (countparent)

def getUUID( comm_name ):
    allComm = CommunitiesService.fetchAllComm()
    result = CommunitiesListService.filterListByName(allComm, '.*' + comm_name + '.*')
    result = str(result)
    counter = result.count('uuid=')
    index = 0
    count = 0
    if (counter<1):
        print '\n------------------------------------------------------------------'
        print 'There is NO Community with this name\nPlease try again ----------->' 
        print '------------------------------------------------------------------\n'
        return (0,0,0,0,0)
    elif (counter<2):
        comm_id = result[result.find('uuid=')+5:result.find('uuid=')+41]
        comm_name = result[result.find('name=')+5:result.find('uuid=')-2]
        acl = result[result.find('type=')+5:result.find('name=')-2]
        parent = result.find('parentUuid=')
        return (comm_id, parent, comm_name, acl, 1)       
    else:
        comm_id = []
        comm_name = []
        acl = []
        parent = []
        numberlist = []
        comm_number = -1
        print '\nThere are multiple communities with this name:'
        print '----------------------------------------------'
        while index < len(result):
            index = result.find('{', index)
            end = result.find('{', index+1)
            comm_id.append(result[result.find('uuid=', index)+5:result.find('uuid=', index)+41])
            comm_name.append(result[result.find('name=', index)+5:result.find('uuid=', index)-2])
            acl.append(result[result.find('type=', index)+5:result.find('name=', index)-2])
            parent.append(result.find('parentUuid=', index, end))
            numberlist.append(count)
            if index == -1:
                break
            print (str(count) + ': ' + comm_name[count])
            index += 1
            count += 1
        print '----------------------------------------------'
        go_on = ''
        while go_on != 'TRUE':
           comm_number = raw_input('Please type the number of the community? ')
           try:
              comm_number = float(comm_number)
           except (TypeError, ValueError):
              continue
           if count-1>=comm_number>=0:
              break
           else:
              continue
        return (comm_id[int(comm_number)], parent[int(comm_number)], comm_name[int(comm_number)], acl[int(comm_number)], 1)
        
while state != ( 'EXIT' ):
        state = raw_input( '\n--------------------------------------------------------\nPress C for moving a community, M for Menu or X for Exit \n--------------------------------------------------------\n' ).upper()
        if state == 'X':
            state = 'EXIT'
            break
        elif state == 'M':
            state = 'MENU'
            execfile( 'cnxmenu.py' )
            break
        elif state =='C':
            comm_name = raw_input('\nWildcard ist automatically added, just enter part of the name but the search is CASE sensitive!\nWhat is the name of the community which you want to move? ')
            comm_id, parent, comm_fullname, acl, noresult = getUUID(comm_name)
            if noresult == 0:
                continue
            if parent > 0:
                decision = raw_input('\nDo you really want to move the subcommunity ' + comm_fullname + ' (y/n) ? ')
                if decision == 'y':
                    CommunitiesService.moveSubcommunityToCommunity(comm_id)
                    print '------------------------------------------------------\n'
                    print '\nSUCCESSFUL MOVED COMMUNITY ' + comm_fullname + '\n'
                    print '------------------------------------------------------\n'
                    continue
                else:
                    print '------------------------------------------------------\n'
                    print '\nCommunity ' + comm_fullname + ' was NOT moved\n'
                    print '------------------------------------------------------\n'
                    continue
            else:
                goBack = ''
                while goBack != ( 'TRUE' ):
                    if checkParent(comm_id)==1:
                       print '\n----------------------------------------------------\nThis community has a subcommunity and can\'t be moved\n----------------------------------------------------\n'
                       break
                    comm_name_parent = raw_input('\nWhat is the name of the community which should be the parent? ')
                    comm_id_parent, parent2, comm_full_name_parent, acl_parent, state = getUUID( comm_name_parent )
                    if state == 0:
                        continue
                    if parent2 > 0:
                        print '\n' + comm_name_parent + ' is already a subcommunity, please use a Community which is NOT a subcommunity\n'
                        continue
                    else:
                        print "\nPlease be aware that:"
                        print '\n--------------------------------------------------------------------------------'
                        print "- Any Invited users on the subcommunity are removed"
                        print "- Community owners in the parent are copied to the new subcommunity as owners"
                        print "- Subcommunity members and owners are copied to the new parent as members"
                        print "- Subcommunity access levels will be at least equal restrictive than from parent"
                        print '\n--------------------------------------------------------------------------------'
                        if (acl_parent=='publicInviteOnly' and acl=='public'):
                            print '\nThe parent Community has MODERATED access, \nthe new subcommunity "' + comm_fullname + '" will have MODERATED access as well'
                        elif (acl_parent=='private' and acl=='public') or (acl_parent=='private' and acl=='publicInviteOnly'):
                            print '\nThe parent Community has only PRIVATE access, the new subcommunity ' + comm_fullname + ' will have PRIVATE access as well'
                        decision = raw_input('\nDo you really want to move the subcommunity ' + comm_fullname + ' into ' + comm_full_name_parent + ' (y/n) ? ')
                        
                        if decision == 'y':
                            CommunitiesService.moveCommunityToSubcommunity(comm_id_parent, comm_id)
                            goBack = 'TRUE'
                            print '-------------------------------------------------------\n'
                            print '\nSUCCESSFUL MOVED COMMUNITY ' + comm_fullname + '\n'
                            print '-------------------------------------------------------\n'
                        else:
                            print '\nCommunity ' + comm_fullname + ' was NOT moved\n'
                    continue            
        else:
            continue