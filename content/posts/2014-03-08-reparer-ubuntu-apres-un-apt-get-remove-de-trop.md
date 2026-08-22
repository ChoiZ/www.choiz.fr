---
title: "Réparer xubuntu après un apt-get remove… de trop"
date: 2014-03-08T13:34:00
slug: "2014-03-08-réparer-xubuntu-après-un-apt-get-remove-de-trop"
author: choiz
tags: ["dpkg", "debian", "xubuntu", "linux"]
---

En voulant modifier xscreensaver par i3lock j'ai supprimé des paquets
non utilisés (jeux etc…).

J'ai malheureusement supprimé un peu (trop) de paquets tel que
(xfdesktop4 et xfce4-panel). Au démarrage de x, une fois identifié, un
écran gris s'affiche et rien d'autre. Heureusement grâce à mon accès
SSH je peux me connecter à la machine à distance.

Pour voir la liste des paquets désinstallés j'ai donc fait :

    dpkg --get-selections > liste-des-paquets

Il suffit ensuite d'ouvrir dans un éditeur texte (type vi) le fichier
pour voir les paquets installés / désinstallés. Et réinstaller avec sudo
apt-get install le ou les paquets manquants.
