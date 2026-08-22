---
title: "Migration de Pelican à Hugo"
date: 2026-08-22T10:00:00
slug: "2026-08-22-migration-de-pelican-a-hugo"
author: choiz
tags: ["blog", "hugo", "pelican", "migration"]
---

En 2015 je migrais ce blog de [Tumblr à Pelican](https://www.choiz.fr/2015-08-20-migration-de-tumblr-a-pelican.html). Onze ans après cette migration Tumblr → Pelican, je passe cette fois de Pelican à Hugo. Voici pourquoi et, surtout, comment sans rien casser.

Pourquoi changer
----------------

Pelican m'a bien servi une décennie. Mais avec le temps, chaque publication traînait sa part de friction : un *virtualenv* Python à réveiller, des bricolages de locale pour avoir mes dates en français, du CSS minifié à la main… Rien de bloquant, mais de l'agacement qui s'accumule.

[Hugo](https://gohugo.io) répond exactement à ça :

- un seul binaire, aucune dépendance — fini le venv et les `pip install` qui cassent ;
- des builds quasi instantanés, même sur cent articles ;
- un pipeline d'assets intégré (Sass, empreinte de version…) ;
- des taxonomies (tags) natives.

La contrainte non négociable : garder les URLs
----------------------------------------------

Le vrai risque d'une migration, ce n'est pas le contenu — c'est de changer les URLs. Pour deux raisons : le référencement, et surtout mes commentaires. J'utilise [utterances](https://www.choiz.fr/2020-04-13-utiliser-les-github-issues-pour-avoir-des-commentaires-sur-le-blog.html), qui indexe chaque fil de discussion par l'URL de la page. Si une URL change, les commentaires existants se détachent.

Il fallait donc que Hugo produise exactement les mêmes chemins que Pelican, du type `/2015-11-15-configurer-un-serveur-mail.html`. La recette dans `hugo.toml` :

```toml
uglyURLs = true

[permalinks]
  posts = "/:slug/"
  tags  = "/tag/:slug/"
```

Combiné à un `slug` explicite dans chaque article, on retombe sur le `/slug.html` à la racine. Un seul article m'a résisté : celui dont le slug contenait des parenthèses (`…-3p-(usg)`), que Hugo « nettoyait ». Un `url:` forcé dans son en-tête a réglé le cas :

```yaml
url: "/2017-08-26-remplacer-sa-livebox-par-un-unifi-security-gateway-3p-(usg).html"
```

Résultat : les 103 articles ont gardé leur URL au caractère près, accents compris.

Convertir le contenu
--------------------

Le corps des articles étant déjà en Markdown, il migre tel quel : titres, tableaux, images, blocs de code. Seul l'en-tête (les métadonnées) change de format — les `Title:` / `Date:` de Pelican deviennent du YAML entre `---`. Un petit script Python a fait les 103 d'un coup.

Un piège au passage : un titre contenait un `#` échappé en `\#` par Pelican, ce que le YAML de Hugo refuse. Il a fallu nettoyer ces échappements à la conversion.

Le thème, les tags, le flux
---------------------------

J'ai porté mon thème dans les *layouts* Hugo : la colonne de gauche, la mise en page, la coloration du code. Les pages de tags retombent sur `/tags.html` et `/tag/x.html` comme avant, et le flux Atom reste au même endroit, `/feeds/all.atom.xml`, pour ne pas perdre les abonnés.

Publier
-------

Je n'ai pas changé ma façon de publier : je build en local et je commite la sortie, signée. Juste, la commande d'avant — un `make` qui réveillait Python — est devenue&nbsp;:

```sh
hugo
```

En résumé
---------

Même blog, même allure, mêmes URLs, mêmes commentaires — mais un seul binaire à la place de tout un environnement Python. Le blog change encore de moteur sans que ça se voie de l'extérieur. C'est exactement ce qu'on demande à une migration.
