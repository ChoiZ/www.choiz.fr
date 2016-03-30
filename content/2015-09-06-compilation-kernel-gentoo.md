Pour compiler le kernel sous gentoo : :

    cd /usr/src/linux

    make menuconfig

    make && make modules_install

    make install

Le kernel est maintenant compilé.

Maintenant il faut mettre à jour grub. :

    grub2-mkconfig -o /boot/grub/grub.cfg

Puis lancer uname -a qui affiche le kernel actuellement utilisé ainsi
que le nombre de compilation.

Il faut maintenant redémarrer la machine : :

    reboot

Au final vérifier avec uname -a si le bon kernel est chargé.
