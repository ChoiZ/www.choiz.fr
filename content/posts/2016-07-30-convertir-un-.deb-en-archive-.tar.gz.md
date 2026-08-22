---
title: "Convertir un .deb en archive .tar.gz"
date: 2016-07-30T10:28:18
slug: "2016-07-30-convertir-un-.deb-en-archive-.tar.gz"
author: choiz
tags: ["archive", "debian", "gentoo", "gzip", "linux"]
---

En voulant installer le logiciel "slack" sur ma machine gentoo au travail j'ai
trouvé un logiciel plutôt intéressant nommé "deb2targz".

En effet [slack](https://slack.com/downloads) ne dispose que des archives ubuntu
en 32 bits, 64 bits et fedora en 64 bits.

deb2targz permet de convertir un fichier ".deb" en archive ".tar.gz".

Si vous êtes sur gentoo installez le via : `emerge -a app-arch/deb2targz`
