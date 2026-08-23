---
title: "Protection de fichier tel qu'un htaccess en PHP"
date: 2011-02-11T15:40:00
slug: "2011-02-11-protection-de-fichier-tel-quun-htaccess-en-php"
author: choiz
tags: ["php", "code"]
---

Faire un système de protection (tel que htaccess) direct dans un fichier PHP :

Au lieu de :

<pre><del>if (!empty($_SERVER["PHP_AUTH_USER"]) &&
$_SERVER["PHP_AUTH_USER"] == "login" &&
$_SERVER["PHP_AUTH_PW"] == "password") {</del></pre>

```
<?php
// Identifiants stockés dans un fichier de config non versionné (hors du repo)
$config = require __DIR__ . '/auth-config.php'; // ['user' => 'login', 'pass_hash' => password_hash('password', PASSWORD_DEFAULT)]

if (!empty($_SERVER["PHP_AUTH_USER"]) &&
hash_equals($config['user'], $_SERVER["PHP_AUTH_USER"]) &&
password_verify($_SERVER["PHP_AUTH_PW"], $config['pass_hash'])) {
    // code protégé ici
} else {
    header('WWW-Authenticate: Basic realm="Restricted area"');
    header('HTTP/1.0 401 Unauthorized');
    exit('Access Denied');
}
```

> ⚠️ À ne pas reproduire : ne jamais coder les identifiants en dur, ils finissent versionnés et exposés dans le repo. Sortez-les dans une config non versionnée et comparez un hash avec hash_equals() / password_verify() ; le == sur un secret est aussi sensible aux attaques par timing.

Attention l'utilisation du htaccess n'est pas recommandée sur une connexion non
chiffrée (tel que le HTTP). Utilisez-le plutôt sur une connexion chiffrée
(HTTPS).

On peut d'ailleurs refuser d'emblée toute connexion non chiffrée, directement en
PHP, en vérifiant qu'on est bien en HTTPS (y compris derrière un reverse proxy) :

```php
$secure = (!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off')
    || (($_SERVER['HTTP_X_FORWARDED_PROTO'] ?? '') === 'https');

if (!$secure) {
    header('Location: https://' . $_SERVER['HTTP_HOST'] . $_SERVER['REQUEST_URI'], true, 301);
    exit;
}
```
