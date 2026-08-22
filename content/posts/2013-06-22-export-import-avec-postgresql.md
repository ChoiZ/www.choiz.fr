---
title: "Export / Import avec PostgreSQL"
date: 2013-06-22T19:57:41
slug: "2013-06-22-export-import-avec-postgresql"
author: choiz
tags: ["sql"]
---

Pour exporter une table spécifique d'une base :

    pg_dump *mabase* --table=*matable* > *dump_base_table*.sql

Pour exporter une base :

    pg_dump *mabase* > *dump_base*.sql

Pour importer un dump dans une base :

    psql *base* < *dump_base_table*.sql
    psql *base* < *dump_base*.sql
