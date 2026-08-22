---
title: "Différences entre des fichiers avec Vim"
date: 2011-05-19T23:32:00
slug: "2011-05-19-différences-entre-des-fichiers-avec-vim"
author: choiz
tags: ["vim", "diff", "cli"]
---

J'ai souvent besoin de voir les différences entre plusieurs fichiers...
J'utilise souvent la commande diff dans un terminal, mais mon éditeur
texte favori "Vim" sait aussi très bien faire un différentiel.
Utilisation avec le terminal :

    diff fichier1 fichier2

Celui-ci retournera les différences directement dans le terminal (pas
pratique pour l'édition).

Utilisation avec vim :

    vim -d fichier1 fichier2

Ensuite il suffit d'utiliser (CTRL + W puis W) pour changer de fenêtre
(gauche à droite ou droite à gauche) ou bien en utilisant (CTRL + W puis
flèche de droite ou gauche) suivant la direction où on veut aller.

Pour le reste des commandes reportez-vous au [guide de survie de
vi](http://matrix.samizdat.net/pratique/documentation/guide-survie-VI.html)
!
