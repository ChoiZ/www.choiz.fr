---
title: "jQuery attr() avec onclick par click()"
date: 2011-01-07T16:43:00
slug: "2011-01-07-jquery-attr-avec-onclick-par-click"
author: choiz
tags: ["code", "jquery", "javascript"]
---

Après avoir perdu 2h… J'ai découvert que la méthode attr() de jQuery
fonctionne pas avec l'attribut "onclick"…

Edit : Avec jQuery pour modifier le contenu d'un onclick il faut faire
.attr('onClick','valeur') ou faire de la façon suivante.

Remplacer donc :

    var mavar = 'fonctionAffichage();';
    $("#code").attr("onclick","mavar");

Par ce que je conseillais à l'époque… mais qu'il ne faut surtout pas faire :

<pre><del>var mavar = 'fonctionAffichage();';
$("#code").removeAttr('onclick').click(function() { eval(mavar); });</del></pre>

> ⚠️ Il ne faut pas utiliser `eval()` : exécuter une chaîne de code, c'est une porte ouverte à l'injection ou au XSS dès que cette chaîne contient la moindre donnée non maîtrisée. On attache une référence de fonction, jamais une chaîne à évaluer, et on oublie au passage l'attribut onclick inline.

Voici ce qu'il faut utiliser à la place :

    $("#code").off("click").on("click", fonctionAffichage);
