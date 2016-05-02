Title: Insérer un \# au début de chaque ligne d'un fichier avec vim
Date: 2011-10-05 00:42:00
Author: choiz
Category: text
Tags: Vim, search, replace, line, add, ligne, fichier, file, remplace, ajout
Slug: 2011-10-05-insérer-un-au-début-de-chaque-ligne-dun-fichier
Status: published

Voilà la commande pour ajouter un \# au début de chaque ligne d'un
fichier avec vim :

    :1,$s/^/#/

Explications :

:1,$ Sélection des ligne 1 à $ ($ étant la dernière).

s/^/\#/ s pour search ^ indique le début de ligne / sépare ma recherche
par ce que l'on remplace \# est le caractère que je veux remplacer
