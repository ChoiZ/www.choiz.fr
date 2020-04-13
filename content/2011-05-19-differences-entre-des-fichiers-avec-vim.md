Title: Différences entre des fichiers avec Vim
Date: 2011-05-19 23:32:00
Author: choiz
Category: text
Tags: vim, diff, cli
Slug: 2011-05-19-différences-entre-des-fichiers-avec-vim
Status: published

J'ai souvent besoin de voir les différences entre plusieurs fichiers...
J'utilise souvent la commande diff dans un terminal, mais mon éditeur
texte favoris "Vim" sait aussi trés bien faire un différentiel.
Utilisation avec le terminal :

    diff fichier1 fichier2

Celui-ci retournera les différences directement dans le terminal (pas
pratique pour l'édition).

Utilisation avec vim :

    vim -d fichier1 fichier2

Ensuite il suffit d'utiliser (CTRL + W puis W) pour changer de fenêtre
(gauche à droite ou droite à gauche) ou bien en utilisant (CTRL + W puis
fléche de droite ou gauche) suivant la direction ou on veut aller.

Pour le reste des commandes reportez-vous au [guide de survie de
vi](http://matrix.samizdat.net/pratique/documentation/guide-survie-VI.html)
!
