Suppression des branches distantes inexistantes
###############################################
:date: 2015-08-25 13:43:05
:author: choiz
:category: text
:tags: git, branch, remote, prune, origin
:slug: 2015-08-25-suppression-des-branches-distantes-inexistantes
:status: published

Lors d'un developpement j'ai créer une branche "add_namespace" qui m'a permis d'ajouter des namespaces a différents fichiers PHP.

Une fois la modification faite j'ai envoyé ma branche sur l'origin, en faisant un "pull request" (github) ou "merge request" (gitlab).

Un autre développeur a donc accepté mon pull request (il a donc mergé la branche) et a supprimer ma branche de l'origine.

Sur mon environement je vois toujours cette branche.

    git branch -a

    \* master

    remote/origin/HEAD -> origin/master

    remote/origin/add_namespace

    remote/origin/master

Pour pouvoir effacer cette remote qui n'existe plus il suffit de tapper la commande :

    git remote prune origin

    Élimination de origin

    URL : git@git.mondomain.com:mondepot.git

     \* [éliminé] origin/add_namespace

Maintenant il suffit de vérifier que tout est propre :

    git branch -a

    \* master

    remote/origin/HEAD -> origin/master

    remote/origin/master

