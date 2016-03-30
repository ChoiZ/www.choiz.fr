Utilisation des branches et de git stash
========================================

date  
2012-04-14 16:32:42

author  
choiz

category  
text

tags  
git, git stash, git stash pop, git stash list, git branch, git checkout

slug  
2012-04-14-utilisation-des-branches-et-de-git-stash

status  
published

Quand j'utilise git avec des branches il m'arrive d'avoir des fichiers
sur une branche qui sont pas a commiter dans l'immédiat. J'utilise donc
git stash, voyons voir comment l'utiliser simplement.

On regarde l'état du status et des branches :

    git status
    # On branch master
    nothing to commit (working directory clean)

    $ git branch
    * master

Je travail sur la branche master et je n'ai pas d'autre branche. Je vais
donc faire une branche API pour mon projet. :

    git branch API

    git branch
      API
      * master

Maintenant je vais changer de branche git checkout pour être sur ma
branche API et modifier les fichiers sur cette branche. :

    git checkout API
    Switched to branch 'API'

    git branch
    * API
      master

Maintenant je vais modifier un mon fichier manage.py sur ma branche API.
:

    git status
    # On branch API
    # Changes not staged for commit:
    #   (use "git add <file>..." to update what will be committed)
    #   (use "git checkout -- <file>..." to discard changes in working directory)
    #
    #    modified:   manage.py
    #
    no changes added to commit (use "git add" and/or "git commit -a")

Si je veux revenir sur mon master, sans avoir la modification du
manage.py je vais devoir utiliser git stash (qui sauvegardera mes
modifications du manage.py) :

    git stash
    Saved working directory and index state WIP on API: 8b6342d Fix register.py
    HEAD is now at 8b6342d Fix register.py

    $ git status
    # On branch API
    nothing to commit (working directory clean)

Maintenant que notre branche est propre on peut changer de branche
revenir sur le master par exemple. :

    $ git checkout master
    Switched to branch 'master'

    $ git status
    # On branch master
    nothing to commit (working directory clean)

On peut donc travailler tranquillement sur la branche master. Puis
revenir sur notre branche API, lister les stash git stash list récupérer
les modifications précédentes git stash pop. :

    git checkout API
    Switched to branch 'API'

    git stash list
    stash@{0}: WIP on API: 8b6342d Fix register.py

    git stash pop
    # On branch API
    # Changes not staged for commit:
    #   (use "git add <file>..." to update what will be committed)
    #   (use "git checkout -- <file>..." to discard changes in working directory)
    #
    #    modified:   manage.py
    #
    no changes added to commit (use "git add" and/or "git commit -a")
    Dropped refs/stash@{0} (533906a52b923a8960fa0f6fdf17a288c94f233a)

    $ git status
    # On branch API
    # Changes not staged for commit:
    #   (use "git add <file>..." to update what will be committed)
    #   (use "git checkout -- <file>..." to discard changes in working directory)
    #
    #    modified:   manage.py
    #
    no changes added to commit (use "git add" and/or "git commit -a")

Maintenant je peux continuer les modifications sur ma branche API
réutilise git stash si besoin ou les commiter, merger ma branche…

git stash pop (récupére le dernier stash enregistré
[stash@{0}](mailto:stash@{0}), l'applique et le supprime de la liste)
mon alias = git stapp

git stash apply (récupére le dernier stash enregistré
[stash@{0](mailto:stash@{0)} et l'applique)

Et pour rien n'oublier (RTFM) : man git stash
