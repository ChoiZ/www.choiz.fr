Title: Git déplacer mon dernier commit sur une autre branche
Date: 2013-06-22 13:07:00
Author: choiz
Category: text
Tags: git
Slug: 2013-06-22-git-déplacer-mon-dernier-commit-sur-une-autre
Status: published

J'ai fait une boulette ! J'ai commité deux fois en étant sur la branche
*master*… Généralement je fais toujours une branche pour les
modifications, cette fois j'avais créé cette branche *debug\_redirect*
mais je n'étais pas dessus…

Je me suis retrouvé avec les commits A-B-C sur mon *master*. Or le seul
qui devait être dessus devait être A et je devais avoir B-C dans ma
branche *debug\_redirect*. Voici un schéma de la situation :

![Schéma : master sur C, debug_redirect sur A]({static}/images/git-branch-1.svg)

Je dois donc soit mettre à jour ma branche *debug\_redirect*. :

    git checkout debug_redirect

    git merge master

Ce qui donne :

![Schéma : master et debug_redirect sur C]({static}/images/git-branch-2.svg)

Il me reste qu'à retourner sur le *master* et revenir à la version A. :

    git checkout master

    git reset --hard HEAD~2

Ce qui donne :

![Schéma : master sur A, debug_redirect sur C]({static}/images/git-branch-3.svg)

Maintenant que j'ai fixé mon bug sur ma branche *debug\_redirect* je
peux le merger avec le *master*. :

    git merge debug_redirect --no-ff

Résultat :

![Schéma : merge no-ff, D fusionne C sur master]({static}/images/git-branch-4.svg)

Pour voir vos commits par branche vous pouvez aussi utiliser la commande
git log :

    git log --graph --oneline --decorate
    *   4c677ac (HEAD, master) Merge branch 'debug_redirect'
    |\ 
    | * 90e7a7a (debug_redirect) Fix another bug on redirect
    | * 40ae981 Fix the redirect bug
    |/ 
    * 4e06ff4 initial commit
