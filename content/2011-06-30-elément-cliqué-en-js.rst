Elément cliqué en js
####################
:date: 2011-06-30 16:55:59
:author: choiz
:category: text
:tags: js, element, click, javascript, html
:slug: 2011-06-30-elément-cliqué-en-js
:status: published

Pour savoir quel élément est cliqué j'utilise ce petit bout de
javascript :

.. raw:: html

   </p>

    .. raw:: html

       </p>

    | function checkclick(e) {
    |     e = e \|\| window.event;
    |     var o = e.target \|\| e.srcElement;
    |     console.log(o);
    | }
    | document.onclick=checkclick;

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

Pratique pour du debug ;)

.. raw:: html

   </p>
