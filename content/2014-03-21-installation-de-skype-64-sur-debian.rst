Installation de Skype 64 sur Debian
###################################
:date: 2014-03-21 01:32:18
:author: choiz
:category: text
:tags: Skype, Debian, Installation de Skype, Skype Debian 64, Debian 64
:slug: 2014-03-21-installation-de-skype-64-sur-debian
:status: published

Télécharger la dernière version de `Skype <http://www.skype.com>`__
(Debian 7.0 [multiarch]).

Ajouter l'achitecture i386 si vous ne l'avez pas déjà fait.

``dpkg --add-architecture i386``

Puis mettre à jour les paquets

``apt-get update``

``apt-get upgrade``

``apt-get install -f``

Installer Skype en n'oubliant pas de remplacer "x" par la bonne version

``dpkg -i skype-debian_x_i386.deb``

