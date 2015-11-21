Git déplacer mon dernier commit sur une autre branche
#####################################################
:date: 2013-06-22 13:07:00
:author: choiz
:category: text
:tags: git, reset, checkout, merge, branch, commit
:slug: 2013-06-22-git-déplacer-mon-dernier-commit-sur-une-autre
:status: published

J'ai fais une boulette ! J'ai commité deux fois en étant sur la branche
*master*\… Généralement je fais toujours une branche pour les modifications,
cette fois j'avais créé cette branche *debug\_redirect* mais je n'étais pas
dessus…

Je me suis retrouvé avec les commits A-B-C sur mon *master*. Or le seul qui
devait être dessus devait être A et je devais avoir B-C dans ma branche
*debug\_redirect*. Voici un schéma de la situation : ::

    debug\_redirect
              ↓
              A-B-C
                  ↑
                 master

Je dois donc soit mettre a jour ma branche *debug\_redirect*. ::

    git checkout debug\_redirect

    git merge master

Ce qui donne : ::

    debug\_redirect
            ↓
        A-B-C
            ↑
          master

Il me reste qu'a retourner sur le *master* et revenir à la version A. ::

    git checkout master

    git reset --hard HEAD~2

Ce qui donne : ::

      debug\_redirect
          ↓
      A-B-C
      ↑
    master

Maintenant que j'ai fixé mon bug sur ma branche \ *debug\_redirect* je peux le
merger avec le *master*. ::

    git merge debug\_redirect --no-ff

Résultat : ::

             B-C      debug\_redirect
           /     \\
         A - - - - D   master

Pour voir vos commits par branche vous pouvez aussi utiliser la commande git log
: ::

    git log --graph --oneline --decorate
    \*   4c677ac (HEAD, master) Merge branch 'debug\_redirect'
    \|\\ 
    \| \* 90e7a7a (debug\_redirect) Fix another bug on redirect
    \| \* 40ae981 Fix the redirect bug
    \|/ 
    \* 4e06ff4 initial commit
