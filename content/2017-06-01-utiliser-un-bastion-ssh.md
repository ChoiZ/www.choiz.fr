Title: Utiliser un Bastion SSH
Date: 2017-06-01 21:29:24
Author: choiz
Category: text
Tags: ssh, linux
Slug: 2017-06-01-utiliser-un-bastion-ssh
Status: published

Pour créer un Bastion SSH il suffit de modifier votre configuration ssh qui se
trouve dans *~/.ssh/config* et d'ajouter les deux lignes suivantes :

```
Host destination.local
    ProxyCommand ssh user@bastion.fr -W %h:%p
```

C'est tout.

Explications : on utilise l'host *bastion.fr* pour se connecter à
*destination.local*. Quand je tape sur ma machine local *ssh
choiz@destination.local* mon client SSH lit le fichier de configuration, se
connecte à l'host *bastion.fr* avec l'utilisateur *user* puis fait une nouvelle
connexion vers ma destination.

Vous pouvez modifier votre configuration ssh pour se connecter à votre bastion
avec une clé spécifique puis a votre destination avec une autre clé par exemple
ou avec des utilisateurs différents…

Exemple :

```
Host bastion.fr
    User toto
    IdentifyFile ~/.ssh/bastion

Host destination.local
    User tata
    IdentifyFile ~/.ssh/destination
```

Enjoy vincent.m ;-)
