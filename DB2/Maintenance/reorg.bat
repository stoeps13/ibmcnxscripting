# Script for IBM Connections Database reorganisation
#
# copy this script to the Connections_Install/connections.sql/
# and call the script
#
# Author: Klaus Bild
# E-Mail: klaus.bild@gmail.com
#
FOR /f %%a IN ('dir /b/s reorg.sql') DO (
	echo %%a
	ECHO.%%a|findstr "profiles homepage" >nul&IF ERRORLEVEL 1 (DB2CMD.EXE -c -w -i db2 -td@ -vf %%a) ELSE (DB2CMD.EXE -c -w -i db2 -tvf %%a)
)
