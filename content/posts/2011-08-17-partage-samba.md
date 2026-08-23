---
title: "Partage Samba !"
date: 2011-08-17T20:41:00
slug: "2011-08-17-partage-samba"
author: choiz
tags: ["linux"]
---

Configuration d'un serveur samba. Éditer le fichier de configuration
/etc/samba/smb.conf Voici le contenu de mon fichier de configuration :

    | ### Global ###
    | [global]
    | ## Identification ##
    | workgroup = WORKGROUP
    | netbios name = %h
    | server string = Serveur samba %h
    | security = user
    | ## Log ##
    | log file = /var/log/samba/log.%m
    | max log size = 1000
    | ## Auth ##
    | encrypt passwords = true
    | smb passwd file = /etc/samba/smbpasswd
    | ### Share ###
    | [choiz]
    | path = /home/choiz/samba
    | read only = no
    | writeable = yes
    | valid users = choiz
    | comment = partage de choiz
    | [partagereadonly]
    | path = /home/partageread
    | read only = yes
    | writeable = no
    | valid users = choiz, @group
    | comment = partage en lecture pour choiz et le groupe "group"

> ⚠️ À ne pas reproduire : j'avais mis `public = yes` dans le `[global]` de cet exemple, ça autorise l'accès invité par défaut sur tout partage qui ne précise pas explicitement `guest ok = no`. Je l'ai retiré du global ; à n'activer, si besoin, que partage par partage.

Maintenant il faut créer notre utilisateur "choiz" grâce à :

    smbpasswd -a choiz

Pour les groupes samba utilise les groupes unix. À vous de voir si vous
voulez gérer votre partage samba utilisateur par utilisateur ou
directement avec des groupes.

N'oubliez pas de redémarrer le service Samba avant de tester depuis
votre client le partage de fichiers ! :

    /etc/init.d/samba restart
