Étant actuellement sur un noyau en version 4.2.0, ci-dessous la marche a
suivre pour le mettre à jour vers la version : 4.3.0.

Je liste les différents noyaux gentoo disponibles : :

    eix sys-kernel/gentoo-sources

Je télécharge le noyau 4.3.0 : :

    emerge -a =sys-kernel/gentoo-sources-4.3.0

Une fois téléchargé, il faut modifier le lien symbolique /usr/src/linux
grâce à eselect.

J'affiche la liste des noyaux (celui actuellement selectionné est suivi
d'une étoile) : :

    eselect kernel list

    [1]     linux-4.2.0-gentoo *
    [2]     linux-4.3.0-gentoo

Pour selectionner notre noyau 4.3.0 il faut utiliser : :

    eselect kernel set 2

Maintenant que vous avez selectionné votre noyau, copier le fichier
".config" de votre noyau précédent (pour conserver vos réglages de
compilation) :

    cp /usr/src/linux-4.2.0-gentoo/.config /usr/src/linux

Puis [compiler votre
kernel](http://www.choiz.fr/2015-09-06-compilation-kernel-gentoo.html).
