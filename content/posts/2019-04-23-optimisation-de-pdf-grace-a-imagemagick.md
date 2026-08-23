---
title: "Optimisation de pdf grâce à ImageMagick"
date: 2019-04-23T00:32:20
slug: "2019-04-23-optimisation-de-pdf-grace-a-imagemagick"
author: choiz
tags: ["imagemagick", "pdf"]
---

Ayant de gros pdf de 3Mo je cherchais une solution pour les optimiser en ligne de commande.

ImageMagick est doté de l'outil convert qui permet de convertir des images.

Avec la commande suivante j'ai pu convertir un PDF de 3,5Mo en un PDF de 1,5Mo en compressant les pages au format JPG 90%.

Au lieu de :

<pre><del>convert -density 300x300 -quality 9 -compress jpeg input.pdf output.pdf</del></pre>

```
convert -density 300x300 -quality 90 -compress jpeg input.pdf output.pdf
```

> ⚠️ `-quality` s'exprime sur 100, pas sur 10 : la commande affichait `-quality 9` (soit 9%, une compression bien trop agressive) alors que le texte annonçait 90%. Corrigé en `-quality 90`.
