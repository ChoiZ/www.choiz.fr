Partage Samba !
###############
:date: 2011-08-17 20:41:00
:author: choiz
:category: text
:tags: Linux, Samba, config, configuration, Partage, Sharing
:slug: 2011-08-17-partage-samba
:status: published

Configuration d'un serveur samba.
Editer le fichier de configuration `/etc/samba/smb.conf`
Voici le contenu de mon fichier de configuration : ::

    | ### Global ###
    | [global]
    | ## Identification ##
    | workgroup = WORKGROUP
    | netbios name = %h
    | server string = Serveur samba %h
    | security = user
    | public = yes
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

Maintenant il faut créer notre utilisateur "choiz" grâce à : ::

    smbpasswd -a choiz

Pour les groupes samba utilise les groupes unix. A vous de voir si vous voulez
gérer votre partage samba utilisateur par utilisateur ou directement avec des
groupes.

N'oubliez pas de redémarrer le service Samba avant de tester depuis votre client
le partage de fichiers ! ::

    /etc/init.d/samba restart
