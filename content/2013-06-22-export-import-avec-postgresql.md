Pour exporter une table spécifique d'une base : :

    pg_dump *mabase* --table=*matable* > *dump_base_table*.sql

Pour exporter une base : :

    pg_dump *mabase* > *dump_base*.sql

Pour importer un dump dans une base : :

    psql *base* < *dump_base_table*.sql
    psql *base* < *dump_base*.sql
