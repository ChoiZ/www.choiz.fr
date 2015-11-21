Git mes fichiers de config gitconfig / gitignore
################################################
:date: 2012-01-31 10:34:00
:author: choiz
:category: text
:tags: git, gitconfig, gitignore, git color, git tools, git alias, git merge, git diff, git editor, git excludesfile
:slug: 2012-01-31-git-mes-fichiers-de-config-gitconfig-gitignore
:status: published

Fichier .gitconfig ::

    [user]
        name = François LASSERRE
        email = mon@email.fr
    [diff]
        tool = vimdiff
    [color]
        branch = auto
        diff = auto
        status = auto
        interactive = auto
        ui = true
    [alias]
        br = branch
        ci = commit -a
        co = checkout
        sh = show --color-words
        st = status
        last = cat-file commit HEAD
        tree = log --graph --oneline --decorate
        graph = log --graph --decorate
        pom = push origin master
    [core]
        excludesfile = ~/.gitignore
        editor = vim
    [merge]
        tool = vimdiff

Fichier .gitignore ::

    # Ignore files from git
    
    # ._ files (Mac Os X)
    ._*
    
    # .DS_STORE (Mac Os X)
    .DS_STORE
    
    # .swp (Vim)
    *.swp

