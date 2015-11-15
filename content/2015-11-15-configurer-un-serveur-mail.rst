Configurer un serveur mail
############################
:date: 2015-11-15 17:11:23
:author: choiz
:category: text
:tags: mail, postfix, dovecot, dns
:slug: 2015-11-15-configurer-un-serveur-mail
:status: published

Installation d'un serveur mail complet et à jour sous debian jessie (8.2).

Configuration des DNS
=====================

Pour commencer nous allons créer des entrées DNS.

Nous créons un MX pour les mails avec une priorité de 1, un sous domaine "mail" qui pointe vers l'adresse ipv4 de votre serveur, d'un sous domaine webmail qui pointe sur le sous domaine mail et d'un enregistrement SPF ::

    votredomaine.com.           MX      1   mail.votredomaine.com.
    mail.votredomaine.com.      A           ip.v4.du.serveur
    webmail.votredomaine.com.   CNAME       mail.votredomaine.com.
    votredomain.com.            SPF         "v=spf1 ip4:ip.v4.du.server ~all"

Installation des paquets
========================

Maintenant installons postfix dovecot-imapd et sasl2-bin : ::

    apt-get install postfix dovecot-imapd sasl2-bin

Configurer le serveur de messagerie comme "Site Internet", puis en nom de courrier indiquer "mail.votredomaine.com".

Configuration de dovecot
========================

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

Editer /etc/dovecot/conf.d/10-master.conf ::

    unix_listener /var/spool/postfix/private/auth {
      mode = 0666
      user = postfix
      group = postfix
    }

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

Configuration de sasl
=====================

Editer /etc/default/saslauthd : ::

    START=yes
    OPTIONS="-m /var/spool/postfix/var/run/saslauthd"

Puis lancer : ::

    /etc/init.d/saslauthd start

C'est fini pour sasl

Configuration de postfix
========================

Editer /etc/postfix/main.cf : :::

    smtpd_banner = $myhostname ESMTP $mail_name
    smtpd_tls_cert_file=/etc/dovecot/ssl/certificat.pem
    smtpd_tls_key_file=/etc/dovecot/ssl/certificat.key
    mynetworks = 127.0.0.0/8 ip.v4.du.server

    virtual_mailbox_domains = votredomaine.com, autredomaine.com
    virtual_mailbox_base = /var/vmail
    virtual_mailbox_maps = hash:/etc/postfix/virtual_mailbox
    virtual_minimum_uid = 100
    virtual_uid_maps = static:5000
    virtual_gid_maps = static:5000
    virtual_alias_maps = hash:/etc/postfix/virtual_alias

    smtpd_sasl_auth_enable = yes
    smtpd_sasl_type = dovecot
    smtpd_sasl_path = private/auth
    smtpd_sasl_security_options = noanonymous
    smtpd_sasl_tls_security_options = noanonymous
    smtpd_sasl_local_domain = $myhostname

    broken_sasl_auth_clients = yes

    smtpd_helo_restrictions = reject_unknown_helo_hostname
    smtpd_sender_restrictions = permit_sasl_authenticated reject_unknown_sender_domain
    smtpd_recipient_restrictions = permit_sasl_authenticated permit_mynetworks reject_unauth_destination
    smtpd_enforce_tls = yes
    smtpd_tls_auth_only = yes
    smtpd_tls_ask_ccert = no
    smtpd_tls_received_header = yes

Créer /etc/postfix/virtual_alias : ::

    touch /etc/postfix/virtual_alias

Pour créer un alias, éditer /etc/postfix/virtual_alias : ::

    alias@votredomaine.com          destination@votredomaine.com

Créer /etc/postfix/virtual_domains : ::

    touch /etc/postfix/virtual_domains

Pour gérer vos domaines, éditer /etc/postfix/virtual_domains : ::

    votredomaine.com                OK
    votredeuxiemedomaine.com        OK

Créer /etc/postfix/virtual_mailbox : ::

    touch /etc/postfix/virtual_mailbox

Pour créer un comte mail, éditer /etc/postfix/virtual_mailbox : ::

    email@votredomaine.com          votredomaine.com/email@votredomaine.com/
    linus@torvald.com               torvald.com/linus@torvald.com/

N'oubliez pas lors de la création de nouveau comptes mail d'éditer /etc/dovecot/users ;-)

Maintenant il faut dire a postfix que nous avons modifier nos fichiers virtuels : ::

    postmap /etc/postfix/virtual_alias
    postmap /etc/postfix/virtual_domains
    postmap /etc/postfix/virtual_mailbox

Puis redemarrer postfix : ::

    /etc/init.d/postfix restart

Fin de la configuration de postfix
