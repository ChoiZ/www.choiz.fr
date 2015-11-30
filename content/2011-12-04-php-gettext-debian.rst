PHP + Gettext + Debian
######################
:date: 2011-12-04 19:10:00
:author: choiz
:category: text
:tags: .mo, .po, /etc/locale, LC_ALL, gettext, php, php-gettext, setlocale, xgettext
:slug: 2011-12-04-php-gettext-debian
:status: published

J'utilise maintenant php-gettext pour mes traductions. C'est plus facile en
utilisant des outils tel que pootle ou poedit.  Pour utiliser gettext sur votre
site en php il faut télécharger le package php-gettext ainsi que d'autres outils
tel que xgettext ou msgfmt : ::

    apt-get install php-gettext

    apt-get install xgettext

    apt-get install msgfmt

Ensuite il faut modifier le fichier `/etc/locale.gen` et enlever les
commentaires devant les langues qui vont sont à traduire par exemple :
Allemand, Anglais, Espagnol, Français & Suédois : ::

    de_DE.UTF-8 UTF-8
    en_GB.UTF-8 UTF-8
    es_ES.UTF-8 UTF-8
    fr_FR.UTF-8 UTF-8
    sv_SE.UTF-8 UTF-8

Puis regénérer les locales : ::

    locale-gen

Ensuite il faut définir votre chemin pour les traductions par exemple : ::

    lang/fr_FR/LC_MESSAGES/domaine.mo

Puis dans votre fichier php de configuration : ::

    <?php
    // configuration de la langue
    $lang = 'fr_FR'; // Langue a afficher
    $lang_encode = 'utf8'; // Encodage du fichier
    $lang_path = './lang'; // Chemin des fichiers de langue
    $lang_file = 'domaine'; // Nom du fichier de langue

    putenv('LANG='.$lang.'.'.$lang_encode);
    putenv('LANGUAGE='.$lang.'.'.$lang_encode);
    setlocale(LC_MESSAGES, $lang.'.'.$lang_encode);
    bindtextdomain($lang_file, $lang_path);

    if (function_exists('bind_textdomain_codeset')) {
        bind_textdomain_codeset($lang_file, $lang_encode);
    }

    textdomain($lang_file);
    ?>

Puis faites le test en affichant dans un fichier php le texte "hello" ::

    <?php
    // on inclus la config…
    include_once('config.php');
    echo _('hello');
    ?>

Pour générer un fichier .mo a partir d'un fichier .po : ::

    msgfmt domaine.po -o domaine.mo

Pour générer un fichier .po a partir de fichier php avec du gettext, faire un
fichier texte avec tous vos fichiers php ou on doit récupérer le gettext.

Exemple listing_gettext.txt tel que : ::

    index.php
    contact.php
    etc…

Ensuite il faut faire la commande suivante pour générer le fichier domaine.po
dans le dossier lang/ depuis notre fichier texte avec les php : ::

    find . -iname "*.php" | xargs xgettext --from-code=UTF-8 --default-domain=domaine -p lang/

Pour finir voilà le path des fichiers .po et .mo dans mon application web : ::

    lang/fr_FR/LC_MESSAGES/domaine.po
    lang/fr_FR/LC_MESSAGES/domaine.mo
    lang/en_GB/LC_MESSAGES/domaine.po
    lang/en_GB/LC_MESSAGES/domaine.mo

Mise à jour le 30 Novembre 2015 par `doogaille http://www.github.com/doogaille`_.
