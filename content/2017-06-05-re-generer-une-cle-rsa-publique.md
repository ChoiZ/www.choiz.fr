Title: Re-générer une clé rsa publique
Date: 2017-06-05 15:03:08
Author: choiz
Category: text
Tags: ssh, key, rsa, pub
Slug: 2017-06-05-re-generer-une-cle-rsa-publique
Status: published

Si vous n'avez plus de clé publique, mais que vous avez toujours votre clé privée vous pouvez regénérer votre clé
publique.

Pour se faire il faut utiliser la commande *ssh-keygen* avec l'option *-y* et *-f* pour désigner la clé privé.

```ssh-keygen -y -f ~/.ssh/id_rsa > ~/.ssh/id_rsa.pub```

On utilise ci-dessus l'id_rsa (privée) pour générer l'id_rsa.pub.
