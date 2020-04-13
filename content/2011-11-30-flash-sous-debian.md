Title: Flash sous Debian
Date: 2011-11-30 22:52:56
Author: choiz
Category: text
Tags: debian, linux
Slug: 2011-11-30-flash-sous-debian
Status: published

Lors de l'installation de Debian sur mon poste au travail j'ai eu la
surprise en ouvrant Firefox que Deezer ne fonctionne pas ! Travaillant
chez Deezer c'est un peu problèmatique.

J'ai donc téléchargé le package flashplugin-nonfree en procédant comme
ceci :

    vi /etc/apt/source.list

Ajouter contrib non-free aux différentes sources (sauf security) puis :

    apt-get update

    apt-get install flashplugin-nonfree

En relançant Firefox j'ai bien flash player fonctionnel sur Deezer.

Le package flashplugin étant nonfree Debian ne l'inclus pas directement
lors de l'installation.
