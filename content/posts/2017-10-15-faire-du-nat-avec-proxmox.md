---
title: "Faire du NAT avec Proxmox"
date: 2017-10-15T22:08:23
slug: "2017-10-15-faire-un-nat-avec-proxmox"
author: choiz
tags: ["network", "proxmox"]
---

L'idée est d'utiliser qu'une seule adresse ip publique pour plusieurs VM. Comme à
la maison vous avez des adresses ip en 192.168.x.x notre serveur proxmox peut
faire la même chose.

Ip Publique de proxmox : 11.22.33.44
Ip Privée de proxmox : 10.0.0.254

Je me connecte en ssh à Proxmox et je modifie le fichier `/etc/network/interfaces`
j'ajoute à la fin du fichier :

    auto vmbr2
    iface vmbr2 inet static
        address 10.0.0.254
        netmask 255.255.255.0
        bridge_ports none
        bridge_stp off
        bridge_fd 0
        post-up echo 1 > /proc/sys/net/ipv4/ip_forward
        post-up iptables -t nat -A POSTROUTING -s '10.0.0.0/24' -o vmbr0 -j MASQUERADE
        post-down iptables -t nat -D POSTROUTING -s '10.0.0.0/24' -o vmbr0 -j MASQUERADE

On peut également ajouter si on veut différents ports qu'on ouvre vers
l'extérieur vers tel ou tel VM ou conteneur.
Par exemple j'ouvre le port 22 de mon conteneur avec l'ip 10.0.0.1 sur le port
8022 de mon ip public :

        post-up iptables -t nat -A PREROUTING -i vmbr0 -p tcp --dport 8022 -j DNAT --to 10.0.0.1:22
        post-down iptables -t nat -D PREROUTING -i vmbr0 -p tcp --dport 8022 -j DNAT --to 10.0.0.1:22

Ensuite enregistrer le fichier `/etc/network/interfaces` puis relancer les
interfaces réseaux

    service networking restart

Lorsque vous allez faire la configuration réseau d'une VM ou d'un conteneur, il
suffit de renseigner une adresse ip de la plage 10.0.0.0/24

Exemple :

    auto eth0
    iface eth0 inet static
        address 10.0.0.1
        netmask 255.255.255.0
        gateway 10.0.0.254

Puis faites un ping depuis votre conteneur vers l'ip 10.0.0.254, puis vers un
site internet duckduckgo.com par exemple.
