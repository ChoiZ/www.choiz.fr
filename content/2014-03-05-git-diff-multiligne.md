Title: Git diff multiligne
Date: 2014-03-05 12:56:00
Author: choiz
Category: text
Tags: git, diff, wrap, multiline, multiligne, less, config, gitconfig
Slug: 2014-03-05-git-diff-multiligne
Status: published

Lors d'une modification d'un bout de code, j'ai perdu la fin d'une
ligne…

J'ai du faire un *git diff* dans mon terminal et copié la ligne (mais
pas entièrement…).

J'ai donc refais un *git diff* dans mon terminal et je me suis aperçu
que ma ligne qui devait être sur plusieurs lignes ne l'était pas…

Mon fichier texte ressemble à ceci :

    ligne avec un peu de texte ici nous avons 66 caractères affichés.

Or, quand je fais un diff on ne voit pas tous les caractères :

    git diff HEAD~1 HEAD
    diff --git a/test.txt b/test.txt
    new file mode 100644
    index 0000000..235a891
    --- /dev/null
    +++ b/test.txt
    @@ -0,0 +1 @@
    +ligne avec un peu de texte ici nous avons 66 caractè\
    No newline at end of file

Pour résoudre ce problème il faut soit ajouter *GIT\_PAGER=""* avant la
commande *git diff* soit ajouter dans son fichier de config git :

    git config --global core.pager "less -r"

Voilà ce que ça donne avec GIT\_PAGER :

    GIT_PAGER="" git diff HEAD~1 HEAD
    diff --git a/test.txt b/test.txt
    new file mode 100644
    index 0000000..235a891
    --- /dev/null
    +++ b/test.txt
    @@ -0,0 +1 @@
    +ligne avec un peu de texte ici nous avons 66 caractères affichés.\
    No newline at end of file
