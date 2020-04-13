Title: Passage en SSL du blog
Date: 2016-04-28 22:17:11
Author: choiz
Category: text
Tags: blog, ssl, github
Slug: 2016-04-28-passage-en-ssl-du-blog
Status: published

J'utilise pelican sur github pour écrire mon blog depuis quelques temps, voir les
articles précédents sur le sujet.

J'ai décidé de passer le blog en https, avec un certificat gratuit let's encrypt.

Pour mettre en place un certificat SSL sur "github page" il faut avoir un serveur web qui
fait reverse proxy. J'utilise donc apache avec la configuration suivante :

- Un vhost pour "choiz.fr" qui redirige le port 80 de "choiz.fr" vers le 443 de "www.choiz.fr".
- Un vhost pour "choiz.fr" qui redirige le port 443 (avec un certificat ssl
valide) de "choiz.fr" vers le 443 de
"www.choiz.fr".
- Un vhost pour "www.choiz.fr" qui redirige le port 80 de "www.choiz.fr" vers
le 443 de "www.choiz.fr".
- Et un vhost avec le certificat SSL ainsi que le reverse proxy qui fait croire a
github que je tape directement l'url "http://choiz.github.io".

Ici la configuration du dernier vhost :

```
<IfModule mod_ssl.c>
<VirtualHost *:443>
    ServerName www.choiz.fr

    SSLProxyEngine On
    ProxyRequests Off
    ProxyPreserveHost Off
    ProxyPass / https://choiz.github.io/
    ProxyPassReverse / https://choiz.github.io/
    ProxyPassReverse / http://choiz.github.io/

    # puis la config du SSL
    SSLEngine On
    SSLCertificateFile …
    SSLCertificateKeyFile …
</VirtualHost>
</IfModule>
```
