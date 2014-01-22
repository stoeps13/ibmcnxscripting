# Path to archive Logs
archLogs=/opt/db2archivelogs

# get all databases of db2 instance
databases=$(db2 list database directory | grep alias | awk '{print $4}' | sort)

# Loop through list of databases:
for database in ${databases[@]}
do
 echo $database
db2 update database configuration for $database using LOGARCHMETH1 LOGRETAIN AUTO_DEL_REC_OBJ ON num_db_backups 1 rec_his_retentn 0 logarchmeth1 disk:$archLogs
done

