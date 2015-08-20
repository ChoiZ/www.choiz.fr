Git diff multiligne
###################
:date: 2014-03-05 12:56:00
:author: choiz
:category: text
:tags: git, diff, wrap, multiline, multiligne, less, config, gitconfig
:slug: 2014-03-05-git-diff-multiligne
:status: published

Lors d'une modification d'un bout de code, j'ai perdu la fin d'une
ligne…

.. raw:: html

   </p>

J'ai du faire un *git diff* dans mon terminal et copié la ligne (mais
pas entièrement…).

.. raw:: html

   </p>

J'ai donc refais un *git diff* dans mon terminal et je me suis aperçu
que ma ligne qui devait être sur plusieurs lignes ne l'était pas…

.. raw:: html

   </p>

Mon fichier texte ressemble à ceci :

.. raw:: html

   </p>

``ligne avec un peu de texte ici nous avons 66 caractères affichés.``

.. raw:: html

   </p>

Or, quand je fais un diff on ne voit pas tous les caractères

.. raw:: html

   </p>

::

    $ git diff HEAD~1 HEADdiff --git a/test.txt b/test.txtnew file mode 100644index 0000000..235a891--- /dev/null+++ b/test.txt@@ -0,0 +1 @@+ligne avec un peu de texte ici nous avons 66 caractè\ No newline at end of file

.. raw:: html

   </p>

Pour résoudre ce problème il faut soit ajouter *GIT\_PAGER=""*  avant la
commande *git diff* soit ajouter dans son fichier de config git :

.. raw:: html

   </p>

``git config --global core.pager "less -r"``

.. raw:: html

   </p>

Voila ce que ça donne avec GIT\_PAGER

.. raw:: html

   </p>

``GIT_PAGER="" git diff HEAD~1 HEAD``

.. raw:: html

   </p>

::

    diff --git a/test.txt b/test.txtnew file mode 100644index 0000000..235a891--- /dev/null+++ b/test.txt@@ -0,0 +1 @@+ligne avec un peu de texte ici nous avons 66 caractères affichés.\ No newline at end of file

.. raw:: html

   </p>
