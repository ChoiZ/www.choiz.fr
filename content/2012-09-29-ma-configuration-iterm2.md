Title: Ma configuration iTerm2
Date: 2012-09-29 16:27:52
Author: choiz
Category: text
Tags: iTerm2, config, keypad, numeric, enter, ⌥→, ⌥←, ↩, shortcut, clavier, pavé numérique, configuration iTerm2
Slug: 2012-09-29-ma-configuration-iterm2
Status: published

Depuis quelques jours j'utilise iTerm2 et je trouve ce terminal sous Mac
Os X vraiment au top !

J'ai un clavier Apple Usb avec le pavé numérique il faut donc modifier
les préférences d'iTerm2.

iTerm &gt; Préférences (ou ⌘ ,) puis dans Profiles &gt; Keys et en bas
"Load Preset..." et choisir "xterm with Numeric Keypad". Ce n'est pas
tout malheureusement.

La touche "enter" du pavé numérique ne fonctionne pas il faut donc
cliquer sur "+" et dans Keyboard Shortcut: appuyer sur la touche et "↩"
doit apparaitre. Dans Action: choisir "Send Hex Code" et taper "0xd".

J'ai également ajouter 2 raccourcis bien pratiques :

-   "alt et fleche de gauche" soit "⌥←" avec le code "\[H" permet de
    revenir au debut de la ligne de commande que l'on tape (pratique si
    on oublie un argument).
-   "alt et fleche de droite" soit "⌥→" avec le code "\[F" pour aller à
    la fin de la ligne.

