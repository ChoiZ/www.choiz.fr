---
title: "Reprendre la main sur un Screen pas \"detached\""
date: 2012-04-18T01:39:00
slug: "2012-04-18-reprendre-la-main-sur-un-screen-pas-detached"
author: choiz
tags: ["linux"]
---

Lorsque j'ai voulu "réattacher" mon "Screen" j'ai eu le message suivant :

    There is a screen on:
    1652.pts-8.stream62(06.12.2011 02:29:16)(Attached)

Habituellement je détache mon "Screen" mais cette fois j'ai oublié.

Pour "détacher" / "réattacher" mon "Screen" j'ai dû faire la commande suivante :

    screen -dRR

Je note car c'est toujours bon à savoir :)
