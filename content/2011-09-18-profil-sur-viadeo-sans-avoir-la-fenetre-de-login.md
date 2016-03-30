J'ai voulu plusieurs fois voir un profil sur Viadeo sans forcement être
identifié. Lorsque l'on déplace la souris ou que l'on scroll une autre
page s'affiche. Exemple sur [ma page
viadeo](http://www.viadeo.com/fr/profile/francois.lasserre1). Pour
empécher d'avoir la page de login il faut modifier une fonction
Javascript. Avec un outil tel que [Firebug](http://www.getfirebug.com)
vous pouvez modifier le code Javascript du site (localement). Ouvrir
firebug en mode console et modifier la fonction createJoin() ! Dans la
console a coté de "&gt;&gt;&gt;" il suffit de taper : :

    function createJoin() { false; }

Avec ce code on modifie le contenu de la fonction createJoin() par false
(plutôt que le code par defaut qui ouvre la fenêtre d'identification).
