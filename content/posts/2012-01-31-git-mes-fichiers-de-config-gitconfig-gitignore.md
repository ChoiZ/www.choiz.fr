---
title: "Git mes fichiers de config gitconfig / gitignore"
date: 2012-01-31T10:34:00
slug: "2012-01-31-git-mes-fichiers-de-config-gitconfig-gitignore"
author: choiz
tags: ["git", "config"]
---

Fichier .gitconfig :

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

Fichier .gitignore :

    # Ignore files from git

    # ._ files (Mac Os X)
    ._*

    # .DS_STORE (Mac Os X)
    .DS_STORE

    # .swp (Vim)
    *.swp
