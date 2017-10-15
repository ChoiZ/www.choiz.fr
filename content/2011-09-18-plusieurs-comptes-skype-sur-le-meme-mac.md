Title: Plusieurs comptes Skype sur le même Mac !
Date: 2011-09-18 23:47:53
Author: choiz
Category: text
Tags: Skype, MacOs
Slug: 2011-09-18-plusieurs-comptes-skype-sur-le-même-mac
Status: published

Comment lancer plusieurs comptes Skype avec le même Mac ?

![image0](http://media.tumblr.com/tumblr_lrqn73WCUg1qzr4hx.png)

Créer un compte utilisateur dans les préférences systèmes &gt;
utilisateurs. Par exemple l'utilisateur : "skype" avec comme mot de
passe "password". Ensuite ouvrir un terminal (dans spotlight tapez
terminal). Puis :

    su skype (ou "su nomdutilisateur" en fonction de l'utilisateur créé).

    Password:

    password (ou autre suivant le mot de passe de l'utilisateur).

Puis :

    /Applications/Skype.app/Contents/MacOS/Skype

Ce qui devrait lancer une seconde instance de Skype.
