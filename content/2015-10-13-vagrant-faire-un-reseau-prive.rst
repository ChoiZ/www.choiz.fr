Vagrant faire un réseau privé
#############################
:date: 2015-10-13 18:21:02
:author: choiz
:category: text
:tags: vagrant, réseau, privé, private, network
:slug: 2015-10-13-vagrant-faire-un-reseau-prive
:status: published

J'utilise plusieurs machines virtuelles avec vagrant, une avec un backoffice et une avec une API.

J'ai donc du faire un réseau privé dans vagrant pour que le BO communique avec l'API.

Il suffit de modifier la configuration de la vm #1 et d'ajouter :

    config.vm.network "private_network", ip: "192.168.10.1"

Et dans la configuration de la vm #2 d'ajouter :

    config.vm.network "private_network", ip: "192.168.10.2"

Votre vm #1 peut (suite au redémarrage des deux vm vagrant) communiquer avec votre vm #2 directement avec l'ip `192.168.10.2`.
