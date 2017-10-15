Title: Remplacer sa livebox par un UniFi Security Gateway 3P (USG)
Date: 2017-08-26 19:00:56
Modified: 2017-09-02 18:25:10
Author: choiz
Category: text
Tags: UniFi, Gateway, Livebox, USG, Network
Slug: 2017-08-26-remplacer-sa-livebox-par-un-unifi-security-gateway-3p-(usg)
Status: published

Ayant pas mal utilisé le materiel d'ubiquiti j'ai acheté un USG 3 pour la maison.

En recherchant un peu sur le net j'ai vu qu'il était possible de remplacer la
livebox par l'USG tout en concervant la télévision etc… grâce aux VLANs.

Il y a pas mal de manipulations a faire avant de pouvoir remplacer totalement sa
livebox par l'USG.

J'ai utilisé un raspberry pi qui me permet d'installer un controlleur UniFi qui
permet de gerer son matériel de la marque.

En branchant l'USG au secteur il prend l'adresse IP 192.168.1.1 (la même que la
livebox dans un premier temps ça aide pas…). Je branche donc l'USG en direct sur
mon poste et je me connect en ssh dessus avec les login / pass : "ubnt / ubnt".

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

Remplacer le dhclient3, copier la rfc au bon endroit et rendre executable mon
script :
```
sudo bash
mv dhclient3 /sbin/dhclient3
chmod 775 /sbin/dhclient3
chown root:root /sbin/dhclient3
mv rfc3442-classless-routes /etc/dhcp3/dhclient-exit-hooks.d/
chown root:root /etc/dhcp3/dhclient-exit-hooks.d/rfc3442-classless-routes
chmod a+x config_usg.sh
```

Editer le fichier /opt/vyatta/sbin/vyatta-interfaces.pl et ajouter l'option 90
du dhcp. Il faut aller a la ligne 194 :
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

Débrancher votre controlleur du réseau (pour ne pas que l'USG reprovisionne une 
vielle configuration).

Se connecter de nouveau en ssh sur l'usg :
```
ssh ubnt@192.168.1.1
```

Se connecter en tant que root pour executer le script
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

Puis j'éteind l'USG pour remplacer la livebox.

Le port WAN1 pour l'ONT

Le port LAN1 pour votre réseau local

Le port WAN2/LAN2 pour la télévision

Quand j'arrive a joindre l'usg sur l'IP 192.168.1.1 je me reconnect en ssh et je
me connect en root pour sauver la config et l'envoyer sur ma machine.
```
sudo bash
mca-ctrl -t dump-cfg > config.gateway.json
scp config.gateway.json user@ma_machine:/home/user/
```

Maintenant je me déconnecte de l'usg. Je débranche le câble réseau entre l'usg et
mon réseau local pour pouvoir rebrancher mon controlleur. Si on débranche pas
l'usg il va reprendre la config par defaut du controlleur et il faudra tout
refaire (hormis les copies des fichiers dhclient3 rfc… etc…).

Depuis mon poste je copie sur mon controlleur le fichier config.gateway.json que
je viens de sauver.
```
scp config.gateway.json user@mon_controlleur:/home/user
```

Puis je me connecte a mon controlleur en ssh pour déposer dans le bon dossier ce
fichier.

Le dossier doit être `/data/sites/default` si vous utilisez le site par defaut.

Reconnecter l'USG a votre réseau.

Il va être de nouveau provisionné par votre controlleur, si vous avez des
erreurs lors de ce provisionning elles seront affichées dans "alerts" sur votre
controlleur. Dans ce cas il y a un truc qui cloche entre votre config et celle
du controlleur revoir les différentes étapes.

Si le provisionning est ok l'USG redémarre et la config est enfin fini ! ;-)

Grand merci au forum lafibre.info et particulièrement ce [sujet](https://lafibre.info/remplacer-livebox/unifi-security-gateway-en-remplacement-de-la-livebox/).
