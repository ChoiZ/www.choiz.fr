---
title: "Suppression des branches distantes inexistantes"
date: 2015-08-25T13:43:05
slug: "2015-08-25-suppression-des-branches-distantes-inexistantes"
author: choiz
tags: ["git"]
---

Lors d'un développement j'ai créé une branche "add\_namespace" qui m'a
permis d'ajouter des namespaces à différents fichiers PHP.

Une fois la modification faite j'ai envoyé ma branche sur l'origin, en
faisant un "pull request" (github) ou "merge request" (gitlab).

Un autre développeur a accepté mon pull request (il a donc mergé la
branche) et a supprimé ma branche de l'origine.

Sur mon environnement je vois toujours cette branche.

> git branch -a
>
> \* master
>
> remote/origin/HEAD -&gt; origin/master
>
> remote/origin/add\_namespace
>
> remote/origin/master

Pour pouvoir effacer cette branche dans le remote, il suffit de taper
la commande :

> git remote prune origin
>
> Élimination de origin
>
> URL : <git@git.mondomain.com>:mondepot.git
>
>  \* \[éliminé\] origin/add\_namespace

Maintenant, vérifions que tout est propre :

> git branch -a
>
> \* master
>
> remote/origin/HEAD -&gt; origin/master
>
> remote/origin/master
