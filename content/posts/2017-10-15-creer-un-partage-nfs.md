---
title: "Créer un partage NFS"
date: 2017-10-15T19:52:13
slug: "2017-10-15-creer-un-partage-nfs"
author: choiz
tags: ["nfs", "linux", "debian", "gentoo"]
---

Pour installer un serveur NFS sur Debian voici la marche à suivre :
```
apt install nfs-kernel-server
```

Une fois le paquet installé, il faut modifier la configuration pour ajouter
votre partage.

Editer le fichier `/etc/exports`
```
vim /etc/exports
```

J'ajoute dans le fichier le dossier à partager `/home/user/share` et l'adresse
du ou des clients qui peuvent accéder à ce partage
`10.0.0.1(rw,sync,no_subtree_check)` ici mon client a l'adresse ip 10.0.0.1 ce
qui donne :
```
/home/user/share 10.0.0.1(rw,sync,no_subtree_check)
```

Recharger le service :
```
service nfs-kernel-server reload
```

Vérifier que votre partage est bien actif :
```
showmount -e
```

Côté client, j'ai installé sur Gentoo : `net-fs/nfs-utils`
```
emerge -a net-fs/nfs-utils
```

Sur Debian installer le paquet : `nfs-common`
```
apt install nfs-common
```

Ensuite configurer votre fichier `/etc/fstab`
```
vim /etc/fstab
```

Ajouter à la fin du fichier l'ip de votre partage avec le nom local puis le
point de montage sur votre client.
```
10.0.0.100:/home/user/share /home/user/nfs-nas nfs defaults,user,auto,noatime,intr 0 0
```

Puis monter le nouveau partage avec la commande `mount -a`

Si vous faites la commande `ls /home/user/nfs-nas` vous devriez voir les
fichiers qui se trouvent sur votre serveur.
