Title: Update i3-sensible-terminal
Date: 2019-03-24 16:26:25
Author: choiz
Category: text
Tags: linux
Slug: 2019-03-24-update-i3-sensible-terminal
Status: published

En voulant modifier ma config de i3 je me suis aperçu que j'avais modifié la ligne :
```
bindsym $mod+Return exec i3-sensible-terminal
```
par la ligne suivante :
```
bindsym $mod+Return exec urxvt
```

Je préfere ne pas modifier cette ligne à chaque installation de i3wm, donc je réédite ma ligne pour utiliser par défaut `i3-sensible-terminal`.

Pour modifier le terminal executé par la commande `i3-sensible-terminal` il suffit donc de lancer la commande suivante puis de choisir dans mon cas urxvt :
```
update-alternatives --config x-terminal-emulator
```
