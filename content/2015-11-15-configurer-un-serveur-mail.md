Configurer un serveur mail
==========================

date  
2015-11-15 17:11:23

author  
choiz

category  
text

tags  
mail, postfix, dovecot, dns, ssl, rainloop, webmail

slug  
2015-11-15-configurer-un-serveur-mail

status  
published

Installation d'un serveur mail complet et à jour sous debian jessie
(8.2).

Configuration des DNS
---------------------

Pour commencer nous allons créer des entrées DNS.

Nous créons un MX pour les mails avec une priorité de 1, un sous domaine
"mail" qui pointe vers l'adresse ipv4 de votre serveur, d'un sous
domaine webmail qui pointe sur le sous domaine mail et d'un
enregistrement SPF :

    votredomaine.com.           MX      1   mail.votredomaine.com.
    mail.votredomaine.com.      A           ip.v4.du.serveur
    webmail.votredomaine.com.   CNAME       mail.votredomaine.com.
    votredomain.com.            SPF         "v=spf1 ip4:ip.v4.du.server ~all"

Installation des paquets
------------------------

Maintenant installons postfix dovecot-imapd et sasl2-bin : :

    apt-get install postfix dovecot-imapd sasl2-bin php5-curl

Configurer le serveur de messagerie comme "Site Internet", puis en nom
de courrier indiquer "mail.votredomaine.com".

Configuration de dovecot
------------------------

Créer un dossier ssl dans dovecot : :

    mkdir /etc/dovecot/ssl && cd /etc/dovecot/ssl

Créer un certificat ssl : :

    openssl req -new -newkey rsa:2048 -nodes -keyout certificat.key -out certificat.csr

Puis répondre aux différentes questions pour ma part j'ai répondu : :

    FR
    (vide)
    Paris
    votredomaine
    IT
    mail.votredomaine.com
    contact@votredomaine.com
    (vide)
    (vide)

Ensuite : :

    openssl x509 -req -days 365 -in certificat.csr -signkey certificat.key -out certificat.crt

Puis : :

    cat certificat.key certificat.crt > certificat.pem

Créer le groupe et l'utilisateur vmail : :

    groupadd -g 5000 vmail
    useradd -m -d /var/vmail -s /bin/false -u 5000 -g vmail vmail

Ajouter dans /etc/dovecot/dovecot.conf :

    listen = ip.v4.du.server

Editer /etc/dovecot/conf.d/10-auth.conf :

    disable_plaintext_auth = yes
    auth_username_format = %Lu
    #!include auth-system.conf.ext
    !include auth-passwdfile.conf.ext

Editer /etc/dovecot/conf.d/10-logging.conf :

    auth_verbose = yes
    mail_debug = yes

Editer /etc/dovecot/conf.d/10-master.conf :

    unix_listener /var/spool/postfix/private/auth {
      mode = 0666
      user = postfix
      group = postfix
    }

Editer /etc/dovecot/conf.d/10-ssl.conf :

    ssl = required
    ssl_cert = </etc/dovecot/ssl/certificat.pem
    ssl_key = </etc/dovecot/ssl/certificat.key

Editer /etc/dovecot/conf.d/15-mailboxes.conf :

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

Editer /etc/dovecot/conf.d/auth-passwdfile.conf.ext :

    passdb {
        driver = passwd-file
        args = scheme=MD5 username_format=%u /etc/dovecot/users
    }

    userdb {
        driver = passwd-file
        args = username_format=%u /etc/dovecot/users
        default_fields = uid=5000 gid=5000 home=/var/vmail/%d mail=maildir:~/%u
    }

Créer le fichier /etc/dovecot/users :

    touch /etc/dovecot/users

Puis pour chaque mail créer un enregistrement : :

    adresse@votredomaine.com:motdepassemd5:::::::

Le format est le suivant :

<table>
<thead>
<tr class="header">
<th align="left">Champ</th>
<th align="left">Valeur</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Adresse email</td>
<td align="left"><script type="text/javascript">
<!--
h='&#118;&#x6f;&#116;&#114;&#x65;&#100;&#x6f;&#x6d;&#x61;&#x69;&#110;&#x65;&#46;&#x63;&#x6f;&#x6d;';a='&#64;';n='&#x61;&#100;&#114;&#x65;&#x73;&#x73;&#x65;';e=n+a+h;
document.write('<a h'+'ref'+'="ma'+'ilto'+':'+e+'" clas'+'s="em' + 'ail">'+e+'<\/'+'a'+'>');
// -->
</script><noscript>&#x61;&#100;&#114;&#x65;&#x73;&#x73;&#x65;&#32;&#x61;&#116;&#32;&#118;&#x6f;&#116;&#114;&#x65;&#100;&#x6f;&#x6d;&#x61;&#x69;&#110;&#x65;&#32;&#100;&#x6f;&#116;&#32;&#x63;&#x6f;&#x6d;</noscript></td>
</tr>
<tr class="even">
<td align="left">------------------</td>
<td align="left">--------------------------------</td>
</tr>
<tr class="odd">
<td align="left">Mot de passe (MD5)</td>
<td align="left">motdepassemd5</td>
</tr>
<tr class="even">
<td align="left">------------------</td>
<td align="left">--------------------------------</td>
</tr>
<tr class="odd">
<td align="left">uid</td>
<td align="left">déjà défini dans auth-passwdfile</td>
</tr>
<tr class="even">
<td align="left">------------------</td>
<td align="left">--------------------------------</td>
</tr>
<tr class="odd">
<td align="left">gid</td>
<td align="left">déjà défini dans auth-passwdfile</td>
</tr>
<tr class="even">
<td align="left">------------------</td>
<td align="left">--------------------------------</td>
</tr>
<tr class="odd">
<td align="left">home directory</td>
<td align="left">déjà défini dans auth-passwdfile</td>
</tr>
<tr class="even">
<td align="left">------------------</td>
<td align="left">--------------------------------</td>
</tr>
<tr class="odd">
<td align="left">mail directory</td>
<td align="left">déjà défini dans auth-passwdfile</td>
</tr>
</tbody>
</table>

Tester votre utilisateur grâce à la commande : :

    doveadm user adresse@votredomaine.com

Ce qui devrait afficher : :

    field   value
    uid     5000
    gid     5000
    home    /var/vmail/votredomaine.com
    mail    maildir:~/adresse@votredomaine.com

Démarrer dovecot : :

    /etc/init.d/dovecot start

Tester la connexion : :

    openssl s_client -connect ip.v4.du.server:993

Si vous avez "\* OK \[CAPABILITY …\] Dovecot ready. Vous pouvez vous
authentifier : :

    . LOGIN adresse@votredomaine.com motdepasseenclair

C'est fini pour dovecot.

Configuration de sasl
---------------------

Editer /etc/default/saslauthd : :

    START=yes
    OPTIONS="-m /var/spool/postfix/var/run/saslauthd"

Puis lancer : :

    /etc/init.d/saslauthd start

C'est fini pour sasl

Configuration de postfix
------------------------

Editer /etc/postfix/main.cf : ::

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

    smtpd_enforce_tls = no
    smtpd_tls_auth_only = no
    smtpd_tls_ask_ccert = no
    smtpd_tls_received_header = yes
    tls_random_source = dev:/dev/urandom

Créer /etc/postfix/virtual\_alias : :

    touch /etc/postfix/virtual_alias

Pour créer un alias, éditer /etc/postfix/virtual\_alias : :

    alias@votredomaine.com          destination@votredomaine.com

Créer /etc/postfix/virtual\_domains : :

    touch /etc/postfix/virtual_domains

Pour gérer vos domaines, éditer /etc/postfix/virtual\_domains : :

    votredomaine.com                OK
    votredeuxiemedomaine.com        OK

Créer /etc/postfix/virtual\_mailbox : :

    touch /etc/postfix/virtual_mailbox

Pour créer un comte mail, éditer /etc/postfix/virtual\_mailbox : :

    email@votredomaine.com          votredomaine.com/email@votredomaine.com/
    linus@torvald.com               torvald.com/linus@torvald.com/

N'oubliez pas lors de la création de nouveau comptes mail d'éditer
/etc/dovecot/users ;-)

Maintenant il faut dire a postfix que nous avons modifier nos fichiers
virtuels : :

    postmap /etc/postfix/virtual_alias
    postmap /etc/postfix/virtual_domains
    postmap /etc/postfix/virtual_mailbox

Editer /etc/postfix/master.cf : :

    smtp    inet    n   -   -   -   -   smtpd   -v
     -o smtpd_tls_cert_file=/etc/dovecot/ssl/certificat.pem
     -o smtpd_tls_key_file=/etc/dovecot/ssl/certificat.key
    submission inet n - n - - smtpd
     -o smtpd_tls_security_level=encrypt
     -o smtpd_sasl_auth_enable=yes
    urd inet n - n - - smtpd
     -o smtpd_tls_wrappermode=yes
     -o smtpd_sasl_auth_enable=yes
    smtps   inet    n   -   -   -   -   smtpd   -v
     -o smtpd_tls_wrappermode=yes
     -o smtpd_tls_cert_file=/etc/dovecot/ssl/certificat.pem
     -o smtpd_tls_key_file=/etc/dovecot/ssl/certificat.key

Puis redemarrer postfix : :

    /etc/init.d/postfix restart

Fin de la configuration de postfix.

Vous pouvez maintenant tester votre serveur mail ainsi que la qualité de
votre serveur sur le site <http://www.mail-tester.com>

Installation d'un webmail rainloop
----------------------------------

Créer un dossier pour votre webmail : :

    mkdir -p /var/www/webmail/public && cd /var/www/webmail/public

Télécharger rainloop : :

    wget http://repository.rainloop.net/v2/webmail/rainloop-community-latest.zip

Décompresser rainloop : :

    unzip rainloop*.zip && rm -rf rainloop*.zip

Modifier les droits : :

    chown -R www-data:www-data /var/www/webmail
    find . -type f -exec chmod 644 {} \;
    find . -type d -exec chmod 755 {} \;

Créer un vhost pour apache dans
/etc/apache2/site-enabled/001-webmail.domain.com.conf :

    <VirtualHost *:80>
        ServerAdmin contact@domain.com
        ServerName mail.domain.com

        DocumentRoot /var/www/webmail/public
        <Directory /var/www/webmail/public>
            Options FollowSymLinks
            #Options Indexes FollowSymLinks MultiViews
            AllowOverride All
            Order allow,deny
            allow from all
        </Directory>

        <Directory /var/www/webmail/public/data>
            Options -FollowSymLinks
            AllowOverride None
            Order allow,deny
            Deny from all
        </Directory>

        ErrorLog ${APACHE_LOG_DIR}/webmail_error.log

        # Possible values include: debug, info, notice, warn, error, crit,
        # alert, emerg.
        LogLevel warn

        CustomLog ${APACHE_LOG_DIR}/webmail_access.log combined
    </VirtualHost>

N'oubliez pas de redémarrer apache : :

    /etc/init.d/apache2 restart

Pour configurer rainloop se rendre sur : <http://mail.domain.com/?admin>

<table>
<thead>
<tr class="header">
<th align="left">Login</th>
<th align="left">admin</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Password</td>
<td align="left">12345</td>
</tr>
</tbody>
</table>

Changer la langue et votre mot de passe (dans security).

Puis dans domains configurez votre nom de domaine en cliquant sur + Add
domain

<table>
<thead>
<tr class="header">
<th align="left">Name</th>
<th align="left">domaine.com</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">============</td>
<td align="left">===========================</td>
</tr>
<tr class="even">
<td align="left">IMAP</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left">============</td>
<td align="left">===========================</td>
</tr>
<tr class="even">
<td align="left">Server</td>
<td align="left">mail.domain.com</td>
</tr>
<tr class="odd">
<td align="left">------------</td>
<td align="left">---------------------------</td>
</tr>
<tr class="even">
<td align="left">Secure</td>
<td align="left">SSL/TLS</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th align="left">SMTP</th>
<th align="left"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Server</td>
<td align="left">mail.domain.com</td>
</tr>
<tr class="even">
<td align="left">------------</td>
<td align="left">---------------------------</td>
</tr>
<tr class="odd">
<td align="left">Secure</td>
<td align="left">SSL/TLS</td>
</tr>
</tbody>
</table>

Puis + Add

Je supprime tous les autres domaines (gmail etc…)

Ensuite j'active les plugins, et les packages : X-Originating-IP, Black
list et White list.

Maintenant rendez-vous sur : <http://mail.domain.com> et identifiez-vous
avec votre login et mot de passe.
