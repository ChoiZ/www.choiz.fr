---
title: "Mettre à jour Gentoo"
date: 2015-09-27T14:04:13
slug: "2015-09-27-mettre-a-jour-gentoo"
author: choiz
tags: ["gentoo", "emerge", "linux"]
---

Pour mettre à jour Gentoo j'utilise différentes commandes.

Dans un premier temps je fais la mise à jour d'eix :

    eix-sync

Ensuite :

    emerge -pvuDN world

-p ou --pretend, permet d'afficher ce qui sera mis à jour. Affiche
également les différents flags (N = new (not yet installed), U =
updating (to another version) etc…) -v ou --verbose, mode verbeux. -u ou
--update, met à jour les programmes dans la meilleure version disponible.
-D ou --deep, met à jour les dépendances des programmes si nécessaire.
-N ou --newuse, met à jour les programmes dont le "USE" a été modifié
depuis son installation.

Une fois la liste des programmes et ses modifications vérifiée nous
pouvons lancer la mise à jour :

    emerge -vuDN world
