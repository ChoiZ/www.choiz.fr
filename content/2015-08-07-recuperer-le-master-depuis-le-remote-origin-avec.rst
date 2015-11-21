Récupérer le master depuis le remote origin avec git
####################################################
:date: 2015-08-07 17:33:07
:author: choiz
:category: text
:tags: git, origin, remote, master, branch, checkout, track
:slug: 2015-08-07-récupérer-le-master-depuis-le-remote-origin-avec
:status: published

Dans certains projets j’utilise git avec plusieurs remote, par exemple :

- un remote “origin” se trouve sur un serveur perso.
- un remote “github” qui lui est sur github.com.

Quand je vais sur le master il m’arrive d’avoir ce message : ::

    "your branch is up-to-date with “github/master”."

Je préfèrerai que ma branche soit à jour avec mon origin/master et non
github/master.

La solution que j’ai trouvé est la suivante :

1) supprimer ma branche master locale : ::

    git branch -d master

2) récupèrer mon master depuis le remote origin : ::

    git checkout -t -b master origin/master

Pour info :

-t ou --track pour rattacher à l’origin/master

-b pour créer ma nouvelle branche “master”

Plus d’info avec man git-checkout ;-)
