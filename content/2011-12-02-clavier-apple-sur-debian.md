Title: Clavier Apple sur debian
Date: 2011-12-02 00:14:00
Author: choiz
Category: text
Tags: debian, keyboard, osx
Slug: 2011-12-02-clavier-apple-sur-debian
Status: published

Depuis le temps que je bosse avec un clavier Apple je me suis habitué au
mapage clavier Mac. Il y a beaucoup de différences entre un clavier
AZERTY de PC et un clavier AZERTY de Mac.

Les touches : @ \# ~ | (pipe) = + - \_ ! ( ) { } \[ \] sont disposées à
des endroits complétement différents.

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
je n'ai pas réussi a mapper l'Alt de gauche pour avoir la même fonction
qu'à droite…

Et ensuite j'ai indiqué que je ne voulais pas pouvoir quitter le server
X avec la combinaison de touche Control+Alt+Backspace.

Si ceci ne fonctionne pas il faut se rendre dans la configuration du
clavier de votre gestionnaire de fenêtre (xfce: dans mon cas). Puis
désactiver le layout par defaut du système.

![image0](http://media.tumblr.com/tumblr_lvjsbrOL8E1qzr4hx.png)
