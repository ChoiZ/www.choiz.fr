Title: Installation de Proxmox-VE 5 sur Debian Stretch
Date: 2017-08-26 17:36:19
Author: choiz
Category: text
Tags: proxmox, debian, linux
Slug: 2017-08-26-installation-de-proxmox-ve-5-sur-debian-stretch
Status: published

Suite à l'installation de mon NAS, j'ai installer un proxmox dessus.
Par contre il ne faut pas modifier le sources.list ni installer
firmware-linux-nonfree avant d'installer proxmox (celà ne fonctionne pas du
tout).

Sur debian éditer le fichier /etc/hosts comme ceci :
```
127.0.0.1       localhost.localdomain localhost
192.168.15.77   prox4m1.proxmox.com prox4m1 pvelocalhost

# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
```

Puis tester la configuration :
```
hostname --ip-address
192.168.15.77 # should return here your IP adress
```

Puis on ajoute au sources.list le dépot de proxmox, on récupere la clé et on
update :
```
echo "deb http://download.proxmox.com/debian/pve stretch pve-no-subscription" > /etc/apt/sources.list.d/pve-install-repo.list
wget http://download.proxmox.com/debian/proxmox-ve-release-5.x.gpg -O /etc/apt/trusted.gpg.d/proxmox-ve-release-5.x.gpg
apt update && apt dist-upgrade
```

Puis on install les packages Proxmox VE :
```
apt install proxmox-ve postfix open-iscsi
```

On configure postfix en distribution locale uniquement et à la fin de
l'installation on reboot.

Au reboot vous devriez avoir la main en https sur https://ip_proxmox:8006

S'identifier avec vos login / pass debian.

Pour ne pas avoir la popup qui indique que vous n'avez pas de souscription il
faut modifier le fichier /usr/share/pve-manager/js/pvemanagerlib.js et
rechercher la ligne avec :

  ```if (data.status !== 'Active') {```

remplacer par :

  ```if (false /*data.status !== 'Active'*/) {```

Puis relancer pveproxy avec la commande `pveproxy restart`

Se déconnecter de l'interface proxmox, à la reconnection vous n'aurez plus le
message de souscription.

Puis faire les commandes optionnelles :
```
apt remove os-prober
apt remove linux-image-amd64 linux-image-4.9.0-3-amd64
update-grub
```
