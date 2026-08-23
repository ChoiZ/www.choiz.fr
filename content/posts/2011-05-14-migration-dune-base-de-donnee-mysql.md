---
title: "Migration d'une base de données Mysql"
date: 2011-05-14T13:21:17
slug: "2011-05-14-migration-dune-base-de-donnée-mysql"
author: choiz
tags: ["mysql", "linux", "sql"]
---

Pour faire mes migrations de base de données j'utilise en ligne de
commande mysqldump et mysql.

Dans un premier temps je sauve ma base database dans le fichier dump.sql
J'utilise l'utilisateur mysql : utilisateur avec son mot de passe p4ss :

    mysqldump -u utilisateur -p database > dump.sql

> ⚠️ À ne pas reproduire : ne mettez jamais le mot de passe en argument de la commande (visible dans l'historique du shell et dans `ps aux`) ; d'ailleurs `-p p4ss` avec un espace ne le passe même pas, p4ss serait lu comme nom de base. Laissez `-p` seul pour le prompt interactif, ou utilisez un `~/.my.cnf` en 600.

Une fois que j'ai mon fichier dump.sql je le mets sur la nouvelle
machine, puis j'exécute la commande suivante :

    mysql -u utilisateur -pp4ss database < fichierdump.sql
