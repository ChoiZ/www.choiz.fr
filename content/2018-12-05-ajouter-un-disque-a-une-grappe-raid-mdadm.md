Title: Ajouter un disque a une grappe RAID MDADM
Date: 2018-12-05 23:22:42
Author: choiz
Category: text
Tags: RAID, MDADM
Slug: 2018-12-05-ajouter-un-disque-a-une-grappe-raid-mdadm
Status: published

Ayant enfin fini la migration de mon NAS vers mon nouveau NAS, j'ai récupéré mon troisième disque de 10To pour l'ajouter à ma grappe RAID1 qui contient déjà 2 disques de 10To.

Pour ajouter le disque /dev/sdd dans la grappe /dev/md0 il faut tapper la commande suivante :

```
mdadm --manage /dev/md0 --add /dev/sdd1
```

Si vous n'avez pas de chance comme moi, vous aurez le message d'erreur suivant :

```
mdadm: Cannot open /dev/sdd1: Device or resource busy
```

Il faut donc redémarrer la machine et éditer le grub à la main… (avec la touche e), puis ajouter dans la ligne avec le kernel `nodmraid` puis appuyer sur f10 ou b pour booter.

Une fois la machine prête j'ai pu lancer ma commande cette fois-ci avec succès :

```
mdadm --manage /dev/md0 --add /dev/sdd1
mdadm: added /dev/sdd1
```

Il faut maintenant dire à MDADM qu'on a un raid1 sur 3 disques avec la commande suivante :

```
mdadm --grow /dev/md0 --raid-device=3
raid_disks for /dev/md0 set to 3
```

Vous pouvez maintenant faire un watch pour voir l'avancement de la copie sur le troisième disque :

```
watch cat /proc/mdstat
```
