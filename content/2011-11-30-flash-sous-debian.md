Lors de l'installation de Debian sur mon poste au travail j'ai eu la
surprise en ouvrant Firefox que Deezer ne fonctionne pas ! Travaillant
chez Deezer c'est un peu problèmatique.

J'ai donc téléchargé le package flashplugin-nonfree en procédant comme
ceci : :

    vi /etc/apt/source.list

Ajouter contrib non-free aux différentes sources (sauf security) puis :
:

    apt-get update

    apt-get install flashplugin-nonfree

En relançant Firefox j'ai bien flash player fonctionnel sur Deezer.

Le package flashplugin étant nonfree Debian ne l'inclus pas directement
lors de l'installation.
