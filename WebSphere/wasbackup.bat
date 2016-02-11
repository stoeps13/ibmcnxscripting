REM Backup WebSphere configuration

set ORGPATH=%CD%
set WASUSER=wasoperator
set WASUSERPW=password
set WAS_HOME=D:\IBM\WebSphere\AppServer
set LOG=D:\Backup\Log\websphere-config.log
set WAS_BCK_PATH=D:\Backup\WebSphere
set DAY=%DATE:~0,2%
set MONTH=%DATE:~3,2%
set YEAR=%DATE:~6,4%

echo Start WebSphere Config Backup %DATE% %TIME% > %LOG%
cd %WAS_HOME%\bin
backupConfig.bat %WAS_BCK_PATH%\websphere-config-%YEAR%%MONTH%%DAY%.zip -nostop -username %WASUSER% -password %WASUSERPW% >> %LOG%
IF ERRORLEVEL 1 GOTO error
echo Backup successful >> %LOG%
GOTO end

:error
echo Error during config backup >> %LOG%

:end
echo Script completed >> %LOG%
cd %ORGPATH%
