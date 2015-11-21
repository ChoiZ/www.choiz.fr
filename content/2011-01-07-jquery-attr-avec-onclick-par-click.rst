jQuery attr() avec onclick par click()
######################################
:date: 2011-01-07 16:43:00
:author: choiz
:category: text
:tags: code, js, jquery, attr(), click(), removeAttr()
:slug: 2011-01-07-jquery-attr-avec-onclick-par-click
:status: published

Après avoir perdu 2h…
J'ai découvert que la methode attr() de jQuery fonctionne pas
avec l'attribut "onclick"…

Edit : Avec jQuery pour modifier le contenu d'un onclick il faut faire
.attr('onClick','valeur') ou faire de la façon suivante.

Remplacer donc : ::

    var mavar = 'fonctionAffichage();';
    $("#code").attr("onclick","mavar");

Par : ::

    var mavar = 'fonctionAffichage();';
    $("#code").removeAttr('onclick').click(function() { eval(mavar); });
