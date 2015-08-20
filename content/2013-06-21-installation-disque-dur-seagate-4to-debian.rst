Installation disque dur Seagate 4To Debian
##########################################
:date: 2013-06-21 00:30:00
:author: choiz
:category: text
:tags: debian, disque dur, 4To, partition, fs, config_efi_partition, fdisk, parted, gpt, mkfs
:slug: 2013-06-21-installation-disque-dur-seagate-4to-debian
:status: published

| J'ai investi dans un gros disque dur de 4To pour mes sauvegardes
  (Fichiers persos, photos, vidéos…).
| J'ai donc formaté mon disque avec « Fdisk » et j'ai eu le message
  suivant :

.. raw:: html

   </p>

::

    Warning: invalid flag 0x0000 of partition table 4 will be corrected by w(rite)

    WARNING: The size of this disk is 4.0 TB (4000787030016 bytes).
    DOS partition table format can not be used on drives for volumes
    larger than (2199023255040 bytes) for 512-byte sectors. Use parted(1) and GUID 
    partition table format (GPT).

.. raw:: html

   </p>

J'ai donc vérifié si j'avais dans le noyau l'option
CONFIG\_EFI\_PARTITION active :

.. raw:: html

   </p>

``# cat "/boot/config-`uname -r`" | grep CONFIG_EFI_PARTITION``

.. raw:: html

   </p>

::

    CONFIG_EFI_PARTITION=y

.. raw:: html

   </p>

C'était le cas, donc j'ai un autre problème… C'est « Fdisk » qui pose
problème. Avec ma version (2.20.1) on peut faire une partition maximum
de 2To.

.. raw:: html

   </p>

Donc je me relance dans le partitionnement avec « parted ».

.. raw:: html

   </p>

Note : mon disque est en /dev/sdd n'oubliez pas de modifier les
commandes en fonction de votre configuration.

.. raw:: html

   </p>

``# parted /dev/sdd``

.. raw:: html

   </p>

::

    GNU Parted 2.3
    Using /dev/sdd
    Welcome to GNU Parted! Type 'help' to view a list of commands.

.. raw:: html

   </p>

Définir le label GPT qui permet de faire des partition > 2To.

.. raw:: html

   </p>

``mklabel gpt``

.. raw:: html

   </p>

::

    Warning: The existing disk label on /dev/sdd will be destroyed and all data on this disk will be lost. Do you want to continue?
    Yes/No?

.. raw:: html

   </p>

``yes`` ``unit TB``

.. raw:: html

   </p>

Faire la partition de 4To

.. raw:: html

   </p>

``mkpart primary 0.00TB 4.00TB``

.. raw:: html

   </p>

Vérifier

.. raw:: html

   </p>

``print``

.. raw:: html

   </p>

::

    Model: ATA ST4000DM000-1F21 (scsi)
    Disk /dev/sdd: 4001GB
    Sector size (logical/physical): 512B/4096B
    Partition Table: gpt

    Number  Start   End     Size    File system  Name     Flags
     1      1049kB  4001GB  4001GB               primary

.. raw:: html

   </p>

Quitter « parted »

.. raw:: html

   </p>

``quit``

.. raw:: html

   </p>

::

    Information: You may need to update /etc/fstab.

.. raw:: html

   </p>

Formater la partition avec un système de fichiers donné :

.. raw:: html

   </p>

``# mkfs.ext4 /dev/sdd1``

.. raw:: html

   </p>

::

    mke2fs 1.42.5 (29-Jul-2012)
    Étiquette de système de fichiers=
    Type de système d'exploitation : Linux
    Taille de bloc=4096 (log=2)
    Taille de fragment=4096 (log=2)
    « Stride » = 0 blocs, « Stripe width » = 0 blocs
    244195328 i-noeuds, 976754176 blocs
    48837708 blocs (5.00%) réservés pour le super utilisateur
    Premier bloc de données=0
    Nombre maximum de blocs du système de fichiers=4294967296
    29809 groupes de blocs
    32768 blocs par groupe, 32768 fragments par groupe
    8192 i-noeuds par groupe
    Superblocs de secours stockés sur les blocs : 
        32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208, 
        4096000, 7962624, 11239424, 20480000, 23887872, 71663616, 78675968, 
        102400000, 214990848, 512000000, 550731776, 644972544

    Allocation des tables de groupe : complété                        
    Écriture des tables d'i-noeuds : complété                        
    Création du journal (32768 blocs) : complété
    Écriture des superblocs et de l'information de comptabilité du système de
    fichiers : complété  

.. raw:: html

   </p>

Il ne reste plus qu'a monter la partition et éditer le fstab ;)

.. raw:: html

   </p>
