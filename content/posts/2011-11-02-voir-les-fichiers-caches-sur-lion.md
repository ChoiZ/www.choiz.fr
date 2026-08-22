---
title: "Voir les fichiers cachés sur Lion"
date: 2011-11-02T11:17:12
slug: "2011-11-02-voir-les-fichiers-cachés-sur-lion"
author: choiz
tags: ["file", "osx"]
---

Dans un terminal :

    defaults write com.apple.Finder AppleShowAllFiles TRUE

    killall Finder

Ouvrir une fenêtre du Finder et vous voyez les fichiers cachés.
