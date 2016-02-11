@echo off
REM
REM Author: Klaus Bild
REM E-Mail: klaus.bild@gmail.com
REM History:    20140210   Klaus Bild           Initial Version
REM             20140408   Christoph Stoettner  Fix for caseinsensitiv findstr

REM Needed for variable expansion
SETLOCAL ENABLEDELAYEDEXPANSION
REM Set Backup-Directory, change to your environment
set DBBACKUPPATH=d:\db2\backup

REM Check System Language
FOR /F "tokens=3 delims= " %%G in ('reg query "hklm\system\controlset001\control\nls\language" /v Installlanguage') DO (
IF [%%G] EQU [0409] (
  ECHO English install language detected
  set TOKEN=3
) ELSE (
  ECHO Some other language detected
  set TOKEN=4
)

REM get all databases of db2 instance and loop through the list
FOR /F "tokens=%TOKEN% delims== " %%a IN ('DB2CMD.EXE -c -w -i DB2 list DATABASE DIRECTORY ^| findstr /i "Alias"') DO (
				set DATABASES=%%a,!DATABASES!
				title Starting database %%a backup on %date% at %time%...
				DB2CMD.EXE -c -w -i DB2 BACKUP DATABASE %%a ONLINE to %DBBACKUPPATH% INCLUDE LOGS
				)
ECHO Successfull created backups for %DATABASES% in %DBBACKUPPATH%
