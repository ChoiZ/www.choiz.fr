Title: Renommer des fichiers en CLI (ligne de commande)
Date: 2012-04-14 16:02:00
Author: choiz
Category: text
Tags: cli, file, linux
Slug: 2012-04-14-renomer-des-fichiers-en-cli-ligne-de-commande
Status: published

Lorsque je fais mes backups j'essaye d'avoir des noms de fichiers
corrects. Sous linux pour renommer plusieurs fichiers avec bash j'utilise
"rename".

Exemple je veux supprimer tous les espaces d'un fichier :

    rename "s/ *//g" *.*

Ou renommer tous mes fichiers .WAV en .wav etc… :

    rename "s/\.WAV/\.wav/g" *.WAV

À vous de modifier l'expression régulière !
