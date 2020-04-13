Title: Git se déplacer dans une branche distante
Date: 2013-10-01 13:51:00
Author: choiz
Category: text
Tags: git, origin, branch
Slug: 2013-10-01-git-se-déplacer-dans-une-branche-distante
Status: published

J'utilise des branches tel que prod, preprod pour mes projets et en
local il m'arrive de vouloir aller sur ses branches :

    git checkout preprod

Et j'ai l'erreur suivante :

    error: pathspec 'preprod' did not match any file(s) known to git.

Je vais mettre a jour mon origin :

    git fetch origin

Maintenant je veux ma branche distante en lui précisant l'origin :

    git checkout -b preprod origin/preprod

Et j'ai bien ma branche en local comme git me l'indique :

    Branch preprod set up to track remote branch preprod from origin.
    Switched to a new branch 'preprod'
