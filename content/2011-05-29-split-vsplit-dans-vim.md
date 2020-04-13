Title: Split & Vsplit dans vim
Date: 2011-05-29 17:16:00
Author: choiz
Category: text
Tags: vim, file
Slug: 2011-05-29-split-vsplit-dans-vim
Status: published

Trés souvent lorsque j'utilise Vim je sépare ma fenêtre en 2,3,4 pour
pouvoir ouvrir plusieurs fichiers en même temps.

Il y a 2 méthodes :

- la division de la fenêtre horizontal en utilisant :

`:split` (ou `:new`) puis : `:e le_fichier_a_ouvrir`

- la division de la fenêtre verticalement en utilisant :

`:vsplit` puis : `:e le_fichier_a_ouvrir`

Et comme lors de l'utilisation du diff (CTRL + W puis W) pour changer de
fenêtre (gauche à droite ou droite à gauche ou haut en bas ou bas en
haut) ou bien en utilisant (CTRL + W puis une fléche directionnelle).

Pour agrandir ou réduire la fenêtre courante utiliser CTRL + W (puis
&gt; si vous êtes sur votre fenêtre de droite pour ajouter une colonne,
si vous êtes sur la fenêtre de gauche ceci supprimera une colonne et vis
versa avec &lt;) vous pouvez également ajouter / supprimer 5 ou 10
colonnes avec : `5>` et `10>`
