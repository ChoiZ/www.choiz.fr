Title: Icônes / Favicon / Apple-touch-icon
Date: 2013-11-03 14:11:02
Author: choiz
Category: text
Tags: cli, imagemagick
Slug: 2013-11-03-icônes-favicon-apple-touch-icon
Status: published

Voici comment faire facilement sa favicon et ses icônes pour les
appareils mobiles avec image magick.

Mon icône de base est en 512x512px au format png avec prise en charge de
la transparence "icon512.png".

Je veux faire une favicon en 16x16px, 32x32px 48x48px et 64x64px le tout
dans un seul fichier favicon.ico. :

    convert icon512.png \
        -bordercolor white -border 0 \
        \( -clone 0 -resize 16x16 \) \
        \( -clone 0 -resize 32x32 \) \
        \( -clone 0 -resize 48x48 \) \
        \( -clone 0 -resize 64x64 \) \
        -delete 0 -alpha off favicon.ico

Ensuite je veux faire mes icônes pour les appareils mobiles : Android,
Apple etc… :

    convert icon512.png -resize x60 touch-icon-iphone.png
    convert icon512.png -resize x76 touch-icon-ipad.png
    convert icon512.png -resize x120 touch-icon-iphone-retina.png
    convert icon512.png -resize x152 touch-icon-ipad-retina.png

Maintenant il faut ajouter dans notre page html entre les balises head :

    <link rel="shortcut icon" type="image/x-icon" href="favicon.ico">
    <link rel="apple-touch-icon-precomposed" href="touch-icon-iphone.png">
    <link rel="apple-touch-icon-precomposed" sizes="76x76" href="touch-icon-ipad.png">
    <link rel="apple-touch-icon-precomposed" sizes="120x120" href="touch-icon-iphone-retina.png">
    <link rel="apple-touch-icon-precomposed" sizes="152x152" href="touch-icon-ipad-retina.png">

A noter les appareils Android utilisent aussi les images
"apple-touch-icon".
