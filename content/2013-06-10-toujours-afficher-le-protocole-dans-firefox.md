Title: Toujours afficher le protocole dans Firefox
Date: 2013-06-10 14:22:00
Author: choiz
Category: text
Tags: firefox, config, http, urlbar, browser
Slug: 2013-06-10-toujours-afficher-le-protocole-dans-firefox
Status: published

Souvent lorsque je copie/colle une url depuis firefox j'ajoute <http://>
or lors de la copie celui-ci est copié… Je me retrouve donc avec deux
fois <http://>…

Pour résoudre ce problème j'affiche toujours le protocole dans Firefox :

Ecrire dans la barre d'adresse :

    about:config

Rechercher :

    browser.urlbar.trimURLs

Modifier la valeur par :

    false
