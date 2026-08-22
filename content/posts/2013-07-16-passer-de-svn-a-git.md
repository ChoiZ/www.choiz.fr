---
title: "Passer de svn à git"
date: 2013-07-16T22:37:00
slug: "2013-07-16-passer-de-svn-à-git"
author: choiz
tags: ["svn", "git"]
---

Sur le projet Addictradio nous utilisons encore un de nos dépôts avec
svn. Il est temps de faire la migration de svn à git !

J'ai testé plusieurs méthodes et aucune ne fait exactement ce que je
voulais voici donc ma procédure :

    svn log --quiet 'svn://svn.mondomaine/monprojet' | grep "^r" | awk
    '{print $3}' | sort | uniq | awk '{ print $1" = "$1"
    <"$1"@mondomaine>" }' > authors.txt

J'ai ensuite édité authors.txt pour remplacer nos différents pseudos par
nos prénoms et noms puis j'ai vérifié les adresses e-mails.

Puis j'ai utilisé git svn clone :

    git svn clone 'svn://svn.mondomaine/monprojet' --no-metadata
    --authors-file=authors.txt --tags=tags --branches=branches
    --trunk=trunk monprojet

Si vous avez des tags dans svn, vous pouvez les mettre dans git :

    git branch -r | sed -rne 's, \*tags/([^@]+)$,\\1,p' | while read
    tag; do echo "git tag $tag 'tags/${tag}^'; git branch -r -d
    tags/$tag"; done | sh

Pour finir ajoutez votre dépôt distant :

    git remote add origin git@git.mondomaine:/monprojet.git
    git push -u origin --tags
