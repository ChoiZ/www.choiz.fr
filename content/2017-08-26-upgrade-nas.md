Title: Upgrade NAS
Date: 2017-08-26 11:04:27
Author: choiz
Category: text
Tags: NAS, HP, Microserver, Debian, Proxmox, Stockage, Data
Slug: 2017-08-26-upgrade-nas
Status: published

J'ai acheté il y a quelques années un HP Microserver Gen7 qui me sert de NAS,
dessus j'avais installé Debian 6 à l'époque puis j'ai mis à jour jusqu'à la version 9.

Mon objectif est l'ajout d'un disque car j'ai 4 emplacements pour le stockage et
je n'utilisais que 3 de ses 4 emplacements.

Pour commencer il me fallait un rack 5"¼ permettant de mettre un disque 3"½ ou
2"½, je l'ai trouvé sur [LDLC](http://www.ldlc.com/fiche/PB00157318.html) c'est
un "ICY BOX IB-129SSK-B".

Ensuite j'ai pris sur
[Amazon](https://www.amazon.fr/gp/product/B01LZY5T8Y/ref=oh_aui_detailpage_o02_s00?ie=UTF8&psc=1)
un disque Seagate ST500LM030 en 2"½ de 500Go.

Et j'avais ce qu'il fallait pour le SATA et l'alimentation.

Ce qui m'a permis de mettre un disque 2"½ au niveau de l'emplacement CDROM du HP
Microserver.

J'ai du tué mon uptime d'un an (depuis mon dernier déménagemet) :

```
    12:31:37 choiz@wayland ~  #❯❯❯ uptime
    12:31:37 up 366 days,  1:08,  1 user,  load average: 0,16, 0,22, 0,24
```

Pour la réinstallation j'ai monté un [serveur PXE sur
debian](https://wiki.debian-fr.xyz/PXE_avec_support_EFI) merci Benjamin pour le
lien et les conseils.

Installationn du TFTP :

```
# apt-install -y tftpd-hpa
```

Si vous avez un pare-feu n'oubliez pas d'ouvrir le port 69 :
```
# iptables -A INPUT -p udp -m udp --dport 69 -j ACCEPT
```

Installer le serveur DHCP :

```
# apt install isc-dhcp-server
```

Mes IP sont dans le réseau 192.168.1.0/24, mon router en 192.168.1.1, je met un
range entre 192.168.1.100 et 192.168.1.150 mon serveur TFTP est en 192.168.1.2.

Voici la conf d'isc-dhcp-server :
```
default-lease-time 600;
max-lease-time 7200;

allow booting;

# in this example, we serve DHCP requests from 192.168.1.(3 to 253)
# and we have a router at 192.168.1.1
subnet 192.168.1.0 netmask 255.255.255.0 {
  range 192.168.1.100 192.168.1.150;
  option broadcast-address 192.168.1.255;
  option routers 192.168.1.1;
  option domain-name-servers 192.168.1.1;
  filename "pxelinux.0";
}

group {
  next-server 192.168.1.2;
  host tftpclient {
    filename "pxelinux.0";
  }
}
```

Redémarrer le DHCP pour que la config soit prise en compte.
```
# systemctl restart isc-dhcp-server
```

Maintenant nous téléchargeons la derniere version de debian pour la mettre sur
notre TFTP :

```
# cd /srv/tftp/
# wget -c http://ftp.fr.debian.org/debian/dists/stretch/main/installer-amd64/current/images/netboot/netboot.tar.gz
# tar -zxf netboot.tar.gz
# rm netboot.tar.gz
# systemctl restart tftpd-hpa
```

Le PXE est maintenant fonctionnel avec l'installation de debian.

Je réinstall donc debian 9.1 proprement.

Pour éviter d'avoir ses messages d'erreurs :
```
W: Possible missing firmware /lib/firmware/tigon/tg3_tso5.bin for module tg3
W: Possible missing firmware /lib/firmware/tigon/tg3_tso.bin for module tg3
W: Possible missing firmware /lib/firmware/tigon/tg3.bin for module tg3
```

J'édit mon fichier /etc/apt/sources.list et j'ajoute les "non-free".

Puis j'install le firmware-linux-nonfree :
```
apt update
apt install firmware-linux-nonfree
```

Il me reste plus qu'a remonter mes disques de backup et de refaire mes partages.
