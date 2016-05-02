Title: Compilation Kernel Gentoo
Date: 2015-09-06 11:48:24
Author: choiz
Category: text
Tags: compilation, kernel, gentoo
Slug: 2015-09-06-compilation-kernel-gentoo
Status: published

Pour compiler le kernel sous gentoo :

    cd /usr/src/linux

    make menuconfig

    make && make modules_install

    make install

Le kernel est maintenant compilé.

Maintenant il faut mettre à jour grub. :

    grub2-mkconfig -o /boot/grub/grub.cfg

Puis lancer uname -a qui affiche le kernel actuellement utilisé ainsi
que le nombre de compilation.

Il faut maintenant redémarrer la machine :

    reboot

Au final vérifier avec uname -a si le bon kernel est chargé.
