Initialiser des sous-modules en cascade dans git
################################################
:date: 2015-01-25 11:17:00
:author: choiz
:category: text
:tags: git, submodule, update, init, recursive
:slug: 2015-01-25-initialiser-des-sous-modules-en-cascade-dans-git
:status: published

Pour initialiser les sous-modules dans git j'utilise la commande
suivante :

.. raw:: html

   </p>

``git submodule init``

.. raw:: html

   </p>

Ensuite je dois faire un update des sous-modules pour charger le contenu
:

.. raw:: html

   </p>

``git submodule update``

.. raw:: html

   </p>

Pour faire les deux en même temps (init + update) vous pouvez faire :

.. raw:: html

   </p>

``git submodule update --init``

.. raw:: html

   </p>

Imaginons maintenant que vous avez des sous-modules dans d'autres
sous-modules. Exemple dans mon dépot
`dotfiles <https://www.github.com/ChoiZ/dotfiles.git>`__ j'ai mon dépot
`vim <https://www.github.com/ChoiZ/vim-config.git>`__ et dedans des
sous-modules avec les plugins de vim. Pour initialiser, mettre à jour et
le tout en cascade (dans tous les dossiers et sous-dossiers) il faut
faire :

.. raw:: html

   </p>

``git submodule update --init --recursive``

.. raw:: html

   </p>
