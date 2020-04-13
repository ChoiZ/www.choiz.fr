Title: Gentoo utilisation de layman & eix
Date: 2015-07-19 10:54:55
Author: choiz
Category: text
Tags: emerge, gentoo
Slug: 2015-07-19-gentoo-utilisation-de-layman-eix
Status: published

Certains programmes n’étant pas en dernière version dans les dépôts
gentoo l’utilisation de layman peut faciliter la vie.

Étant à la recherche de vagrant, la seule version disponible à ce jour
sur gentoo est vagrant-1.4.3-r2… En allant sur le site officiel de
vagrant je me rend compte que nous sommes à la version 1.7.3.

J’ai donc trouvé un overlay avec vagrant-bin version 1.7.3 :
<http://gpo.zugaina.org/app-emulation/vagrant-bin>

Pour utiliser cette overlay nous avons besoin de layman.

Installation :

    emerge -a layman

    echo "source /usr/portage/local/layman/make.conf" >> /etc/make.conf

Pour afficher tous les overlays disponible :

    layman -L

Ajouter l’overlay stefantalpalaru (dans lequel nous avons
vagrant-bin-1.7.3) :

    layman -f -a stefantalpalaru

Maintenant si on recherche dans eix “vagrant” rien n’a changé.

Il faut mettre à jour eix :

    eix-update

Maintenant avec eix vagrant nous avons la ligne vagrant-bin et donc nous
pouvons installer vagrant-1.7.3 via emerge.
