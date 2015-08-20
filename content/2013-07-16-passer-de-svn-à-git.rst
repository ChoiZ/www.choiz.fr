Passer de svn à git
###################
:date: 2013-07-16 22:37:00
:author: choiz
:category: text
:tags: svn to git, svn, git, migate, git svn clone, authors, tags
:slug: 2013-07-16-passer-de-svn-à-git
:status: published

| Sur le projet Addictradio nous utilisons encore un de nos dépot avec
  svn.
| Il est temps de faire la migration de svn à git !

.. raw:: html

   </p>

J'ai testé plusieurs méthodes et aucune ne fait exactement ce que je
voulais voici donc ma procédure :

.. raw:: html

   </p>

    .. raw:: html

       </p>

    svn log --quiet 'svn://svn.mondomaine/monprojet' \| grep "^r" \| awk
    '{print $3}' \| sort \| uniq \| awk '{ print $1" = "$1"
    <"$1"@mondomaine>" }' > authors.txt

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

J'ai ensuite édité authors.txt pour remplacer nos différents pseudos par
nos prénoms et noms et j'ai vérifier les adresses e-mails.

.. raw:: html

   </p>

Puis j'ai git svn clone :

.. raw:: html

   </p>

    .. raw:: html

       </p>

    git svn clone 'svn://svn.mondomaine/monprojet' --no-metadata
    --authors-file=authors.txt --tags=tags --branches=branches
    --trunk=trunk monprojet

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

Si vous avez des tags dans svn, vous pouvez les mettre dans git :

.. raw:: html

   </p>

    .. raw:: html

       </p>

    git branch -r \| sed -rne 's, \*tags/([^@]+)$,\\1,p' \| while read
    tag; do echo "git tag $tag 'tags/${tag}^'; git branch -r -d
    tags/$tag"; done \| sh

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

Pour finir ajoutez votre dépot distant :

.. raw:: html

   </p>

    .. raw:: html

       </p>

    | git remote add origin git@git.mondomaine:/monprojet.git
    | git push -u origin --tags

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

Merci à
`Bazoud <http://bazoud.com/articles/2010-12-11-migration-de-svn-vers-git-en-4-etapes/index.html>`__
pour différentes commandes ;)

.. raw:: html

   </p>
