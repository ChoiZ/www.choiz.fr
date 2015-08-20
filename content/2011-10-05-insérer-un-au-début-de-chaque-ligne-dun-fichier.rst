Insérer un # au début de chaque ligne d'un fichier avec vim
###########################################################
:date: 2011-10-05 00:42:00
:author: choiz
:category: text
:tags: Vim, search, replace, line, add, ligne, fichier, file, remplace, ajout
:slug: 2011-10-05-insérer-un-au-début-de-chaque-ligne-dun-fichier
:status: published

Voilà la commande pour ajouter un # au début de chaque ligne d'un
fichier avec vim :

.. raw:: html

   </p>

``:1,$s/^/#/``

.. raw:: html

   </p>

Explications :

.. raw:: html

   </p>

``:1,$``

.. raw:: html

   </p>

Selection des ligne 1 à $ ($ étant la dernière).

.. raw:: html

   </p>

``s/^/#/``

.. raw:: html

   </p>

s pour search (en fait il cherche et remplace) ^ le début de ligne ($ si
on voulais la fin de la ligne) et # le caractère que je veux remplacer

.. raw:: html

   </p>
