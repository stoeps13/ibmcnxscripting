Some scripts which can be used or called from wsadmin
-----------------------------------------------------

# changeDataSource.py

I wrote this script to set the DataSource connection pool settings as it is recommended in IBM Connections Performance Tuning Guide. 

There is only a Performance Tuning Guide for IBM Connections 4, so i have no advice to set the parameters for ccm databases.

## Call Script through wsadmin

You have to call the scripts with `-username adminuser -password yourpassword` or you get a password popup.

### Linux
Change to `WASROOT/profiles/Dmgr01/bin`

    ./wsadmin.sh -lang jython -f pathtoscript/changeDataSource.py

### Windows
Change to `WASROOT\profiles\Dmgr01\bin`

    wsadmin.bat -lang jython -f pathtoscript\changeDataSource.py

# MemberSync

* memberSyncByEmail.py  
* memberSyncByEXID.py   
* memberSyncByLogin.py

These scripts help you synchronize Users against LDAP. They all call first memberSync.py (which contains all needed ConnectionsAppAdmin.py calls) and then start to call each application memberSyncService.

You have to change the line execfile("path/memberService.py") that wsadmin can find the files!

Then call the memberSync-Scripts with:

    ./wsadmin.sh -lang jython -username admin -password password -f "path/memberSyncByXYZ.py" 'MAILADDRESS|EXID|UID'

You can use the DB2 Script `checkExID.sh` for caseSensitiv Mail and UID parts.

# Backup and Restore Security Roles

## securityrolebackup.sh (former j2eerolebackup.sh)

Loops through installed applications and stores backup to filesystem.

Script need a filepath as parameter!

    cd WAS_HOME/profiles/Dmgr01/bin

    ./wsadmin.sh -lang jython -username admin -password password -f securityrolebackup.sh "../temp"

## securityrolerestore.sh

! I didn't tested this script! Please do not use in production!

Restores roles which are saved through securityrolebackup.sh.

Script need a filepath (where Backup is stored!) as parameter!

    ./wsadmin.sh -lang jython -username admin -password password -f securityrolerestore.sh "../temp"
