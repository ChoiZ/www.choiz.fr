Pour initialiser les sous-modules dans git j'utilise la commande
suivante : :

    git submodule init

Ensuite je dois faire un update des sous-modules pour charger le contenu
: :

    git submodule update

Pour faire les deux en même temps (init + update) vous pouvez faire : :

    git submodule update --init

Imaginons maintenant que vous avez des sous-modules dans d'autres
sous-modules. Exemple dans mon dépot
[dotfiles](https://www.github.com/ChoiZ/dotfiles.git) j'ai mon dépot
[vim](https://www.github.com/ChoiZ/vim-config.git) et dedans des
sous-modules avec les plugins de vim. Pour initialiser, mettre à jour et
le tout en cascade (dans tous les dossiers et sous-dossiers) il faut
faire : :

    git submodule update --init --recursive
