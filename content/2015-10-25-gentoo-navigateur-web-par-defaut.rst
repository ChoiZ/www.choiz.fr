Gentoo Navigateur Web par Défaut
################################
:date: 2015-10-25 14:02:17
:author: choiz
:category: text
:tags: gentoo, web, browser, default, navigateur
:slug: 2015-10-25-gentoo-navigateur-web-par-defaut
:status: published

Sur ma machine "links" était le navigateur web par défaut.
Il est pratique pour lire du texte, dès que l'on a du contenu audio ou vidéo il
est préférable d'utiliser un navigateur tel que Firefox.

Voici la commande pour voir le navigateur par défaut pour les url utilisants le
protocole "http" : ::

    xdg-mime query default x-scheme-handler/http

Et voici la commande pour le "https" : ::

    xdg-mime query default x-scheme-handler/https

Pour changer le navigateur par défaut par Firefox il suffit d'executer ses deux
commandes : ::

    xdg-mime default firefox.desktop x-scheme-handler/http
    xdg-mime default firefox.desktop x-scheme-handler/https
