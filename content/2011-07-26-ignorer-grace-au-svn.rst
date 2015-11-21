Ignorer grâce au SVN
####################
:date: 2011-07-26 18:53:21
:author: choiz
:category: text
:tags: svn, ignore, fichier, file, folder, dossier, .DS_Store, ._*, ._, .swp, Vim, Mac Os
:slug: 2011-07-26-ignorer-grâce-au-svn
:status: published

Il existe plusieurs solutions pour ignorer des fichiers sur un svn : ::

    svn propset svn:ignore

Ou dans la configuration du svn dans `~/.subversion/config` le `global-ignores`

Pour ignorer tous les fichiers qui commencent par `._` dans le dossier ou
l'on se trouve actuellement il suffit d'executer la commande svn
suivante : ::

    svn propset svn:ignore "._*" .

Par contre si on veut ignorer tous les fichiers qui commencent par `._`
dans tous les dossiers (et sous dossiers) du svn il faut éditer le
fichier `~/.subversion/config` et d'éditer la ligne suivante : ::

    global-ignores = ._*

On peut également ajouter d'autres fichiers a ignorer tel que les `.swp`
de Vim ou les `.DS_STORE` de Mac OS en remplaçant comme ceci : ::

    global-ignores = ._* .DS_STORE *.swp
