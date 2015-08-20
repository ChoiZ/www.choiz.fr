imapfilter ou comment filtrer ses mails facilement
##################################################
:date: 2014-03-11 13:54:00
:author: choiz
:category: text
:tags: imapfilter, mail, filter, imap
:slug: 2014-03-11-imapfilter-ou-comment-filtrer-ses-mails-facilement
:status: published

Installer imapfilter via apt par exemple :

.. raw:: html

   </p>

``apt-get install imapfilter``

.. raw:: html

   </p>

Se rendre dans le dossier de configuration :

.. raw:: html

   </p>

``cd ~/.imapfilter``

.. raw:: html

   </p>

Créer un fichier config.lua

.. raw:: html

   </p>

``touch config.lua``

.. raw:: html

   </p>

Maintenant je décide de faire un fichier de configuration par boite
email.

.. raw:: html

   </p>

Ici gmail :

.. raw:: html

   </p>

``cat > gmail.lua <<EOFgmail = IMAP {    server = 'imap.gmail.com',    username = 'mail@gmail.com',    password = 'mon_mot_de_passe',    ssl = 'ssl3',}EOF``

.. raw:: html

   </p>

Et un pour Yahoo :

.. raw:: html

   </p>

``cat > yahoo.lua <<EOFyahoo = IMAP {    server = 'imap.yahoo.com',    username = 'mail@yahoo.com',    password = 'mon_mot_de_passe',    ssl = 'ssl3',}EOF``

.. raw:: html

   </p>

Ajouter nos boites dans le fichier de config avec des filtres :

.. raw:: html

   </p>

``if_dir = os.getenv('HOME') .. '/.imapfilter/'-- on inclus nos comptes imap…dofile(if_dir .. "gmail.lua")dofile(if_dir .. "yahoo.lua")-- nos optionsoptions.timeout = 120-- filtres pour le compte gmail (on copie les messages non lus dans la boite "nouveaux")nonlugmail=gmail.INBOX:is_unseen()nonlugmail:copy_message(gmail['nouveaux'])-- filtres pour le compte yahoo (on supprime tous les messages lus)del_read_yahoo=yahoo.INBOX:is_seen()del_read_yahoo:delete_messages()``

.. raw:: html

   </p>

Maintenant c'est à vous de faire vos propres filtres. Une fois
configuré, lancer imapfilter simplement depuis le terminal :

.. raw:: html

   </p>

``imapfilter``

.. raw:: html

   </p>
