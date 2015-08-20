Réparer ubuntu après un apt-get remove… de trop
###############################################
:date: 2014-03-08 13:34:00
:author: choiz
:category: text
:tags: xubuntu, ubuntu, xfce, écran gris, apt-get remove, réparation
:slug: 2014-03-08-réparer-ubuntu-après-un-apt-get-remove-de-trop
:status: published

En voulant modifier xscreensaver par i3lock j'ai supprimé des paquets
non utilisés (jeux etc…).

| J'ai malheureusement supprimé un peu (trop) de paquets tel que
  (xfdesktop4 et xfce4-panel).
| Au démarrage de x, une fois identifié, un écran gris s'affiche et rien
  d'autre. Heureusement grâce à mon access SSH je peux me connecter à la
  machine à distance.

Pour voir la liste des paquets déinstallés j'ai donc fait :

``dpkg --get-selections > liste-des-paquets``

Il suffit ensuite d'ouvrir dans un éditeur texte (type vi) le fichier
pour voir les paquets installés / déinstallés. Et réinstaller avec sudo
apt-get install le ou les paquets manquants.

