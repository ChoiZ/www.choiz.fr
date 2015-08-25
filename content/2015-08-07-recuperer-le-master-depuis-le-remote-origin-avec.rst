Récupérer le master depuis le remote origin avec git
####################################################
:date: 2015-08-07 17:33:07
:author: choiz
:category: text
:tags: git, origin, remote, master, branch, checkout, track
:slug: 2015-08-07-récupérer-le-master-depuis-le-remote-origin-avec
:status: published

| Dans certains projets j’utilise git avec plusieurs remote, par exemple
  :

| - un remote “origin” se trouve sur un serveur perso.

| - un remote “github” qui lui est sur github.com.

.. raw:: html

   </p>

Quand je vais sur le master il m’arrive d’avoir ce message :

.. raw:: html

   </p>

::

    "your branch is up-to-date with “github/master”."

.. raw:: html

   </p>

Je préfèrerai que ma branche soit à jour avec mon origin/master et non
github/master.

.. raw:: html

   </p>

La solution que j’ai trouvé est la suivante :

.. raw:: html

   </p>

1) supprimer ma branche master locale :

.. raw:: html

   </p>

``git branch -d master``

2) récupèrer mon master depuis le remote origin :

.. raw:: html

   </p>

``git checkout -t -b master origin/master``

Pour info :

.. raw:: html

   </p>

-t ou --track pour rattacher à l’origin/master

.. raw:: html

   </p>

-b pour créer ma nouvelle branche “master”

.. raw:: html

   </p>

Plus d’info avec man git-checkout ;-)

.. raw:: html

   </p>
