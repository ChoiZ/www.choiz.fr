imapfilter ou comment filtrer ses mails facilement
##################################################
:date: 2014-03-11 13:54:00
:author: choiz
:category: text
:tags: imapfilter, mail, filter, imap
:slug: 2014-03-11-imapfilter-ou-comment-filtrer-ses-mails-facilement
:status: published

Installer imapfilter via apt par exemple :

``apt-get install imapfilter``

Se rendre dans le dossier de configuration :

``cd ~/.imapfilter``

Créer un fichier config.lua

``touch config.lua``

Maintenant je décide de faire un fichier de configuration par boite
email.

Ici gmail :

``cat > gmail.lua <<EOFgmail = IMAP {    server = 'imap.gmail.com',    username = 'mail@gmail.com',    password = 'mon_mot_de_passe',    ssl = 'ssl3',}EOF``

Et un pour Yahoo :

``cat > yahoo.lua <<EOFyahoo = IMAP {    server = 'imap.yahoo.com',    username = 'mail@yahoo.com',    password = 'mon_mot_de_passe',    ssl = 'ssl3',}EOF``

Ajouter nos boites dans le fichier de config avec des filtres :

``if_dir = os.getenv('HOME') .. '/.imapfilter/'-- on inclus nos comptes imap…dofile(if_dir .. "gmail.lua")dofile(if_dir .. "yahoo.lua")-- nos optionsoptions.timeout = 120-- filtres pour le compte gmail (on copie les messages non lus dans la boite "nouveaux")nonlugmail=gmail.INBOX:is_unseen()nonlugmail:copy_message(gmail['nouveaux'])-- filtres pour le compte yahoo (on supprime tous les messages lus)del_read_yahoo=yahoo.INBOX:is_seen()del_read_yahoo:delete_messages()``

Maintenant c'est à vous de faire vos propres filtres. Une fois
configuré, lancer imapfilter simplement depuis le terminal :

``imapfilter``

