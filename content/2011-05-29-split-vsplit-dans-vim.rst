Split & Vsplit dans vim
#######################
:date: 2011-05-29 17:16:00
:author: choiz
:category: text
:tags: vim, fichier, editeur, texte, terminal, commande, split, vsplit, window, colonnes, cols, columns
:slug: 2011-05-29-split-vsplit-dans-vim
:status: published

Trés souvent lorsque j'utilise Vim je sépare ma fenêtre en 2,3,4 pour
pouvoir ouvrir plusieurs fichiers en même temps.

Pour celà il utilises 2 méthodes soit :

1) la division de la fenêtre horizontal en utilisant

``:split``

ou

``:new``

et ensuite

``:e le_fichier_a_ouvrir``

2) la division de la fenêtre verticalement en utilisant

``:vsplit``

puis

``:e le_fichier_a_ouvrir``

Et comme lors de l'utilisation du diff (CTRL + W puis W) pour changer de
fenêtre (gauche à droite ou droite à gauche ou haut en bas ou bas en
haut) ou bien en utilisant (CTRL + W puis une fléche directionnelle).

Pour agrandir ou réduire la fenêtre courante utiliser CTRL + W (puis >
si vous êtes sur votre fenêtre de droite pour ajouter une colonne, si
vous êtes sur la fenêtre de gauche ceci supprimera une colonne et vis
versa avec <) vous pouvez également ajouter / supprimer 5... 10 ou n
colonnes avec :

``5>``

``10>``

ou ``n>``

