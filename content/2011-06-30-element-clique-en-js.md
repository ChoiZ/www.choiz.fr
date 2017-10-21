Title: Elément cliqué en js
Date: 2011-06-30 16:55:59
Author: choiz
Category: text
Tags: JavaScript, Code
Slug: 2011-06-30-elément-cliqué-en-js
Status: published

Pour savoir quel élément est cliqué j'utilise ce petit bout de javascript :

    function checkclick(e) {
        e = e || window.event;
        var o = e.target || e.srcElement;
        console.log(o);
    }
    document.onclick=checkclick;

Pratique pour faire du débug.
