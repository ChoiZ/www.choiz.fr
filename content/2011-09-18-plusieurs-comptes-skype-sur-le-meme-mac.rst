Plusieurs comptes Skype sur le même Mac !
#########################################
:date: 2011-09-18 23:47:53
:author: choiz
:category: text
:tags: Skype, Multiutilisateur, Mac, MacOs, Mac os x, OsX, Skype Mac, Multi, Compte, Another copy, Another copy of Skype
:slug: 2011-09-18-plusieurs-comptes-skype-sur-le-même-mac
:status: published

Comment lancer plusieurs comptes Skype avec le même Mac ?

|image0|

Créer un compte utilisateur dans les préférences systèmes > utilisateurs. Par
exemple l'utilisateur : "skype" avec comme mot de passe "password".
Ensuite ouvrir un terminal (dans spotlight tapez terminal).
Puis : ::

    su skype (ou "su nomdutilisateur" en fonction de l'utilisateur créé).

    Password:

    password (ou autre suivant le mot de passe de l'utilisateur).

Puis : ::

    /Applications/Skype.app/Contents/MacOS/Skype

Ce qui devrait lancer une seconde instance de Skype.

.. |image0| image:: http://media.tumblr.com/tumblr_lrqn73WCUg1qzr4hx.png
