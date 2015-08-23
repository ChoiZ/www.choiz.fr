Créer paire de clé pour se connecter en SSH
###########################################
:date: 2012-01-13 10:05:18
:author: choiz
:category: text
:tags: clé publique, clé privée, connexion ssh, authorized_keys, ssh, .ssh
:slug: 2012-01-13-créer-paire-de-clé-pour-se-connecter-en-ssh
:status: published

On commence par ouvrir un terminal puis on tape :

    $ ssh-keygen -t dsa -b 1024

Enter file in which to save the key (/Users/choiz/.ssh/id\_dsa):

| En général je garde le fichier id\_rsa donc je tape "enter" sinon vous
  pouvez spécifier un autre chemin ainsi qu'un autre fichier.

Enter passphrase (empty for no passphrase):

Ici on tape un mot de passe si on en veut un lors de la connexion aux
différents hosts. En général j'en défini un.

Pour finir on copie la clé sur le serveur soit via scp :

    scp ~/.ssh/id\_dsa.pub user@ip:~/.ssh/authorized\_keys/

ou via ssh-copy-id :

    ssh-copy-id -i ~/.ssh/id\_dsa.pub user@ip

