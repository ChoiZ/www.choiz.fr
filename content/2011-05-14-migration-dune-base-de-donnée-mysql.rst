Migration d'une base de donnée Mysql
####################################
:date: 2011-05-14 13:21:17
:author: choiz
:category: text
:tags: Mysql, Mysqldump, Database, Migration, Dump Sql, Sql
:slug: 2011-05-14-migration-dune-base-de-donnée-mysql
:status: published

Pour faire mes migrations de base de donnée j'utilise en ligne de
commande mysqldump et mysql.

| Dans un premier temps je sauve ma base ***database*** dans le fichier
  ***fichierdump.sql***
| J'utilise l'utilisateur mysql : ***utilisateur*** avec son mot de
  passe ***p4ssw0rd***

    $ mysqldump -u utilisateur -p p4ssw0rd database > fichierdump.sql

Une fois que j'ai mon fichier ***fichierdump.sql*** je le met sur la
nouvelle machine. Ensuite j'execute la commande suivante :

    $ mysql -u utilisateur -pp4ssw0rd database < fichierdump.sql

