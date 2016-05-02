Title: Export / Import avec PostgreSQL
Date: 2013-06-22 19:57:41
Author: choiz
Category: text
Tags: postgreSQL, pg\_dump, psql, import, export, dump, sql
Slug: 2013-06-22-export-import-avec-postgresql
Status: published

Pour exporter une table spécifique d'une base :

    pg_dump *mabase* --table=*matable* > *dump_base_table*.sql

Pour exporter une base :

    pg_dump *mabase* > *dump_base*.sql

Pour importer un dump dans une base :

    psql *base* < *dump_base_table*.sql
    psql *base* < *dump_base*.sql
