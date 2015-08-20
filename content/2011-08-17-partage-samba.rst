Partage Samba !
###############
:date: 2011-08-17 20:41:00
:author: choiz
:category: text
:tags: Linux, Samba, config, configuration, Partage, Sharing
:slug: 2011-08-17-partage-samba
:status: published

| J'ai réinstallé mon serveur il n'y a pas si longtemps avec Samba. 
| Editer le fichier de configuration :

.. raw:: html

   </p>

    .. raw:: html

       </p>

    vi /etc/samba/smb.conf

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

Voici le contenu de mon fichier de configuration :

.. raw:: html

   </p>

    .. raw:: html

       </p>

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

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

Maintenant il faut créer notre utilisateur "choiz" grâce à :

.. raw:: html

   </p>

    .. raw:: html

       </p>

    smbpasswd -a choiz

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

Pour les groupes samba utilise les groupes unix.

.. raw:: html

   </p>

N'oubliez pas de redémarrer le service Samba !

.. raw:: html

   </p>

    .. raw:: html

       </p>

    /etc/init.d/samba restart

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>
