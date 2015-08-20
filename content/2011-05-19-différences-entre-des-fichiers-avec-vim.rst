Différences entre des fichiers avec Vim
#######################################
:date: 2011-05-19 23:32:00
:author: choiz
:category: text
:tags: Vim, Diff, Différence, Fichiers, Editeur, Texte, Terminal, Console, Commande
:slug: 2011-05-19-différences-entre-des-fichiers-avec-vim
:status: published

| J'ai souvent besoin de voir les différences entre plusieurs
  fichiers... J'utilise souvent la commande diff dans un terminal, mais
  mon éditeur texte favoris "Vim" sait aussi trés bien faire un
  différentiel.
| Utilisation avec le terminal :

.. raw:: html

   </p>

    .. raw:: html

       </p>

    $ diff fichier1 fichier2

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

Celui-ci retournera les différences directement dans le terminal (pas
pratique pour l'édition).

.. raw:: html

   </p>

Utilisation avec vim :

.. raw:: html

   </p>

    .. raw:: html

       </p>

    $ vim -d fichier1 fichier2

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

Ensuite il suffit d'utiliser (CTRL + W puis W) pour changer de fenêtre
(gauche à droite ou droite à gauche) ou bien en utilisant (CTRL + W puis
fléche de droite ou gauche) suivant la direction ou on veut aller ;)

.. raw:: html

   </p>

Pour le reste des commandes reportez-vous au `guide de survie de
vi <http://matrix.samizdat.net/pratique/documentation/guide-survie-VI.html>`__
!

.. raw:: html

   </p>
