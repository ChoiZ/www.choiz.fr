Faire un système de protection (tel que htaccess) direct dans un fichier
PHP : :

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
