@echo off 
REM
REM Author: Christoph Stoettner
REM E-Mail: christoph.stoettner@stoeps.de
REM
REM History: 20140408 Christoph Stoettner Initial version

REM Needed for variable expansion
SETLOCAL ENABLEDELAYEDEXPANSION
REM Set Backup-Directory, change to your environment
set DBLOGPATH=D:\db2\logs
REM get all databases of db2 instance and loop through the list
FOR /F "tokens=3 delims== " %%a IN ('DB2CMD.EXE -c -w -i DB2 list DATABASE DIRECTORY ^| findstr /i "Alias"') DO (
				set DATABASES=%%a,!DATABASES!
				title Starting database %%a Log configuration on %date% at %time%... 
                REM DB2CMD.EXE -c -w -i DB2 UPDATE DATABASE CONFIGURATION FOR %%a using LOGARCHMETH1 LOGRETAIN AUTO_DEL_REC_OBJ ON num_db_backups 1 rec_his_retentn 0 logarchmeth1 disk:%DBLOGPATH%
                DB2 UPDATE DATABASE CONFIGURATION FOR %%a using logarchmeth1 disk:%DBLOGPATH%
                db2 update db cfg for %%a using AUTO_DEL_REC_OBJ ON
 		db2 update db cfg for %%a using num_db_backups 2
 		db2 update db cfg for %%a using rec_his_retentn 0
 		db2 update db cfg for %%a using LOGARCHCOMPR1 on
 		db2 update db cfg for %%a using LOGFILSIZ 8196
				)
ECHO Successfull configured logs for %DATABASES% in %DBLOGPATH%
