PHP + Gettext + Debian
######################
:date: 2011-12-04 19:10:00
:author: choiz
:category: text
:tags: .mo, .po, /etc/locale, LC_ALL, gettext, php, php-gettext, setlocale, xgettext
:slug: 2011-12-04-php-gettext-debian
:status: published

| J'utilise maintenant php-gettext pour mes traductions. C'est plus
  facile en utilisant des outils tel que pootle ou poedit.
| Pour utiliser gettext sur votre site en php il faut télécharger le
  package php-gettext ainsi que d'autres outils tel que xgettext ou
  msgfmt :

.. raw:: html

   </p>

    .. raw:: html

       </p>

    # apt-get install php-gettext

    .. raw:: html

       </p>

    # apt-get install xgettext

    .. raw:: html

       </p>

    # apt-get install msgfmt

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

Ensuite il faut modifier le fichier /etc/locale.gen et enlever les
commentaires devant les langues qui vont sont à traduire par exemple :
Allemand, Anglais, Espagnol, Français & Suédois :

.. raw:: html

   </p>

    .. raw:: html

       </p>

    | de\_DE.UTF-8 UTF-8
    | en\_GB.UTF-8 UTF-8
    | es\_ES.UTF-8 UTF-8
    | fr\_FR.UTF-8 UTF-8
    | sv\_SE.UTF-8 UTF-8

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

Puis regénérer les locales :

.. raw:: html

   </p>

    .. raw:: html

       </p>

    # locale-gen

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

Ensuite il faut définir votre chemin pour les traductions par exemple :

.. raw:: html

   </p>

    .. raw:: html

       </p>

    lang/fr\_FR/LC\_ALL/domaine.mo

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

Puis dans votre fichier php de configuration :

.. raw:: html

   </p>

    .. raw:: html

       </p>

    | <?php
    | // configuration de la langue
    | $lang\_path = "./lang"; // Chemin des fichiers le langue
    | $lang = 'fr\_FR'; // Langue a afficher
    | $lang\_encode = "UTF-8"; // Encodage du fichier
    | $lang\_LC = "LC\_ALL"; // LC\_MESSAGE etc...
    | $lang\_file = "domaine"; // Nom du fichier de langue
    | putenv("LANG=".$lang);
    | setlocale($lang\_LC, $lang.".".$lang\_encode);
    | bindtextdomain($lang\_file,$lang\_path);
    | bindtextdomain\_codeset($lang\_file,$lang\_encode);
    | textdomain($lang\_path);
    | ?>

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

Puis faites le test en affichant dans un fichier php le texte "hello"

.. raw:: html

   </p>

    .. raw:: html

       </p>

    | <?php
    | // on inclus la config...
    | include\_once('config.php');
    | echo \_('hello');
    | ?>

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

Pour générer un fichier .mo a partir d'un fichier .po :

.. raw:: html

   </p>

    .. raw:: html

       </p>

    msgfmt domaine.po -o domaine.mo

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

Pour générer un fichier .po a partir de fichier php avec du gettext,
faire un fichier texte avec tous vos fichiers php ou on doit récupérer
le gettext.

.. raw:: html

   </p>

Exemple listing\_gettext.txt tel que :

.. raw:: html

   </p>

    .. raw:: html

       </p>

    | index.php
    | contact.php
    | etc...

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

Ensuite il faut faire la commande suivante pour générer le fichier
domaine.po dans le dossier lang/ depuis notre fichier texte avec les php
:

.. raw:: html

   </p>

    .. raw:: html

       </p>

    xgettext -d domaine -p lang/ -k\_ --from-code=UTF-8 -f
    listing\_gettext.txt

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

Pour finir voilà le path des fichiers .po et .mo dans mon application
web :

.. raw:: html

   </p>

    .. raw:: html

       </p>

    | lang/fr\_FR/LC\_ALL/domaine.po
    | lang/fr\_FR/LC\_ALL/domaine.mo
    | lang/en\_GB/LC\_ALL/domaine.po
    |  lang/en\_GB/LC\_ALL/domaine.mo
    | ...

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>
