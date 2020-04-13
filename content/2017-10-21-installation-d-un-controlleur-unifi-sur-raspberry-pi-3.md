Title: Installation d'un controlleur Unifi sur Raspberry Pi 3
Date: 2017-10-21 21:57:19
Author: choiz
Category: text
Tags: raspberry, unifi, debian, linux
Slug: 2017-10-21-installation-d-un-controlleur-unifi-sur-raspberry-pi-3
Status: published

Pour commencer il faut télécharger la dernière version de raspbian sur le site
officiel raspberrypi.org. Actuellement c'est 2017-09-07-raspbian-stretch-lite.zip.

Il faut ensuite extraire l'image de l'archive :
```
unzip 2017-09-07-raspbian-stretch-lite.zip
```

Puis mettre l'image sur une carte micro sd, j'utilise la commande `dmesg` pour
voir le nom du périphérique USB sur ma machine :
```
[5371729.056039] usb-storage 2-1.3:1.0: USB Mass Storage device detected
[5371729.056115] scsi host5: usb-storage 2-1.3:1.0
[5371730.058300] scsi 5:0:0:0: Direct-Access     Single   Flash Reader     1.00 PQ: 0 ANSI: 0
[5371730.058447] sd 5:0:0:0: Attached scsi generic sg1 type 0
[5371730.509370] sd 5:0:0:0: [sdb] 15759360 512-byte logical blocks: (8.07 GB/7.51 GiB)
[5371730.510383] sd 5:0:0:0: [sdb] Write Protect is off
[5371730.510386] sd 5:0:0:0: [sdb] Mode Sense: 03 00 00 00
[5371730.511384] sd 5:0:0:0: [sdb] No Caching mode page found
[5371730.511386] sd 5:0:0:0: [sdb] Assuming drive cache: write through
[5371730.516135]  sdb: sdb1
[5371730.519381] sd 5:0:0:0: [sdb] Attached SCSI removable disk
```

Je copie donc l'image sur /dev/sdb « ma microsd d'après dmesg.

```
dd bs=4M if=/home/choiz/2017-09-07-raspbian-stretch-lite.img of=/dev/sdb conv=fsync
```

Une fois la copie terminée, je déconnecte la micro sd et je démarre le Raspberry Pi.

```
dd bs=4M if=2017-09-07-raspbian-stretch-lite.img of=/dev/sdb conv=fsync
442+1 enregistrements lus
442+1 enregistrements écrits
1854590976 bytes (1,9 GB, 1,7 GiB) copied, 288,12 s, 6,4 MB/s
```

Une fois le Raspberry Pi démarrer s'identifier avec : pi / raspberry (attention
le clavier est en qwerty pour l'instant donc tapper rqspberry en mot de passe ;-)

Puis tappez la commande `sudo bash` pour passer en root puis `raspi-config` pour
configurer votre Raspberry Pi.

1. Changer les locales (4 Localisation Option, puis I1 Change Locale),
    décocher en_GB.UTF-8 UTF-8 et cocher fr_FR.UTF-8 UTF-8.
    "Default local for the system environment:" choisir fr_FR.UTF-8

2. Changer le timezone (4 Localisation Option, puis I2 Change Timezone),
    choisir Europe, puis Paris.

3. Changer le layout du clavier (4 Localisation Option, puis I3 Change Keyboard
    Layout), choisir Generic 105-key (Intl) PC, Other, French,
    French - French (Azerty), The Default for keybord layout, et pour finir : No compose key.

4. Changer le pays pour le wifi (4 Localisation Option, puis I4 Change Wi-fi
        Country), choisir FR France.

5. Ajouter le SSH (5 Interfacing Options, P2 SSH) Puis répondre "yes" pour
   activer le serveur SSH.

6. Choisir 7 Advanced Options, A1 Expand Filesystem.

7. Choisir 8 Update pour mettre à jour raspbian.

8. 2 Hostname si vous voulez changer le nom de votre raspberry par exemple
"raspberrypi3".

9: Finish, et redémarrer.

Récuperer l'adresse ip du raspberry pi pour se connecter dessus via SSH.

```
ssh pi@adresseip
```

Nous changeons le mot de passe de l'utilisateur 'pi'

pi@raspberry3:~ $ `passwd`

pi@raspberry3:~ $ `sudo bash`

root@raspberrypi3:/home/pi# `apt install dirmngr -y`

root@raspberrypi3:/home/pi# `echo 'deb http://www.ubnt.com/downloads/unifi/debian stable ubiquiti' | tee -a /etc/apt/sources.list.d/ubnt.list > /dev/null`

root@raspberrypi3:/home/pi# `apt-key adv --keyserver keyserver.ubuntu.com --recv C0A52C50`

root@raspberrypi3:/home/pi# `apt update -y`

root@raspberrypi3:/home/pi# `apt install unifi -y`

root@raspberrypi3:/home/pi# `echo 'ENABLE_MONGODB=no' | tee -a /etc/mongodb.conf > /dev/null`

root@raspberrypi3:/home/pi# `apt install oracle-java8-jdk -y`

root@raspberrypi3:/home/pi# `echo 'JAVA_HOME=/usr/lib/jvm/jdk-8-oracle-arm32-vfp-hflt' | tee /etc/default/unifi > /dev/null`

root@raspberrypi3:/home/pi# `reboot`

Une fois le raspberry pi démarrer se rendre sur `https://ip_raspberry:8443` vous
devriez avoir votre interface Unifi disponible.

Mettre à jour votre materiel unifi depuis le controlleur. Puis sur le raspberry
pi nous allons changer d'adresse ip pour avoir un réseau séparé.

```
ssh pi@adresseip
```

pi@raspberry3:~ $ `sudo vi /etc/network/interfaces`

Ajouter à la fin du fichier :

```
auto eth0
iface eth0 inet static
    address 10.0.0.10
    network 255.255.255.0
    gateway 10.0.0.1
```

Enregistrer le fichier et quitter (ne pas rédémarrer le pi pour l'instant).

Retourner sur l'interface d'unifi et modifier l'adresse ip de votre réseau LAN.

Gateway/Subnet 10.0.0.1/24

Cliquer sur "UPDATE DHCP RANGE" puis enregistrer vos modifications dans l'onglet
Devices votre USG devrait être en "provisionning".
Redémarrez le Raspberry Pi avec `sudo reboot` puis vous reconnecter au
controlleur avec la nouvelle adresse ip : `https://10.0.0.10:8443`.
