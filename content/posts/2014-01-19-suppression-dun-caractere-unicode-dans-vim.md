---
title: "Suppression d'un caractère unicode dans Vim"
date: 2014-01-19T17:06:00
slug: "2014-01-19-suppression-dun-caractère-unicode-dans-vim"
author: choiz
tags: ["vim", "encoding"]
---

J'étais à la recherche de ce caractère unicode dans vim :

    <U+2028>

Pour pouvoir le supprimer j'ai utilisé la commande suivante :

    :%s/\%U2028//g

Décortiquons la commande :

`:%s/` Recherche et remplace dans tout le fichier

`\%U2028` Le caractère que l'on recherche unicode "2028"

`//` par rien (1er slash sépare la recherche par ce qu'on remplace, le second pour dire la fin de ce qu'on remplace).

`g` dans tout le fichier (global).
