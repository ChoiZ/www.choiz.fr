---
title: "Elément cliqué en js"
date: 2011-06-30T16:55:59
slug: "2011-06-30-elément-cliqué-en-js"
author: choiz
tags: ["javascript", "code"]
---

Pour savoir quel élément est cliqué j'utilise ce petit bout de javascript :

    function checkclick(e) {
        e = e || window.event;
        var o = e.target || e.srcElement;
        console.log(o);
    }
    document.onclick=checkclick;

Pratique pour faire du débug.
