Title: Faire du NAT avec Proxmox
Date: 2017-10-15 22:08:23
Author: choiz
Category: text
Tags: NAT, Proxmox, IPV4
Slug: 2017-10-15-faire-un-nat-avec-proxmox
Status: published

L'idée est d'utiliser qu'une seule adresse ip public pour plusieurs VM. Comme à
la maison vous avez des adresses ip en 192.168.x.x notre serveur proxmox peut
faire la même chose.

Ip Public de proxmox : 11.22.33.44
Ip Privé de proxmox : 10.0.0.254

Je me connect en ssh à Proxmox et je modifie le fichier `/etc/network/interfaces`
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
l'exterieur vers tel ou tel VM ou Conteneur.
Par exemple j'ouvre le port 22 de mon Conteneur avec l'ip 10.0.0.1 sur le port
8022 de mon ip public :

        post-up iptables -t nat -A PREROUTING -i vmbr0 -p tcp --dport 8022 -j DNAT --to 10.0.0.1:22
        post-down iptables -t nat -D PREROUTING -i vmbr0 -p tcp --dport 8022 -j DNAT --to 10.0.0.1:22

Ensuite enregistrer le fichier `/etc/network/interfaces` puis relancer les
interfaces réseaux

    service networking restart
