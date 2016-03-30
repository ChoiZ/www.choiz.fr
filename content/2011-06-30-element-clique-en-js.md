Pour savoir quel élément est cliqué j'utilise ce petit bout de
javascript : :

    function checkclick(e) {
        e = e || window.event;
        var o = e.target || e.srcElement;
        console.log(o);
    }
    document.onclick=checkclick;

Pratique pour faire du débug.
