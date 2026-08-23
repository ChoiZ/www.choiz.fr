---
title: "Installer jshint sur mac"
date: 2013-10-14T12:41:08
slug: "2013-10-14-installer-jshint-sur-mac"
author: choiz
tags: ["npm"]
---

Installation via npm de jshint (-g pour installer pour tous les utilisateurs) :
    sudo npm install -g jshint

> ⚠️ À ne pas reproduire : `sudo npm install -g` exécute les scripts postinstall du paquet (et de ses dépendances) avec les droits root, ce qui expose à un risque supply-chain en cas de paquet compromis. Mieux vaut passer par un gestionnaire de version Node (nvm, fnm) installé sans sudo, ou utiliser `npx jshint` à la volée.

Faire un lien symbolique pour pouvoir utiliser directement jshint sans
préciser tout le chemin à chaque fois :

    ln -s /usr/local/share/npm/bin/jshint /usr/local/bin/jshint
