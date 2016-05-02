Title: Suppression d'un caractère unicode dans Vim
Date: 2014-01-19 17:06:00
Author: choiz
Category: text
Tags: vim, unicode, char, suppression, caractère
Slug: 2014-01-19-suppression-dun-caractère-unicode-dans-vim
Status: published

J'étais à la recherche de se caractère unicode dans vim :

    <U+2028>

Pour pouvoir le supprimer j'ai utilisé la commande suivante :

    :%s/\%U2028//g

Décortiquons la commande :

    `:%s/` Recherche et remplace dans tout le fichier

    `\%U2028` Le caractère que l'on recherche unicode "2028"

    `//` par rien (1er slash sépare la recherche par ce qu'on remplace, le second pour dire la fin de ce qu'on remplace).

    `g` dans tout le fichier (global).
