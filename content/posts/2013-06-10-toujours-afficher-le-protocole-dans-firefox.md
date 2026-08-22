---
title: "Toujours afficher le protocole dans Firefox"
date: 2013-06-10T14:22:00
slug: "2013-06-10-toujours-afficher-le-protocole-dans-firefox"
author: choiz
tags: ["web", "config"]
---

Souvent lorsque je copie/colle une url depuis firefox j'ajoute <http://>
or lors de la copie celui-ci est copié… Je me retrouve donc avec deux
fois <http://>…

Pour résoudre ce problème j'affiche toujours le protocole dans Firefox :

Écrire dans la barre d'adresse :

    about:config

Rechercher :

    browser.urlbar.trimURLs

Modifier la valeur par :

    false
