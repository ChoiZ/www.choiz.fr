---
title: "Versionner son CSS et son JS en précisant de plus en plus"
date: 2026-08-04T09:30:00
slug: "2026-08-04-versionner-son-css-et-son-js-en-precisant-de-plus-en-plus"
author: choiz
tags: ["css", "javascript", "deploy", "cache", "version"]
---

Quand on met à jour le CSS ou le JS d'un site, on tombe toujours sur le même
problème : le navigateur — ou pire, le proxy devant — garde en cache
l'ancienne version du fichier. On déploie, on recharge la page, et rien ne
bouge. Le fameux « vide ton cache » que l'on répète aux clients…

La parade est connue : on ajoute un numéro de version à l'URL du fichier
statique, par exemple `style.css?v=25`. Dès que la version change, l'URL
change, et le navigateur est bien obligé d'aller rechercher le fichier.

Reste une question : que mettre dans ce numéro de version ? J'ai adopté une
règle toute simple. C'est exactement le même principe que celui dont je
parlais dans [Bien nommer ses fichiers](https://www.choiz.fr/2018-12-13-bien-nommer-ses-fichiers.html) —
sauf que cet article-là parlait de nommer les fichiers sur mon disque, pas de
versionner des statiques. Le principe, lui, se transpose tel quel :
**on précise de plus en plus.**

Le principe
-----------

Je pars de l'année sur deux chiffres, et à chaque nouveau déploiement dans la
même « tranche » de temps, j'ajoute juste ce qu'il faut de précision pour que
le numéro soit différent du précédent. Pas plus.

Tant que l'année suffit à distinguer deux déploiements, je m'arrête à l'année.
Si je redéploie le même jour, je descends au mois, puis au jour, puis à
l'heure, aux minutes, aux secondes… uniquement quand c'est nécessaire.

Concrètement, voici la suite de mes déploiements sur une période donnée :

| Déploiement                       | Précision atteinte | Version        |
|-----------------------------------|--------------------|----------------|
| 1er déploiement de l'année (2025) | année              | `25`           |
| 2 janvier 2025                    | mois               | `2501`         |
| 2 janvier 2025 à 12h40            | jour               | `250102`       |
| 2 janvier 2025 à 12h48            | heure              | `25010212`     |
| 2 janvier 2025 à 12h52            | minute             | `2501021252`   |
| 2 janvier 2025 à 12h52:43         | seconde            | `250102125243` |
| 2 janvier 2025 à 12h53            | minute             | `2501021253`   |
| 8 janvier 2025 à 11h28            | jour               | `250108`       |
| 4 juin 2025 à 09h11               | mois               | `2506`         |
| 2 janvier 2026                    | année              | `26`           |

On lit la version comme une date que l'on tronque : `AAMMJJHHMMSS`, mais
seulement jusqu'au niveau de précision utile.

Pourquoi pas toujours la date complète ?
-----------------------------------------

On pourrait se dire qu'il suffit de coller à chaque fois `250102125243` et de
ne plus se poser de question. C'est vrai, ça marche. Mais je trouve deux
avantages à ne préciser que le nécessaire :

- **C'est plus court.** Le premier déploiement de l'année, c'est `25`. Deux
  caractères dans l'URL, c'est propre.

- **C'est lisible.** En regardant la version d'un simple coup d'œil dans le
  code source de la page, je sais tout de suite à quelle « échelle » remonte
  mon dernier déploiement. `26` veut dire « je n'ai pas redéployé depuis le
  début de l'année ». `2501021253` veut dire « ce jour-là, j'ai poussé
  plusieurs fois à la minute près ».

La règle de décision
--------------------

À chaque déploiement, la question est : est-ce que ma version d'aujourd'hui
est différente de la précédente si je m'arrête à l'année ? Au mois ? Au jour ?

Je descends d'un cran de précision tant que la réponse est « non », et je
m'arrête dès qu'elle devient « oui ».

- On est le 8 janvier 2025, mon dernier déploiement date du 2 janvier. Le mois
  (`2501`) ne suffit pas à nous distinguer, mais le jour oui : `250108`.

- On est le 4 juin 2025, dernier déploiement le 8 janvier. Là, le mois suffit
  déjà : `2506`.

- On passe en 2026 : l'année suffit de nouveau à tout distinguer, je repars à
  `26`.

Petit piège à connaître
-----------------------

Cette astuce a une limite qu'il faut avoir en tête : comme je tronque, deux
dates différentes peuvent en théorie produire le même numéro si je ne descends
pas assez bas. Le `2506` du 4 juin et un éventuel `2506` d'un autre jour de
juin auraient la même valeur si je m'arrêtais au mois pour les deux.

En pratique, ça ne pose jamais de problème : la règle est justement de
descendre d'un cran dès qu'il y a collision avec le déploiement *précédent*.
Le numéro de version n'a pas besoin d'être unique dans l'absolu, il a juste
besoin d'être **différent de celui d'avant** pour casser le cache. C'est tout
ce qu'on lui demande.

En résumé
---------

Une seule règle à retenir, et c'est toujours la même que pour nommer ses
fichiers : commencer par le plus grand (l'année), et **préciser de plus en
plus** uniquement quand on en a besoin. On obtient des versions courtes quand
on déploie peu, des versions précises quand on enchaîne les mises en ligne, et
un cache toujours à jour.
