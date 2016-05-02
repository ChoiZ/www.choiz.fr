Title: Création d'une clé usb xubuntu sur mac
Date: 2014-03-04 14:10:00
Author: choiz
Category: text
Tags: clé usb, xubuntu, mac, terminal, ubuntu
Slug: 2014-03-04-création-dune-clé-usb-xubuntu-sur-mac
Status: published

Dans le terminal sur votre mac :

    diskutil list

Qui permet de lister vos disque dur / clés usb etc…

ici ma clé usb est disk2. :

    /dev/disk2
       #:                       TYPE NAME                    SIZE       IDENTIFIER
       0:     FDisk_partition_scheme                        *8.1 GB     disk2
       1:                      Linux                         4.0 GB     disk2s1
       2:                 Linux_Swap                         4.1 GB     disk2s5

Démontez la clé. :

    diskutil unmountDisk /dev/disk2

    Unmount of all volumes on disk2 was successful

Maintenant on copie xubuntu depuis notre dossier téléchargements vers
cette clé usb :

    sudo dd if=~/Downloads/xubuntu-13.10-desktop-i386.iso of=/dev/rdisk2 bs=1m

    Password:
    834+0 records in
    834+0 records out
    874512384 bytes transferred in 137.915395 secs (6340934 bytes/sec)

Puis on éjecte proprement la clé usb :

    diskutil eject /dev/disk2

    Disk /dev/disk2 ejected
