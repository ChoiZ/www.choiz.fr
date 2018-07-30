Title: Installer et utiliser lxc
Date: 2018-07-30 10:48:04
Author: choiz
Category: text
Tags: linux, container, lxc
Slug: 2018-07-30-installer-et-utiliser-lxc
Status: published

Installation de lxc sur debian :

```apt-get install lxc```

Création d'un conteneur lxc sous debian :

```lxc-create -n debian9 -t download```

Sélectionner :

```
distribution: debian
Release: strech
Architecture: amd64
```

Lister les conteneurs :

```
lxc-ls -f
NAME        STATE   AUTOSTART GROUPS IPV4 IPV6 
debian9     STOPPED 0         -      -    -
```

Copier debian9 en conteneur debian pour l'utiliser pour un wiki par exemple :

```
lxc-copy -n debian9 -N debian9wiki -B overlay -s
```

Vérifions :

```
lxc-ls -f
NAME        STATE   AUTOSTART GROUPS IPV4 IPV6 
debian9     STOPPED 0         -      -    -    
debian9wiki STOPPED 0         -      -    -
```

Lancer debian9wiki :

```
lxc-start -n debian9wiki
```

Vérifions :

```
lxc-ls -f
NAME        STATE   AUTOSTART GROUPS IPV4           IPV6 
debian9     STOPPED 0         -      -              -    
debian9wiki RUNNING 0         -      192.168.60.140 -    
```

Se connecter a l'aide de lxc-attach :

```
lxc-attach -n debian9wiki
```

Installer openssh-server

```
apt-get install openssh-server
```

Ajouter votre utilisateur user :

```
useradd user
```

Se déconnecter du conteneur et se connecter via ssh avec votre utilisateur user.
