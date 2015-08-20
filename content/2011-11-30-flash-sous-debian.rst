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

    vi /etc/apt/source.list

ajouter contrib non-free aux différentes sources (sauf security)

puis faire :

    apt-get update

    apt-get install flashplugin-nonfree

En relançant Firefox j'ai bel et bien flash player fonctionnel sur
Deezer.

