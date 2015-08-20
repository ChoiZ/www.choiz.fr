Clavier Apple sur debian
########################
:date: 2011-12-02 00:14:00
:author: choiz
:category: text
:tags: Clavier, Apple, Mapage, Debian, Linux, Keyboard, Mac, Mac Keyboard
:slug: 2011-12-02-clavier-apple-sur-debian
:status: published

| Depuis le temps que je bosse avec un clavier Apple [STRIKEOUT:j'ai]
  mes doigts on eu le temps de s'habituer au mapage du clavier. Il y a
  beaucoup de différences entre un clavier AZERTY de PC et un clavier
  AZERTY de Mac.
| Les touches : @ # ~ \| (pipe) = + - \_ ! ( ) { } [ ] sont disposées à
  des endroits complétement différents.

.. raw:: html

   </p>

Pour modifier la configuration faire en console :

.. raw:: html

   </p>

    .. raw:: html

       </p>

    dpkg-reconfigure keyboard-console

    .. raw:: html

       </p>

    Select keymap from arch list

    .. raw:: html

       </p>

    azerty

    .. raw:: html

       </p>

    French

    .. raw:: html

       </p>

    Apple USB

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

    .. raw:: html

       </p>

    dpkg-reconfigure keyboard-configuration

    .. raw:: html

       </p>

    model: Apple

    .. raw:: html

       </p>

    layout: France - Macintosh

    .. raw:: html

       </p>

    Key for AltGr: No AltGr Key

    .. raw:: html

       </p>

    Compose key: Right Alt (AltGr)

    .. raw:: html

       </p>

    Use Control+Alt+Backspace to terminate the X server? no

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

J'ai choisi un clavier Apple, Français Mac, sans touche AltGr, avec
comme touche de fonctionnalité secondaire "Alt droit". Malheureusement
je n'ai pas réussi a mapper l'Alt de gauche pour avoir la même fonction
qu'à droite...

.. raw:: html

   </p>

Et ensuite j'ai indiqué que je ne voulais pas pouvoir quitter le server
X avec la combinaison de touche Control+Alt+Backspace.

.. raw:: html

   </p>

Si ceci ne fonctionne pas il faut se rendre dans la configuration du
clavier de votre gestionnaire de fenêtre (xfce: dans mon cas). Puis
désactiver le layout par defaut du système.

.. raw:: html

   </p>

|image0|

.. raw:: html

   </p>

.. |image0| image:: http://media.tumblr.com/tumblr_lvjsbrOL8E1qzr4hx.png
