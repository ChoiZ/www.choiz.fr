Flash sous Debian
#################
:date: 2011-11-30 22:52:56
:author: choiz
:category: text
:tags: Flash, Debian, Deezer, Firefox, flashplugin, source, apt, souce.list, non-free, contrib
:slug: 2011-11-30-flash-sous-debian
:status: published

| Lors de l'installation de debian j'ai eu la surprise en ouvrant
  Firefox que Deezer ne fonctionne pas !
| Il faut donc télécharger le package flashplugin-nonfree en procédant
  comme ceci :

.. raw:: html

   </p>

    .. raw:: html

       </p>

    vi /etc/apt/source.list

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

ajouter contrib non-free aux différentes sources (sauf security)

.. raw:: html

   </p>

puis faire :

.. raw:: html

   </p>

    .. raw:: html

       </p>

    apt-get update

    .. raw:: html

       </p>

    apt-get install flashplugin-nonfree

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

En relançant Firefox j'ai bel et bien flash player fonctionnel sur
Deezer.

.. raw:: html

   </p>
