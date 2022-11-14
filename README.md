# sphixsearch_exceptions
Sphinxsearch Exceptions Editor

This is a small web app to manage, easily than a text editor, and find new exception to handle.

To install:
python3 -m venv venv
. ./venv/bin/activate
pip3 install flask flask_mysqldb


Edit settings.py file with you mysql account:
```
MYSQL_HOST = '127.0.0.1'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'mySecretPWD'
MYSQL_DB = 'myDB'
MYSQL_QUERY='''select distinct REGEXP_SUBSTR(title,'{#pattern#}') from mytable where title like '%{#searchString#}%' limit 100'''
exceptionFile='exceptions.txt'
```

In MYSQL_QUERY {#pattern#} will be replaced by the regexp passed by the app, and {#searchString#} will be replaced by query term you're looking
For regexp instruction read https://dev.mysql.com/doc/refman/8.0/en/regexp.html

API Endpoint      Methods  Rule
----------------  -------  -----------------------
deleteBase        GET      /api/delete/<base>
isUnpublished     GET      /api/published
list              GET      /api/list
publish           GET      /api/publish
reload            GET      /api/reload
reloadExceptions  GET      /api/reload
save              POST     /api/view
search            POST     /api/search

APP Endpoint      Methods  Rule
----------------  -------  -----------------------
root              GET      /
add               GET      /add
addKey            GET      /add/<key>
searchException   GET      /search
static            GET      /static/<path:filename>
tmpSave           GET      /save
view              GET      /api/view/<base>
