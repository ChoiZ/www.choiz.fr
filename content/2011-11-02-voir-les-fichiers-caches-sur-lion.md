Title: Voir les fichiers cachés sur Lion
Date: 2011-11-02 11:17:12
Author: choiz
Category: text
Tags: fichiers, cachés, hidden, files, lion, defaults, AppleShowAllFiles, Finder
Slug: 2011-11-02-voir-les-fichiers-cachés-sur-lion
Status: published

Dans un terminal : :

    defaults write com.apple.Finder AppleShowAllFiles TRUE

    killall Finder

Ouvrir une fenêtre du Finder et vous voyez les fichiers cachés.
