Title: Remplacer sa livebox par un UniFi Security Gateway 3P (USG)
Date: 2017-08-26 19:00:56
Author: choiz
Category: text
Tags: UniFi, Gateway, Livebox, USG, Network
Slug: 2017-08-26-remplacer-sa-livebox-par-un-unifi-security-gateway-3p-(usg)
Status: published

Ayant pas mal utilisé le materiel d'ubiquiti j'ai acheté un USG 3 pour la maison.

En recherchant un peu sur le net j'ai vu qu'il était possible de remplacer la
livebox par l'USG tout en concervant la télévision etc… grâce a des VLANs.

Il y a pas mal de manipulations a faire avant de pouvoir remplacer totalement sa
livebox par l'USG.

J'ai utilisé un raspberry pi qui me permet d'installer un controlleur UniFi qui
permet de gerer son matériel de la marque.

En branchant l'USG au secteur il prend l'adresse IP 192.168.1.1 (la même que la
livebox dans un premier temps ça aide pas…). Je branche donc l'USG en direct sur
mon poste et je me connect en ssh dessus avec les login / pass : "ubnt / ubnt".

Une fois connecté en ssh il faut reconfigurer l'interface eth1 avec l'adresse IP
de votre choix :
```
# configure
$ set interfaces ethernet eth0 address 192.168.1.10/24
$ delete interfaces ethernet eth0 address 192.168.1.1/24
$ commit
```

On commence par dire qu'on assigne sur eth0 l'IP 192.168.1.10 avec un masque
255.255.255.0 et ensuite on supprime l'IP 192.168.1.1 puis on commit. A ce
moment on se fait déconnecté du SSH vu que l'IP à changée.

Si besoin vous pouvez vous reconnecter avec 192.168.1.10.

L'autre méthode pour changer d'IP est de configurer dans le controlleur UniFi
l'IP de votre réseau en 192.168.1.10/24 ensuite il va reprovisionner l'USG avec
cette IP.

Se rendre sur [le générateur d'option 90 DHCP](https://jsfiddle.net/kgersen/45zudr15/embedded/result/)
Ajouter votre identifiant fti qui permet de se connecter au réseau orange.

Une chaine va être généré par exemple :
```fti/abc1d2e```
génére la chaine :
```00:00:00:00:00:00:00:00:00:00:00:66:74:69:2f:61:62:63:31:64:32:65```

Récupérez l'adresse mac de votre livebox (le modem) elle doit être sous la forme :
```AA:BB:CC:DD:EE:FF```

Télécharger les différents fichiers :

* [dhclient3](https://lafibre.info/remplacer-livebox/en-cours-remplacer-sa-livebox-par-un-routeur-ubiquiti-edgemax/?action=dlattach;attach=34373)
* [rfc3442-classless-routes](https://gist.githubusercontent.com/ChoiZ/32add22a2addcb00c1b07c8a453a5902/raw/c4f3d9426de070121fb70caa9664efbe76c8b2e3/rfc3442-classless-routes)
* [script_orange.sh](https://gist.githubusercontent.com/ChoiZ/32add22a2addcb00c1b07c8a453a5902/raw/c4f3d9426de070121fb70caa9664efbe76c8b2e3/script.orange.sh)
* [config.orange.txt](https://gist.githubusercontent.com/ChoiZ/32add22a2addcb00c1b07c8a453a5902/raw/c4f3d9426de070121fb70caa9664efbe76c8b2e3/config.orange.txt)

Modifier dans script_orange.sh et dans config.orange.txt l'adresse mac + la
chaine fti. Recherchez les chaînes que j'ai cité plus haut en exemple.

Faire un scp de dhclient3 rfc3442-classless-route script_orange.sh et
config.orange.txt sur votre USG avec l'utilisateur qui est indiqué dans votre
controlleur dans settings > site > Device Authentication, cliquez sur
le mot de passe pour le faire apparaitre.
```
scp dhclient3 rfc3442-classless-routes script_orange.sh config.orange.txt user@192.168.1.20:/home/user
```

Se connecter en ssh sur votre usg :
```
ssh user@192.168.1.20
```

Remplacer le dhclient3 :
```
sudo bash
mv dhclient3 /sbin/dhclient3
chmod 775 /sbin/dhclient3
chown root:root /sbin/dhclient3
```

Copier la rfc :
```
mv rfc3442-classless-routes /etc/dhcp3/dhclient-exit-hooks.d/
chown root:root /etc/dhcp3/dhclient-exit-hooks.d/rfc3442-classless-routes
```

Rendre executable le script :
```
chmod a+x script_orange.sh
```

Copier la config dans /config/
```
mv config.orange.txt /config/
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
root@ubnt:/home/user# reboot
Proceed with reboot? [confirm]y
```

Une fois l'usg de nouveau opérationnel, débrancher votre controlleur du réseau
puis se connecter de nouveau en ssh sur l'usg :
```
ssh user@192.168.1.20
```

Reconfigurer l'ip en 192.168.1.1/24 (Débrancher votre livebox du réseau pour pas
avoir de conflit d'ip).
```
configure
set interfaces ethernet eth1 address 192.168.1.1/24
delete interfaces ethernet eth1 address 192.168.1.20/24
commit
```

Maintenant vous êtes déconnecté du ssh vu que votre USG a changé d'ip.

Se reconnecter en ssh sur la nouvelle ip :
```
ssh user@192.168.1.1
```

Se connecter en tant que root pour executer le script
```
sudo bash
./script_orange.sh
exit
```

Puis lancer un configure et charger la conf :
```
configure
load config.orange.txt
```

Vous devriez avoir :
```
Loading configuration from '/config/config.orange.eth0.txt'...
The specified configuration node is not valid
Set ['service' 'gui' 'http-port' '80'] failed
The specified configuration node is not valid
Set ['service' 'gui' 'older-ciphers' 'disable'] failed
The specified configuration node is not valid
Set ['system' 'offload' 'hwnat' 'disable'] failed

Load complete.  Use 'commit' to make changes active.
[edit]
```

Ici je lance un commit pour appliquer la config :
```
commit
```

Et ça m'affiche :
```
[ firewall name LAN_IN ]
Firewall config error: Cannot delete rule set "LAN_IN" (still in use)

[ firewall name LAN_LOCAL ]
Firewall config error: Cannot delete rule set "LAN_LOCAL" (still in use)

[ firewall name LAN_OUT ]
Firewall config error: Cannot delete rule set "LAN_OUT" (still in use)

[ firewall name WAN_IN ]
Error: group [guest_restricted_subnets] doesn't exist

[ firewall name WAN_LOCAL ]
Error: group [guest_restricted_subnets] doesn't exist

[ system conntrack hash-size 4096 ]
Updated conntrack hash size. This change will take affect when the system is rebooted.

[ interfaces ethernet eth0 address dhcp ]
Stopping DHCP client on eth0 ...

[ interfaces ethernet eth0 vif 832 address dhcp ]
Starting DHCP client on eth0.832 ...

[ system syslog ]
Stopping enhanced syslogd: rsyslogd.
Starting enhanced syslogd: rsyslogd.

[ system ntp ]
Stopping NTP server: ntpd.
Starting NTP server: ntpd.

[ service ssh ]
Restarting OpenBSD Secure Shell server: sshd.

[ protocols igmp-proxy ]
Starting IGMP proxy

[ service dhcp-server ]
Stopping DHCP server daemon...
Starting DHCP server daemon...

Commit failed
[edit]
```

Malgrès le fail, je fais un save :
```
root@ubnt# save
Warning: you have uncommitted changes that will not be saved.

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

Le dossier doit être **/data/sites/default** si vous utilisez le site par defaut.

Reconnecter l'USG a votre réseau.

Il va être de nouveau provisionné par votre controlleur, si vous avez des
erreurs lors de ce provisionning elles seront affichées dans "alerts" sur votre
controlleur. Dans ce cas il y a un truc qui cloche entre votre config et celle
du controlleur revoir les différentes étapes.

Si le provisionning est ok l'USG redémarre et la config est enfin fini ! ;-)

Le tout doit être faisable qu'avec un fichier plutôt que d'utiliser
script_orange.sh + config.orange.txt

Grand merci au forum lafibre.info et particulièrement ce [sujet](https://lafibre.info/remplacer-livebox/unifi-security-gateway-en-remplacement-de-la-livebox/).
