Title: Ma config : Clevo w650sz i7 4910MQ
Date: 2015-07-18 12:21:00
Author: choiz
Category: text
Tags: clevo, clevo w650, kernel, ethernet, realtek, audio, hdaudio, achat, i7 4910MQ, mSata
Slug: 2015-07-18-ma-config-clevo-w650sz-i7-4910mq
Status: published

Ayant vendu mon Macbook Air 13" il y a quelques mois, j'ai pris le temps
de comparer les différents portables. La marque Taïwanaise "clevo"
propose des machines avec ou sans OS (gain d'une centaine d'euros pour
Windows).

J'ai donc commandé chez [Anyware](http://www.clevo.fr) un w650sz avec un
i7 4910MQ (qui a un score sur
[cpubenchmark](http://www.cpubenchmark.net/cpu.php?cpu=Intel+Core+i7-4910MQ+%40+2.90GHz)
plutôt remarquable).

Je l'ai commandé sans ram, sans disque dur, avec un rack pour disque dur
à la place d'un graveur dvd ou autre cd, sans extension de garanti pour
un peu moins de 1000€ (j'ai bénéficié d'une réduction de 5% et des frais
de port gratuit). J'ai commandé mes barrettes de ram et mon mSata
ailleurs, car les marques en stock ne me plaisaient pas. *Note l'équipe
de Anyware est bien sympa (ils ont enlevé les 2Go de ram qui m'étaient
inutiles donc non facturé)* Plutôt que payer 2Go de ram et ne jamais les
utiliser… J'ai donc ajouté 2 barrettes de 8Go ainsi qu'un mSata de 128Go
pour un peu moins de 200€.

J'ai utilisé cette machine 2 jours, pour l'instant et elle est parfaite
pour mon utilisation. L'écran 1080p sur un 15" est appréciable, avec mon
iiyama 27" j'ai un dualscreen en 2x1080p ce qui est mieux que ma config
précédente avec un écran en 1080p et l'autre avec une résolution
moindre…

Pour la compilation de chrome qui prenait 2/3h à elle seule sur mon
ancien laptop, en 45mn c'était fait avec d'autres grosses applications
tel que gimp ou darktable…

Pour l'instant rien a redire sur cette machine.

Voici les modules a activer dans le noyau pour le réseau et le son : :

    Realtek 8169 gigabit ethernet support
    Build Analog Device HD-audio codec support
