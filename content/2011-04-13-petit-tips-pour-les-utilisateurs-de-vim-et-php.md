Title: Petit tips pour les utilisateurs de VIM et PHP
Date: 2011-04-13 13:59:00
Author: choiz
Category: text
Tags: php, vim, cli
Slug: 2011-04-13-petit-tips-pour-les-utilisateurs-de-vim-et-php
Status: published

Lorsque je code en PHP, pour tester si il y a des erreurs généralement
dans la console je tape la commande :

    php -l fichier_a_tester.php

Lorsque j'utilise VIM j'utilise la même commande (sans sortir de vim).
Pour la faire il suffit de faire "ESC" pour passer en mode commande de
VIM puis :

    :!php -l %

Ce qui produira exactement le même résultat qu'en console.

:! (permet l'execution d'une commande système dans vim)

Ensuite php -l pour PHP lint

% (récupère le nom du fichier courant avec le path complet)
