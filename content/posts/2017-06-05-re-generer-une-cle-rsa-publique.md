---
title: "Re-générer une clé rsa publique"
date: 2017-06-05T15:03:08
slug: "2017-06-05-re-generer-une-cle-rsa-publique"
author: choiz
tags: ["ssh"]
---

Si vous n'avez plus de clé publique, mais que vous avez toujours votre clé privée vous pouvez regénérer votre clé
publique.

Pour ce faire il faut utiliser la commande *ssh-keygen* avec l'option *-y* et *-f* pour désigner la clé privée.

```ssh-keygen -y -f ~/.ssh/id_rsa > ~/.ssh/id_rsa.pub```

On utilise ci-dessus l'id_rsa (privée) pour générer l'id_rsa.pub.
