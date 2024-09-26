@echo off

set "Ymd=%date:~,4%%date:~5,2%%date:~8,2%"

if not exist "D:\db_backup" (
    mkdir "D:\db_backup"
)

rem suppose the mysql is in the following location
"C:\Program Files\MySQL\MySQL Workbench 8.0\mysqldump" -u root -p 123456 retail > "D:\db_backup\retail_%Ymd%.sql"

@echo on