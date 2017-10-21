Title: Protection de fichier tel qu'un htaccess en PHP
Date: 2011-02-11 15:40:00
Author: choiz
Category: text
Tags: PHP, htaccess, Basic auth, Code
Slug: 2011-02-11-protection-de-fichier-tel-quun-htaccess-en-php
Status: published

Faire un système de protection (tel que htaccess) direct dans un fichier PHP :

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
    ?>

Attention l'utilisation du htaccess n'est pas recommandée sur une connexion non
chiffrée (tel que le HTTP). Utilisez-le plutôt sur une connexion chiffré
(HTTPS).
