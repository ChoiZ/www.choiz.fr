Title: Patch & diff
Date: 2011-05-30 06:00:06
Author: choiz
Category: text
Tags: diff, patch, cli, linux
Slug: 2011-05-30-patch-diff
Status: published

Patch permet de "patcher" un fichier, dossier, projet ! Pratique lorsque
vous distribuez du code et que vous voulez le mettre à jour. Comment
l'utiliser ? Dans un premier temps nous allons faire un différentiel de
notre version actuelle du projet et de la nouvelle version (celle
patchée). :

    diff -u version1.php version2.php > mon_patch

Notre fichier de patch est "mon\_patch" si vous ouvrez celui-ci vous
aurez le différentiel entre les deux fichier. Comment le lire ? Les
lignes avec des + devant sont les nouvelles lignes celles avec des -
sont celles a supprimer. Ce n'est pas plus difficile que ça ! Maintenant
j'applique mon patch sur mon fichier version1.php grâce à la commande
suivante :

    patch -p0 < mon_patch
