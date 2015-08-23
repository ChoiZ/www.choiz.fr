Renomer des fichiers en CLI (ligne de commande)
###############################################
:date: 2012-04-14 16:02:00
:author: choiz
:category: text
:tags: CLI, rename, renommer, fichiers, wav, WAV
:slug: 2012-04-14-renomer-des-fichiers-en-cli-ligne-de-commande
:status: published

Lorsque je fais mes backups j'essaye d'avoir des noms de fichiers
correct. Sous linux pour renomer plusieurs fichiers avec bash j'utilise
"rename".

Exemple je veux supprimer tous les espaces d'un fichier :

``rename "s/ *//g" *.*``

Ou renomer tous mes fichiers .WAV en .wav etc...

``rename "s/\.WAV/\.wav/g" *.WAV``

A vous de modifier l'expression régulière !

