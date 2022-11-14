MYSQL_HOST = '127.0.0.1'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'mySecretPWD'
MYSQL_DB = 'myDB'
## USE {#pattern#} for the regexp and {#searchString#} for the search 
MYSQL_QUERY='''select distinct REGEXP_SUBSTR(title,'{#pattern#}') from mytable where title like '%{#searchString#}%' limit 100'''
#exceptionFile='/home/sphinxsearch/etc/exceptions.txt'
exceptionFile='exceptions.txt'