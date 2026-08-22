Title: Migration d'une base de données Mysql
Date: 2011-05-14 13:21:17
Author: choiz
Category: text
Tags: mysql, linux, sql
Slug: 2011-05-14-migration-dune-base-de-donnée-mysql
Status: published

Pour faire mes migrations de base de données j'utilise en ligne de
commande mysqldump et mysql.

Dans un premier temps je sauve ma base database dans le fichier dump.sql
J'utilise l'utilisateur mysql : utilisateur avec son mot de passe p4ss :

    mysqldump -u utilisateur -p p4ss database > dump.sql

Une fois que j'ai mon fichier dump.sql je le mets sur la nouvelle
machine, puis j'exécute la commande suivante :

    mysql -u utilisateur -pp4ss database < fichierdump.sql
