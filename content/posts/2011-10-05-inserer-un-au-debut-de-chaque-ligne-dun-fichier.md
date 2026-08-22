---
title: "Insérer un # au début de chaque ligne d'un fichier avec vim"
date: 2011-10-05T00:42:00
slug: "2011-10-05-insérer-un-au-début-de-chaque-ligne-dun-fichier"
author: choiz
tags: ["vim", "comments"]
---

Voilà la commande pour ajouter un \# au début de chaque ligne d'un
fichier avec vim :

    :1,$s/^/#/

Explications :

`:1,$` : Sélection des lignes 1 à $ ($ étant la dernière).

`s/^/\#/` : `s` pour search, `^` indique le début de ligne, `/` est un
séparateur pour la recherche et pour ce que l'on souhaite remplacer et `\#`
est le caractère de remplacement.

Je remplace donc le début de ligne par un \#.
