J'ai toujours eu pas mal de soucis lors d'impression de différentes
documentations…

J'utilise souvent la balise &lt;pre&gt; pour les lignes de commandes et
il n'y a pas de retour à la ligne fait automatiquement pour cela un
petit css permet de faire les retours à la ligne lorsque la page est
trop grande. :

    pre {
        white-space: pre-wrap;
        word-wrap: break-word;
    }
