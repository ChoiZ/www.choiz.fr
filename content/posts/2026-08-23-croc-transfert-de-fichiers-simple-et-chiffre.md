---
title: "croc : transférer des fichiers entre deux machines, simplement et chiffré"
date: 2026-08-23T18:30:00
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

Par défaut, croc passe par le relais public de getcroc.com. Il ne voit rien du contenu, mais si vous voulez la maîtrise totale — ou transférer sur un réseau fermé — hébergez le vôtre, c'est une seule commande :

```sh
croc relay
```

et côté client, on lui indique où pointer :

```sh
croc --relay "monrelais.exemple.com:9009" send mon-fichier.zip
```

croc est devenu mon réflexe pour tout transfert ponctuel entre deux machines : simple, rapide, chiffré, multiplateforme, et je peux tout garder chez moi avec mon propre relais. Exactement le genre d'outil que j'aime.
