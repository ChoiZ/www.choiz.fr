---
title: "Flash sous Debian"
date: 2011-11-30T22:52:56
slug: "2011-11-30-flash-sous-debian"
author: choiz
tags: ["debian", "linux"]
---

> ⚠️ Obsolète : Adobe Flash Player est en fin de vie depuis le 31 décembre 2020, ce plugin n'est plus maintenu, plus supporté par les navigateurs et truffé de failles connues. Ne l'installez plus, quelle que soit la distribution.

Lors de l'installation de Debian sur mon poste au travail j'ai eu la
surprise en ouvrant Firefox que Deezer ne fonctionne pas ! Travaillant
chez Deezer c'est un peu problématique.

J'ai donc téléchargé le package flashplugin-nonfree en procédant comme
ceci :

    vi /etc/apt/source.list

Ajouter contrib non-free aux différentes sources (sauf security) puis :

    apt-get update

    apt-get install flashplugin-nonfree

En relançant Firefox j'ai bien flash player fonctionnel sur Deezer.

Le package flashplugin étant nonfree Debian ne l'inclut pas directement
lors de l'installation.
