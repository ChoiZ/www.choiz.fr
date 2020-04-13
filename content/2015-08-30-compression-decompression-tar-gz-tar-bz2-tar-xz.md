Title: Compression Décompression tar.gz tar.bz2 tar.xz
Date: 2015-08-30 11:47:00
Author: choiz
Category: text
Tags: archive, gzip
Slug: 2015-08-30-compression-decompression-tar-gz-tar-bz2-tar-xz
Status: published

J'ai toujours du mal pour décompresser un fichier de type "tar.bz2" ou
"tar.xz". Je n'ai pas encore trouvé le moyen de me souvenir de la
syntaxe…

tar.gz
------

Pour les fichiers `tar.gz` j'arrive parfaitement à compresser ou
décompresser ce format exemple :

On compresse avec :

    tar -cvzf archive.tar.gz dossier_a_compresser/

On décompresse avec :

    tar -xvzf archive.tar.gz

Il suffit de retenir :

-c comme compression / "x" comme eXtract ou eXtraction. -v pour le mode
verbeux. -z pour le "gzip" d'ou le ".gz". -f pour spécifier le fichier.

tar.bz2
-------

Pour les `tar.bz2` je ne sais JAMAIS qu'il faut remplacer "z" de gizip
par "j" de Bzip… (la lettre "b" étant sans doute utilisé avant que le
bzip n'apparaisse). L'alternative est d'utiliser "--bzip"

On compresse avec :

    tar -cvjf archive.tar.bz2 dossier_a_compresser/

Ou :

    tar --bzip2 -cvf archive.tar.bz2 dossier_a_compresser/

On décompresse avec :

    tar -xvjf archive.tar.bz2

Ou :

    tar --bzip2 -xvf archive.tar.bz2

tar.xz
------

Pour ce qui est de Lzma ou le `tar.xz` c'est un "J" majuscule cette
fois ou d'utiliser "--xz".

On compresse avec :

    tar -cvJf archive.tar.xz dossier_a_compresser/

Ou :

    tar --xz -cvf archive.tar.xz dossier_a_compresser/

On décompresse avec :

    tar -xvJf archive.tar.xz

Ou :

    tar --xz -xvf archive.tar.xz
