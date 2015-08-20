Gentoo utilisation de layman & eix
##################################
:date: 2015-07-19 10:54:55
:author: choiz
:category: text
:tags: dépôt, repos, layman, eix, emerge, gentoo, vagrant-bin, overlay
:slug: 2015-07-19-gentoo-utilisation-de-layman-eix
:status: published

Certains programmes n’étant pas en dernière version dans les dépôts
gentoo l’utilisation de layman peut faciliter la vie.

.. raw:: html

   </p>

Étant à la recherche de vagrant, la seule version disponible à ce jour
sur gentoo est vagrant-1.4.3-r2… En allant sur le site officiel de
vagrant je me rend compte que nous sommes à la version 1.7.3.

.. raw:: html

   </p>

J’ai donc trouvé un overlay avec vagrant-bin version 1.7.3 :
http://gpo.zugaina.org/app-emulation/vagrant-bin

.. raw:: html

   </p>

Pour utiliser cette overlay nous avons besoin de layman.

Installation :

.. raw:: html

   </p>

``emerge -a layman``

``echo "source /usr/portage/local/layman/make.conf" >> /etc/make.conf``

Pour afficher tous les overlays disponible :

.. raw:: html

   </p>

``layman -L``

Ajouter l’overlay stefantalpalaru (dans lequel nous avons
vagrant-bin-1.7.3)

.. raw:: html

   </p>

``layman -f -a stefantalpalaru``

Maintenant si on recherche dans eix “vagrant” rien n’a changé.

Il faut mettre à jour eix :

.. raw:: html

   </p>

``eix-update``

Maintenant avec eix vagrant nous avons la ligne vagrant-bin et donc nous
pouvons installer vagrant-1.7.3 via emerge.

.. raw:: html

   </p>
