Configurer un serveur mail
############################
:date: 2015-11-15 17:11:23
:author: choiz
:category: text
:tags: mail, postfix, dovecot, dns
:slug: 2015-11-15-configurer-un-serveur-mail
:status: published

Installation d'un serveur mail complet et à jour sous debian jessie (8.2).

Pour commencer nous allons créer des entrées DNS.

Nous créons un MX pour les mails avec une priorité de 1, un sous domaine "mail" qui pointe vers l'adresse ipv4 de votre serveur et un sous domaine webmail qui pointe sur le sous domaine mail. ::

    votredomaine.com.           MX      1   mail.votredomaine.com.
    mail.votredomaine.com.      A           ip.v4.du.serveur
    webmail.votredomaine.com.   CNAME       mail.votredomaine.com.

Maintenant installons postfix et dovecot-imapd : ::

    apt-get install postfix dovecot-imapd

Configurer le serveur de messagerie comme "Site Internet", puis en nom de courrier indiquer "mail.votredomaine.com".

Créer un dossier ssl dans dovecot : ::

    mkdir /etc/dovecot/ssl && cd /etc/dovecot/ssl

Créer un certificat ssl : ::

    openssl req -new -newkey rsa:2048 -nodes -keyout certificat.key -out certificat.csr

Puis répondre aux différentes questions pour ma part j'ai répondu : ::

    FR
    (vide)
    Paris
    votredomaine
    IT
    mail.votredomaine.com
    contact@votredomaine.com
    (vide)
    (vide)

Ensuite : ::

    openssl x509 -req -days 365 -in certificat.csr -signkey certificat.key -out certificat.crt

Puis : ::

    cat certificat.key certificat.crt > certificat.pem

Créer le groupe et l'utilisateur vmail : ::

    groupadd -g 5000 vmail
    useradd -m -d /var/vmail -s /bin/false -u 5000 -g vmail vmail

Ajouter dans /etc/dovecot/dovecot.conf ::

    listen = ip.v4.du.server

Editer /etc/dovecot/conf.d/10-auth.conf ::

    disable_plaintext_auth = yes
    auth_username_format = %Lu
    #!include auth-system.conf.ext
    !include auth-passwdfile.conf.ext

Editer /etc/dovecot/conf.d/10-logging.conf ::

    auth_verbose = yes
    mail_debug = yes

Editer /etc/dovecot/conf.d/10-ssl.conf ::

    ssl = required
    ssl_cert = </etc/dovecot/ssl/certificat.pem
    ssl_key = </etc/dovecot/ssl/certificat.key

Editer /etc/dovecot/conf.d/15-mailboxes.conf ::

    mailbox Drafts {
        auto = subscribe
        special_use = \Drafts
    }

    mailbox Junk {
        auto = subscribe
        special_use = \Junk
    }

    mailbox Trash {
        auto = subscribe
        special_use = \Trash
    }

    mailbox Sent {
        auto = subscribe
        special_use = \Sent
    }

    #mailbox "Sent Messages" {
    #    special_use = \Sent
    #}

Editer /etc/dovecot/conf.d/auth-passwdfile.conf.ext ::

    passdb {
        driver = passwd-file
        args = scheme=MD5 username_format=%u /etc/dovecot/users
    }

    userdb {
        driver = passwd-file
        args = username_format=%u /etc/dovecot/users
        default_fields = uid=5000 gid=5000 home=/var/vmail/%d mail=maildir:~/%u
    }

Créer le fichier /etc/dovecot/users ::

    touch /etc/dovecot/users

Puis pour chaque mail créer un enregistrement : ::

    adresse@votredomaine.com:motdepassemd5:::::::

Le format est le suivant :

================== ================================
Champ              Valeur
================== ================================
Adresse email      adresse@votredomaine.com
------------------ --------------------------------
Mot de passe (MD5) motdepassemd5
------------------ --------------------------------
uid                déjà défini dans auth-passwdfile
------------------ --------------------------------
gid                déjà défini dans auth-passwdfile
------------------ --------------------------------
home directory     déjà défini dans auth-passwdfile
------------------ --------------------------------
mail directory     déjà défini dans auth-passwdfile
================== ================================

Tester votre utilisateur grâce à la commande : ::

    doveadm user adresse@votredomaine.com

Ce qui devrait afficher : ::

    field   value
    uid     5000
    gid     5000
    home    /var/vmail/votredomaine.com
    mail    maildir:~/adresse@votredomaine.com

Démarrer dovecot : ::

    /etc/init.d/dovecot start

Tester la connexion : ::

    openssl s_client -connect ip.v4.du.server:993

Si vous avez "* OK [CAPABILITY …] Dovecot ready.
Vous pouvez vous authentifier : ::

    . LOGIN adresse@votredomaine.com motdepasseenclair

C'est fini pour dovecot.

Prochaine étape postfix !
