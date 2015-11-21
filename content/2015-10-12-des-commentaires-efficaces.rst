Des commentaires efficaces
##########################
:date: 2015-10-12 13:44:15
:author: choiz
:category: text
:tags: commentaire, code, efficace
:slug: 2015-10-12-des-commentaires-efficaces
:status: published

Dans mes fichiers de test j'utilise souvent des commentaires pour tester qu'une
fonctionnalité de code.

Par exemple pour tester une api : ::

    // Obtenir le livre #1
    api_get('books/1');

    // Ajouter un livre
    api_add('books', $datas);

Je test généralement chaque élément séparement.

Pour tester la première portion de mon code : ::

    //* Obtenir le livre #1
    api_get('books/1');
    //\*/

    /* Ajouter un livre
    api_add('books', $datas);
    //\*/

Pour tester la seconde portion de mon code : ::

    /* Obtenir le livre #1
    api_get('books/1');
    //\*/

    //* Ajouter un livre
    api_add('books', $datas);
    //\*/

Il me suffit d'ajouter ou d'enlever un slash sur le premier commentaire pour
commenter ou non tout le bloc.

Ce n'est pas forcément très lisible donc je fais ça uniquement pour mes tests.
