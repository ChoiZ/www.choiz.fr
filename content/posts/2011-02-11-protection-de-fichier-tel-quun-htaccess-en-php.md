---
title: "Protection de fichier tel qu'un htaccess en PHP"
date: 2011-02-11T15:40:00
slug: "2011-02-11-protection-de-fichier-tel-quun-htaccess-en-php"
author: choiz
tags: ["php", "code"]
---

Faire un système de protection (tel que htaccess) direct dans un fichier PHP :

```
<?php
if (!empty($_SERVER["PHP_AUTH_USER"]) &&
$_SERVER["PHP_AUTH_USER"] == "login" &&
$_SERVER["PHP_AUTH_PW"] == "password") {
    // code protégé ici
} else {
    header('WWW-Authenticate: Basic realm="Restricted area"');
    header('HTTP/1.0 401 Unauthorized');
    exit('Access Denied');
}
```

Attention l'utilisation du htaccess n'est pas recommandée sur une connexion non
chiffrée (tel que le HTTP). Utilisez-le plutôt sur une connexion chiffrée
(HTTPS).
