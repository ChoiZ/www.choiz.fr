Title: Voir le contenu d'un fichier dans un stash précis (git)
Date: 2012-07-06 17:56:00
Author: choiz
Category: text
Tags: git, stash, content, file, file content, git stash, show
Slug: 2012-07-06-voir-le-contenu-dun-fichier-dans-un-stash-précis
Status: published

Pour lister les stash :

    git stash list

    stash@{0}: WIP on BranchName: 5d8a556 Edit file.js
    stash@{1}: WIP on BranchName: 66dfe78 Edit file.css
    …
    stash@{5}: WIP on BranchName: 3bb67ff Add file.css file.js

Pour voir le contenu d'un stash :

    git stash show

    stash@{0} chemin/vers/mon/fichier.js | 199 ++++++++++++++++++++++++++--------
    chemin/vers/mon/autre/fichier.js | 114 ++++++++++++++------

Pour voir le contenu de "chemin/vers/mon/fichier.js" qui est dans le
stash{0} :

    git show stash@{0}:chemin/vers/mon/fichier.js
