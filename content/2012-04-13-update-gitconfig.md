Title: Update .gitconfig
Date: 2012-04-13 12:00:00
Author: choiz
Category: text
Tags: git, gitconfig, git pull, git push, git diff, git stash, stash
Slug: 2012-04-13-update-gitconfig
Status: published

Ajout du pull, push, diff et surtout stash :

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
      di = diff
      ph = push
      pl = pull
      sta = stash
      stalist = stash list
      stast = stash list
      stapp = stash pop
      starm = stash drop
      last = cat-file commit HEAD
      graph = log --graph --decorate
      tree = log --graph --oneline --decorate
      pom = push origin master
      logs = log --stat
      currentbranch = "!git branch | grep ^* | cut -d \" \" -f 2"
    [core]
      excludesfile = ~/.gitignore
    editor = vim
      filemode = false
    [merge]
      tool = vimdiff
    [http]
      #sslverify = false|
