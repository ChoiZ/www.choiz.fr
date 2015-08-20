Création d'une clé usb xubuntu sur mac
######################################
:date: 2014-03-04 14:10:00
:author: choiz
:category: text
:tags: clé usb, xubuntu, mac, terminal, ubuntu
:slug: 2014-03-04-création-dune-clé-usb-xubuntu-sur-mac
:status: published

Dans le terminal sur votre mac :

.. raw:: html

   </p>

``$ diskutil list``

.. raw:: html

   </p>

Qui permet de lister vos disque dur / clés usb etc…

.. raw:: html

   </p>

ici ma clé usb est disk2.

.. raw:: html

   </p>

::

    /dev/disk2
       #:                       TYPE NAME                    SIZE       IDENTIFIER
       0:     FDisk_partition_scheme                        *8.1 GB     disk2
       1:                      Linux                         4.0 GB     disk2s1
       2:                 Linux_Swap                         4.1 GB     disk2s5

.. raw:: html

   </p>

Démontez la clé.

.. raw:: html

   </p>

``$ diskutil unmountDisk /dev/disk2``

.. raw:: html

   </p>

::

    Unmount of all volumes on disk2 was successful

.. raw:: html

   </p>

Maintenant on copie xubuntu depuis notre dossier téléchargements vers
cette clé usb :

.. raw:: html

   </p>

``$ sudo dd if=~/Downloads/xubuntu-13.10-desktop-i386.iso of=/dev/rdisk2 bs=1m``

.. raw:: html

   </p>

::

    Password:
    834+0 records in
    834+0 records out
    874512384 bytes transferred in 137.915395 secs (6340934 bytes/sec)

.. raw:: html

   </p>

Puis on éjecte proprement la clé usb

.. raw:: html

   </p>

``$ diskutil eject /dev/disk2``

.. raw:: html

   </p>

::

    Disk /dev/disk2 ejected

.. raw:: html

   </p>

Et voilà

.. raw:: html

   </p>
