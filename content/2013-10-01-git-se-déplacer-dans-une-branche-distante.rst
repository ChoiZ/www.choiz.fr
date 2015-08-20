Git se déplacer dans une branche distante
#########################################
:date: 2013-10-01 13:51:00
:author: choiz
:category: text
:tags: git, checkout, fetch, origin, checkout -b, branch, remote
:slug: 2013-10-01-git-se-déplacer-dans-une-branche-distante
:status: published

| J'utilise des branches tel que prod, preprod pour mes projets et en
  local il m'arrive de vouloir aller sur ses branches.
| Je fais donc :

.. raw:: html

   </p>

``git checkout preprod``

.. raw:: html

   </p>

Et j'ai l'erreur suivante :

.. raw:: html

   </p>

::

    error: pathspec 'preprod' did not match any file(s) known to git.

.. raw:: html

   </p>

Je vais mettre a jour mon origin :

.. raw:: html

   </p>

``git fetch origin``

.. raw:: html

   </p>

Maintenant je veux ma branche distante en lui précisant l'origin :

.. raw:: html

   </p>

``git checkout -b preprod origin/preprod``

.. raw:: html

   </p>

Et j'ai bien ma branche en local comme git me l'indique :

.. raw:: html

   </p>

::

    Branch preprod set up to track remote branch preprod from origin.
    Switched to a new branch 'preprod'

.. raw:: html

   </p>
