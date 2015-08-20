Suppression d'un caractère unicode dans Vim
###########################################
:date: 2014-01-19 17:06:00
:author: choiz
:category: text
:tags: vim, unicode, char, suppression, caractère
:slug: 2014-01-19-suppression-dun-caractère-unicode-dans-vim
:status: published

J'étais à la recherche de se caractère unicode dans vim :

.. raw:: html

   </p>

``<U+2028>``

.. raw:: html

   </p>

Pour pouvoir le supprimer j'ai utilisé la commande suivante :

.. raw:: html

   </p>

``:%s/\%U2028//g``

.. raw:: html

   </p>

Décortiquons la commande :

.. raw:: html

   </p>

``:%s/`` Recherche et remplace dans tout le fichier

.. raw:: html

   </p>

``\%U2028`` Le caractère que l'on recherche unicode "2028"

.. raw:: html

   </p>

``//`` par rien (1er slash sépare la recherche par ce qu'on remplace, le
second pour dire la fin de ce qu'on remplace).

.. raw:: html

   </p>

``g`` dans tout le fichier (global).

.. raw:: html

   </p>
