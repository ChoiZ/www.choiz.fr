jQuery attr() avec onclick par click()
######################################
:date: 2011-01-07 16:43:00
:author: choiz
:category: text
:tags: code, js, jquery, attr(), click(), removeAttr()
:slug: 2011-01-07-jquery-attr-avec-onclick-par-click
:status: published

Après avoir perdu 2h... le attr() de jQuery [STRIKEOUT:fonctionne pas
avec l'attribut "onclick"] truc super quoi !

.. raw:: html

   </p>

Edit : en jQuery pour modifier le contenu d'un onclick il faut faire
.attr('onClick','valeur') ou faire de la façon suivante.

.. raw:: html

   </p>

Remplacer donc :

.. raw:: html

   </p>

    .. raw:: html

       </p>

    | var mavar  = 'fonctionAffichage();';
    | $("#code").attr("onclick","mavar");

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

| 
| Par :

.. raw:: html

   </p>

    .. raw:: html

       </p>

    var mavar  = 'fonctionAffichage();';

    .. raw:: html

       </p>

    $("#code").removeAttr('onclick').click(function() { eval(mavar); }
    );

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>
