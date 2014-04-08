@echo off 
REM
REM Author: Klaus Bild
REM E-Mail: klaus.bild@gmail.com
REM History:    20140210   Klaus Bild           Initial Version
                20140408   Christoph Stoettner  Fix for caseinsensitiv findstr
                
REM Needed for variable expansion
SETLOCAL ENABLEDELAYEDEXPANSION
REM Set Backup-Directory, change to your environment
set DBBACKUPPATH=d:\db2\backup
REM get all databases of db2 instance and loop through the list
FOR /F "tokens=3 delims== " %%a IN ('DB2CMD.EXE -c -w -i DB2 list DATABASE DIRECTORY ^| findstr /i "Alias"') DO (
				set DATABASES=%%a,!DATABASES!
				title Starting database %%a backup on %date% at %time%... 
				DB2CMD.EXE -c -w -i DB2 BACKUP DATABASE %%a ONLINE to %DBBACKUPPATH% COMPRESS INCLUDE LOGS
				)
ECHO Successfull created backups for %DATABASES% in %DBBACKUPPATH%
