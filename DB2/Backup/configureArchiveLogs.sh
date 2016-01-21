# Path to archive Logs
archLogs=/opt/db2archivelogs

# get all databases of db2 instance
databases=$(db2 list database directory | grep alias | awk '{print $4}' | sort)

# Loop through list of databases:
for database in ${databases[@]}
do
 echo $database
 db2 update db cfg for $database using LOGARCHMETH1 disk:$archLogs
 db2 update db cfg for $database using AUTO_DEL_REC_OBJ ON
 db2 update db cfg for $database using num_db_backups 2
 db2 update db cfg for $database using rec_his_retentn 0
 db2 update db cfg for $database using LOGARCHCOMPR1 on
 db2 update db cfg for $database using LOGFILSIZ 8196
done

