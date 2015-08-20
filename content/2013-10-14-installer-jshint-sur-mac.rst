Installer jshint sur mac
########################
:date: 2013-10-14 12:41:08
:author: choiz
:category: text
:tags: jshint, mac, setup, npm, nodejs
:slug: 2013-10-14-installer-jshint-sur-mac
:status: published

Installation via npm de jshint (-g pour installer pour tous les
utilisateurs) :

    sudo npm install -g jshint

Faire un lien symbolique pour pouvoir utiliser directement jshint sans
préciser tout le chemin a chaque fois :

    ln -s /usr/local/share/npm/bin/jshint /usr/local/bin/jshint

