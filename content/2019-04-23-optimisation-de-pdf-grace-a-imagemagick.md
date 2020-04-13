Title: Optimisation de pdf grâce à ImageMagick
Date: 2019-04-23 00:32:20
Author: choiz
Category: text
Tags: imagemagick, pdf
Slug: 2019-04-23-optimisation-de-pdf-grace-a-imagemagick
Status: published

Ayant de gros pdf de 3Mo je cherchais une solution pour les optimiser en ligne de commande.

ImageMagick est doté de l'outil convert qui permet de convertir des images.

Avec la commande suivante j'ai pu convertir un PDF de 3,5Mo en un PDF de 1,5Mo en compressant les pages au format JPG 90%.
```
convert -density 300x300 -quality 9 -compress jpeg input.pdf output.pdf
```
