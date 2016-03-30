Pour faire mes migrations de base de donnée j'utilise en ligne de
commande mysqldump et mysql.

Dans un premier temps je sauve ma base database dans le fichier dump.sql
J'utilise l'utilisateur mysql : utilisateur avec son mot de passe p4ss :

    mysqldump -u utilisateur -p p4ss database > dump.sql

Une fois que j'ai mon fichier dump.sql je le met sur la nouvelle
machine, puis j'execute la commande suivante : :

    mysql -u utilisateur -pp4ss database < fichierdump.sql
