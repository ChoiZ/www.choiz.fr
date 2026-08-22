---
title: "Split & Vsplit dans vim"
date: 2011-05-29T17:16:00
slug: "2011-05-29-split-vsplit-dans-vim"
author: choiz
tags: ["vim", "file"]
---

Très souvent lorsque j'utilise Vim je sépare ma fenêtre en 2,3,4 pour
pouvoir ouvrir plusieurs fichiers en même temps.

Il y a 2 méthodes :

- la division de la fenêtre horizontale en utilisant :

`:split` (ou `:new`) puis : `:e le_fichier_a_ouvrir`

- la division de la fenêtre verticalement en utilisant :

`:vsplit` puis : `:e le_fichier_a_ouvrir`

Et comme lors de l'utilisation du diff (CTRL + W puis W) pour changer de
fenêtre (gauche à droite ou droite à gauche ou haut en bas ou bas en
haut) ou bien en utilisant (CTRL + W puis une flèche directionnelle).

Pour agrandir ou réduire la fenêtre courante utiliser CTRL + W (puis
&gt; si vous êtes sur votre fenêtre de droite pour ajouter une colonne,
si vous êtes sur la fenêtre de gauche ceci supprimera une colonne et vice
versa avec &lt;) vous pouvez également ajouter / supprimer 5 ou 10
colonnes avec : `5>` et `10>`
