Git déplacer mon dernier commit sur une autre branche
#####################################################
:date: 2013-06-22 13:07:00
:author: choiz
:category: text
:tags: git, reset, checkout, merge, branch, commit
:slug: 2013-06-22-git-déplacer-mon-dernier-commit-sur-une-autre
:status: published

J'ai fais une boulette ! J'ai commité deux fois en étant sur la branche
*master*\ … Généralement je fais toujours une branche pour les
modifications, cette fois j'avais créé cette branche *debug\_redirect*
mais je n'étais pas dessus…

.. raw:: html

   </p>

| Je me suis retrouvé avec les commits A-B-C sur mon *master*. Or le
  seul qui devait être dessus devait être A et je devais avoir B-C dans
  ma branche *debug\_redirect*.
| Voici un schéma de la situation :

.. raw:: html

   </p>

    .. raw:: html

       </p>

    | debug\_redirect
    |           ↓
    |           A-B-C
    |               ↑
    |              master

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

Je dois donc soit mettre a jour ma branche *debug\_redirect*.

.. raw:: html

   </p>

    .. raw:: html

       </p>

    $ git checkout debug\_redirect

    .. raw:: html

       </p>

    $ git merge master

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

Ce qui donne :

.. raw:: html

   </p>

    .. raw:: html

       </p>

    | debug\_redirect
    |         ↓
    |     A-B-C
    |         ↑
    |    master

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

Il me reste qu'a retourner sur le *master* et revenir à la version A.

.. raw:: html

   </p>

    .. raw:: html

       </p>

    $ git checkout master

    .. raw:: html

       </p>

    $ git reset --hard HEAD~2

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

Ce qui donne :

.. raw:: html

   </p>

    .. raw:: html

       </p>

    |      debug\_redirect
    |          ↓
    |      A-B-C
    |      ↑
    | master

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

Maintenant que j'ai fixé mon bug sur ma branche \ *debug\_redirect* je
peux le merger avec le *master*.

.. raw:: html

   </p>

    .. raw:: html

       </p>

    $ git merge debug\_redirect --no-ff

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

Résultat :

.. raw:: html

   </p>

    .. raw:: html

       </p>

    |          B-C      debug\_redirect
    |        /     \\
    |      A - - - - D   master

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

Pour voir vos commits par branche vous pouvez aussi utiliser la commande
git log :

.. raw:: html

   </p>

    .. raw:: html

       </p>

    $ git log --graph --oneline --decorate

    .. raw:: html

       </p>

    | \*   4c677ac (HEAD, master) Merge branch 'debug\_redirect'
    | \|\\ 
    | \| \* 90e7a7a (debug\_redirect) Fix another bug on redirect
    | \| \* 40ae981 Fix the redirect bug
    | \|/ 
    | \* 4e06ff4 initial commit

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>
