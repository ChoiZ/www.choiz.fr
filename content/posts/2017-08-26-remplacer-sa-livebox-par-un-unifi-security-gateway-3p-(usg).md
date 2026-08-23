---
title: "Remplacer sa livebox par un UniFi Security Gateway 3P (USG)"
date: 2017-08-26T19:00:56
slug: "2017-08-26-remplacer-sa-livebox-par-un-unifi-security-gateway-3p-(usg)"
url: "/2017-08-26-remplacer-sa-livebox-par-un-unifi-security-gateway-3p-(usg).html"
author: choiz
tags: ["unifi", "network"]
---

Ayant pas mal utilisé le matériel d'ubiquiti j'ai acheté un USG 3 pour la maison.

En recherchant un peu sur le net j'ai vu qu'il était possible de remplacer la
livebox par l'USG tout en conservant la télévision etc… grâce aux VLANs.

Il y a pas mal de manipulations à faire avant de pouvoir remplacer totalement sa
livebox par l'USG.

J'ai utilisé un raspberry pi qui me permet d'installer un contrôleur UniFi qui
permet de gérer son matériel de la marque.

En branchant l'USG au secteur il prend l'adresse IP 192.168.1.1 (la même que la
livebox dans un premier temps ça aide pas…). Je branche donc l'USG en direct sur
mon poste et je me connecte en ssh dessus avec les login / pass : "ubnt / ubnt".

> ⚠️ À ne pas reproduire : ce tuto garde les identifiants par défaut ubnt/ubnt jusqu'au bout sans jamais dire de les changer. Sur un routeur/pare-feu, des identifiants par défaut valent prise de contrôle immédiate si le SSH est exposé : changez le mot de passe admin UniFi et celui du compte ubnt avant toute remise en production.

Se rendre sur [mon générateur de configuration](https://www.l9.fr/usg-config-generator.php) pour générer un fichier config_usg.sh

Puis télécharger les fichiers :

* [dhclient3](https://lafibre.info/remplacer-livebox/en-cours-remplacer-sa-livebox-par-un-routeur-ubiquiti-edgemax/?action=dlattach;attach=34373)
* [rfc3442-classless-routes](https://gist.githubusercontent.com/ChoiZ/32add22a2addcb00c1b07c8a453a5902/raw/c4f3d9426de070121fb70caa9664efbe76c8b2e3/rfc3442-classless-routes)

Faire un scp de dhclient3 rfc3442-classless-route config_usg.sh sur votre USG
avec l'utilisateur "ubnt" et le mot de passe "ubnt"
```
scp dhclient3 rfc3442-classless-routes config_usg.sh ubnt@192.168.1.1:/home/ubnt
```

Se connecter en ssh sur votre usg :
```
ssh ubnt@192.168.1.1
```

Remplacer le dhclient3, copier la rfc au bon endroit et rendre exécutable mon
script :
```
sudo bash
mv dhclient3 /sbin/dhclient3
chmod 755 /sbin/dhclient3
chown root:root /sbin/dhclient3
mv rfc3442-classless-routes /etc/dhcp3/dhclient-exit-hooks.d/
chown root:root /etc/dhcp3/dhclient-exit-hooks.d/rfc3442-classless-routes
chmod a+x config_usg.sh
```

> ⚠️ À ne pas reproduire : j'avais mis ~~chmod 775~~ sur ce script, ce qui rend un binaire root modifiable par tout le groupe, ce qui peut mener à une exécution root si le groupe est compromis. 755 suffit largement (lecture/exécution pour tous, écriture réservée au propriétaire).

Editer le fichier /opt/vyatta/sbin/vyatta-interfaces.pl et ajouter l'option 90
du dhcp. Il faut aller à la ligne 194 :
```
    $output .= "option rfc3442-classless-static-routes code 121 = array of unsigned integer 8;\n\n";
```
Et ajouter dessous :
```
    $output .= "option rfc3118-auth code 90 = string;\n\n";
```

Maintenant redémarrer l'USG.
```
root@ubnt:/home/ubnt# reboot
Proceed with reboot? [confirm]y
```

Débrancher votre contrôleur du réseau (pour ne pas que l'USG reprovisionne une
vieille configuration).

Se connecter de nouveau en ssh sur l'usg :
```
ssh ubnt@192.168.1.1
```

Se connecter en tant que root pour exécuter le script
```
sudo bash
./config_usg.sh
```

Vous devriez avoir :
```
The specified configuration node already exists
[ service nat rule 6010 outbound-interface eth0.832 ]
NAT configuration warning: interface eth0.832 does not exist on this system

[ service nat rule 6011 outbound-interface eth0.838 ]
NAT configuration warning: interface eth0.838 does not exist on this system

[ interfaces ethernet eth0 vif 838 address dhcp ]
Starting DHCP client on eth0.838 ...

[ interfaces ethernet eth0 vif 832 address dhcp ]
Starting DHCP client on eth0.832 ...

[ service ssh ]
Restarting OpenBSD Secure Shell server: sshd.

[ protocols igmp-proxy ]
Starting IGMP proxy

[ service dhcp-server ]
Stopping DHCP server daemon...
Starting DHCP server daemon...

Saving configuration to '/config/config.boot'...
Done
[edit]
```

Puis j'éteins l'USG pour remplacer la livebox.

Le port WAN1 pour l'ONT

Le port LAN1 pour votre réseau local

Le port WAN2/LAN2 pour la télévision

Quand j'arrive à joindre l'usg sur l'IP 192.168.1.1 je me reconnecte en ssh et je
me connecte en root pour sauver la config et l'envoyer sur ma machine.
```
sudo bash
mca-ctrl -t dump-cfg > config.gateway.json
scp config.gateway.json user@ma_machine:/home/user/
```

Maintenant je me déconnecte de l'usg. Je débranche le câble réseau entre l'usg et
mon réseau local pour pouvoir rebrancher mon contrôleur. Si on débranche pas
l'usg il va reprendre la config par défaut du contrôleur et il faudra tout
refaire (hormis les copies des fichiers dhclient3 rfc… etc…).

Depuis mon poste je copie sur mon contrôleur le fichier config.gateway.json que
je viens de sauver.
```
scp config.gateway.json user@mon_controlleur:/home/user
```

Puis je me connecte à mon contrôleur en ssh pour déposer dans le bon dossier ce
fichier.

Le dossier doit être `/data/sites/default` si vous utilisez le site par défaut.

Reconnecter l'USG à votre réseau.

Il va être de nouveau provisionné par votre contrôleur, si vous avez des
erreurs lors de ce provisionning elles seront affichées dans "alerts" sur votre
contrôleur. Dans ce cas il y a un truc qui cloche entre votre config et celle
du contrôleur revoir les différentes étapes.

Si le provisionning est ok l'USG redémarre et la config est enfin finie ! ;-)

Grand merci au forum lafibre.info et particulièrement ce [sujet](https://lafibre.info/remplacer-livebox/unifi-security-gateway-en-remplacement-de-la-livebox/).

[Ubiquiti Networks USG](http://amzn.to/2xXmsDO) sur Amazon.
