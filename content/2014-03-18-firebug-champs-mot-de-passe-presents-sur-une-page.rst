Firebug champs mot de passe présents sur une page non sécurisée
###############################################################
:date: 2014-03-18 10:11:00
:author: choiz
:category: text
:tags: firebug, http, https, formulaire, warning, mot de passe, password, action, form
:slug: 2014-03-18-firebug-champs-mot-de-passe-présents-sur-une-page
:status: published

Dans mon firebug des "warnings" s'affichent :

::

    Champs mot de passe présents sur une page non sécurisée (http://). Cela représente un risque de sécurité permettant le vol d'identifiants de connexion.

Ainsi que :

::

    Champs mot de passe présents dans un formulaire possédant une action de formulaire non sécurisée (http://). Cela représente un risque de sécurité permettant le vol d'identifiants de connexion.

La première indications informe que vous n'êtes pas sur un site
utilisant le HTTPS. Lorsque vous allez remplir le champs "password"
celui-ci sera envoyé en clair sur le réseau.

La seconde indication informe que l'action du formulaire envoi sur une
page qui n'est pas en HTTPS.

Vous pouvez avoir votre formulaire sur l'url :
https://www.mon-formulaire.fr et dans l'action de votre formulaire avoir
: http://www.mon-formulaire.fr

Dans ce cas l'affichage du formulaire est sécurisé, mais l'envoi des
données ne l'est pas vu que l'action est en http.

