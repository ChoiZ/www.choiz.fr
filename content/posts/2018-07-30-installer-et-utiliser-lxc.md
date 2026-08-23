---
title: "Installer et utiliser lxc"
date: 2018-07-30T10:48:04
slug: "2018-07-30-installer-et-utiliser-lxc"
author: choiz
tags: ["linux", "lxc", "debian"]
---

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

Se connecter à l'aide de lxc-attach :

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
passwd user
```

> ⚠️ À ne pas oublier : `useradd` seul crée un compte sans mot de passe, donc verrouillé — la connexion SSH échouera tant que vous n'aurez pas lancé `passwd user` (ou déployé une clé SSH publique). Autant l'ajouter tout de suite.

Se déconnecter du conteneur et se connecter via ssh avec votre utilisateur user.
