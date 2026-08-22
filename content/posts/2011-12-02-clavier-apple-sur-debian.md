---
title: "Clavier Apple sur debian"
date: 2011-12-02T00:14:00
slug: "2011-12-02-clavier-apple-sur-debian"
author: choiz
tags: ["debian", "keyboard", "osx"]
---

Depuis le temps que je bosse avec un clavier Apple je me suis habitué au
mappage clavier Mac. Il y a beaucoup de différences entre un clavier
AZERTY de PC et un clavier AZERTY de Mac.

Les touches : @ \# ~ | (pipe) = + - \_ ! ( ) { } \[ \] sont disposées à
des endroits complètement différents.

J'ai donc décidé de modifier la configuration de debian pour prendre en
compte un clavier mac. :

    dpkg-reconfigure keyboard-console

    Select keymap from arch list

    azerty

    French

    Apple USB

    dpkg-reconfigure keyboard-configuration

    model: Apple

    layout: France - Macintosh

    Key for AltGr: No AltGr Key

    Compose key: Right Alt (AltGr)

    Use Control+Alt+Backspace to terminate the X server? no

J'ai choisi un clavier Apple, Français Mac, sans touche AltGr, avec
comme touche de fonctionnalité secondaire "Alt droit". Malheureusement
je n'ai pas réussi à mapper l'Alt de gauche pour avoir la même fonction
qu'à droite…

Et ensuite j'ai indiqué que je ne voulais pas pouvoir quitter le serveur
X avec la combinaison de touches Control+Alt+Backspace.

Si ceci ne fonctionne pas il faut se rendre dans la configuration du
clavier de votre gestionnaire de fenêtres (xfce: dans mon cas). Puis
désactiver le layout par défaut du système.

![image0](http://media.tumblr.com/tumblr_lvjsbrOL8E1qzr4hx.png)
