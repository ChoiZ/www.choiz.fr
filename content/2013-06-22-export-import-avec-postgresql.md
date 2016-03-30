Export / Import avec PostgreSQL
===============================

date  
2013-06-22 19:57:41

author  
choiz

category  
text

tags  
postgreSQL, pg\_dump, psql, import, export, dump, sql

slug  
2013-06-22-export-import-avec-postgresql

status  
published

Pour exporter une table spécifique d'une base : :

    pg_dump *mabase* --table=*matable* > *dump_base_table*.sql

Pour exporter une base : :

    pg_dump *mabase* > *dump_base*.sql

Pour importer un dump dans une base : :

    psql *base* < *dump_base_table*.sql
    psql *base* < *dump_base*.sql
