Comment récupérer le contenu d’un fichier d’une autre branche avec GIT ?
########################################################################
:date: 2015-03-20 15:27:23
:author: choiz
:category: text
:slug: 2015-03-20-comment-récupérer-le-contenu-dun-fichier-dune-autre-branche
:status: published

Il suffit d’utiliser git show.

La commande : ::

    git show branch_name:filename

Exemple : ::

    git show reset_password:/templates/reset_password.tmpl
