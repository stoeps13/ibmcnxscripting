@echo off 
REM
REM Author: Klaus Bild
REM E-Mail: klaus.bild@gmail.com

REM Needed for variable expansion
SETLOCAL ENABLEDELAYEDEXPANSION
REM Set Backup-Directory, change to your environment
set DBBACKUPPATH=E:\Transfer
REM get all databases of db2 instance and loop through the list
FOR /F "tokens=5" %%a IN ('DB2CMD.EXE -c -w -i DB2 list DATABASE DIRECTORY ^| findstr "Alias"') DO (
				set DATABASES=%%a,!DATABASES!
				title Starting database %%a backup on %date% at %time%... 
				DB2CMD.EXE -c -w -i DB2 BACKUP DATABASE %%a to %DBBACKUPPATH% COMPRESS
				)
ECHO Successfull created backups for %DATABASES% in %DBBACKUPPATH%a
