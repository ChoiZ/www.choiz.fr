Export / Import avec PostgreSQL
###############################
:date: 2013-06-22 19:57:41
:author: choiz
:category: text
:tags: postgreSQL, pg_dump, psql, import, export, dump, sql
:slug: 2013-06-22-export-import-avec-postgresql
:status: published

Pour exporter une table spécifique d'une base :

    pg\_dump *mabase* --table=*matable* > *dump\_base\_table*.sql

Pour exporter une base :

    pg\_dump *mabase* > *dump\_base*.sql

Pour importer un dump dans une base :

    psql *base* < *dump\_base\_table*.sql

    psql *base* < *dump\_base*.sql

