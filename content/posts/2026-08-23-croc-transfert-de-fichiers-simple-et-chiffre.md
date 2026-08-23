---
title: "croc : transférer des fichiers entre deux machines, simplement et chiffré"
date: 2026-08-23T11:39:00
slug: "2026-08-23-croc-transfert-de-fichiers-simple-et-chiffre"
author: choiz
tags: ["cli", "network", "file"]
---

Envoyer un fichier d'un ordinateur à un autre reste étonnamment pénible : la clé USB qu'on n'a jamais sous la main, le mail qui refuse au-delà de 25 Mo, le cloud qui réclame un compte et un long téléversement… [croc](https://getcroc.com) règle ça en deux commandes, chiffré de bout en bout, sans compte ni serveur à monter. On tape `croc send fichier` d'un côté, on récupère un petit code, on tape ce code de l'autre côté, et le transfert démarre — même entre deux machines derrière leurs box, sans ouvrir le moindre port.

Comment ça marche
-----------------

Tout repose sur le code. Quand vous lancez `croc send`, l'outil génère une phrase du genre `8451-magnum-cargo-arctic`. Ce code joue deux rôles à la fois : il identifie le transfert, et il sert de secret partagé. Les deux machines le passent dans un PAKE (*password-authenticated key exchange*), un algorithme qui permet à deux parties de dériver la même clé de chiffrement solide à partir d'un secret faible, sans jamais faire transiter cette clé sur le réseau. Le transfert est ensuite chiffré de bout en bout avec cette clé.

Entre les deux machines se trouve un relais (public par défaut). Mais il ne fait que faire suivre des octets déjà chiffrés : il ne voit ni le contenu du fichier, ni la clé. Son seul rôle est de permettre à deux ordinateurs, chacun derrière son NAT, de se trouver sans redirection de port. Autrement dit, même le relais ne peut rien lire de ce qui passe.

En pratique
-----------

L'installation, selon la plateforme :

```sh
brew install croc                  # macOS
sudo apt install croc              # Debian / Ubuntu
curl https://getcroc.com | bash    # multiplateforme
```

> ⚠️ À ne pas reproduire tel quel : un curl | bash exécute un script sans relecture ni vérification, ce qui est risqué si le serveur ou la connexion est compromis (MITM). Préférez brew/apt ou le binaire signé des releases GitHub, ou à défaut téléchargez le script et relisez-le avant de l'exécuter.

Pour envoyer, on pointe un fichier ou un dossier :

```sh
croc send mon-fichier.zip
```

croc affiche alors le code à transmettre :

```
Code is: 8451-magnum-cargo-arctic
```

Et sur l'autre machine, il suffit de le taper :

```sh
croc 8451-magnum-cargo-arctic
```

Ça marche aussi bien pour un dossier entier que pour plusieurs fichiers d'un coup, et si le transfert est interrompu, on relance la commande : il reprend là où il s'était arrêté. Enfin, on peut choisir son propre code plutôt que de subir celui généré — pratique quand on le dicte au téléphone :

```sh
croc send --code mon-code-a-moi mon-fichier.zip
```

Garder le contrôle : son propre relais
--------------------------------------

Par défaut, croc passe par le relais public de getcroc.com. Il ne voit rien du contenu, mais si vous voulez la maîtrise totale — ou transférer sur un réseau fermé — hébergez le vôtre. Pas besoin d'installer quoi que ce soit de plus : c'est le même binaire croc, avec la sous-commande `relay`. Sur la machine qui servira de relais (un petit VPS, un Raspberry, un poste du réseau) :

```sh
croc relay
```

Il écoute sur cinq ports TCP par défaut, de 9009 à 9013 — pensez à les ouvrir dans le pare-feu de la machine. On peut en choisir d'autres, deux au minimum :

```sh
croc relay --ports 9009,9010
```

Et pour restreindre l'accès, un mot de passe :

```sh
croc relay --pass mon-mot-de-passe
```

Côté clients, le point important : les deux doivent pointer vers ce relais, pas seulement l'expéditeur. À l'envoi, on préfixe la commande par `--relay` :

```sh
croc --relay "monrelais.exemple.com:9009" send mon-fichier.zip
```

Et à la réception, on ajoute le même `--relay` devant le code :

```sh
croc --relay "monrelais.exemple.com:9009" 8451-magnum-cargo-arctic
```

Si le relais a un mot de passe, on ajoute `--pass mon-mot-de-passe` des deux côtés. Et pour ne pas répéter tout ça à chaque fois, la variable d'environnement `CROC_RELAY` (et `CROC_PASS` pour le mot de passe) fait le même travail une fois pour toutes.

Un point à garder en tête : croc a toujours besoin d'un relais pour mettre les deux machines en relation — il n'existe pas de transfert « sans relais » sur Internet. Si vous bloquez `getcroc.com` dans votre pare-feu, croc « classique » cesse donc de fonctionner, et il faut obligatoirement pointer vers votre propre relais, des deux côtés. Seule exception, sur un même réseau local : l'option `--local` démarre un relais local et découvre l'autre machine sur le LAN, sans jamais toucher Internet.

```sh
croc --local send mon-fichier.zip
croc --local 8451-magnum-cargo-arctic
```

Bloquer le relais public devient alors un bon levier pour forcer tout à passer par votre infrastructure : votre relais pour l'Internet, `--local` pour le réseau local.

croc est devenu mon réflexe pour tout transfert ponctuel entre deux machines : simple, rapide, chiffré, multiplateforme, et je peux tout garder chez moi avec mon propre relais. Exactement le genre d'outil que j'aime.
