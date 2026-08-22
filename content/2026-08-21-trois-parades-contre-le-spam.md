Title: Trois parades contre le spam : cloisonner, autoriser, défier
Date: 2026-08-21 10:00:00
Author: choiz
Category: text
Tags: mail, antispam, smtp
Slug: 2026-08-21-trois-parades-contre-le-spam
Status: published

Le spam, c'est vieux comme le mail, et malgré les filtres bayésiens, les
listes noires et les scores de réputation, il en passe toujours. Au fil du
temps j'ai empilé plusieurs couches pour reprendre la main sur ma boîte :
contrôler ce que je donne comme adresse, n'autoriser que les bons expéditeurs,
et enfin défier ceux que je ne connais pas. Voici les trois, de la plus simple
à la plus radicale.

J'héberge mes propres mails depuis 2015 (je racontais l'installation dans
[Configurer un serveur mail](https://www.choiz.fr/2015-11-15-configurer-un-serveur-mail.html)),
et depuis 2019 je développe jolimail, ma solution de filtrage de courrier. Les
trois approches que je décris ici, je les utilise au quotidien.

Première parade : une adresse par correspondant
-----------------------------------------------

Pendant longtemps, j'ai créé une adresse différente pour chaque correspondant.
Chaque fois qu'une société ou une personne voulait mon email, je lui fabriquais
une adresse rien que pour elle, de la forme `societe-HASH@mondomaine.fr` — où
`HASH` est une petite suite de caractères aléatoires. Par exemple, pour Darty :
`darty-12ej39@mondomaine.fr`. Cette adresse-là, je ne l'ai donnée qu'à Darty, et
elle redirige vers ma vraie boîte.

L'intérêt est double :

- **La traçabilité.** Si je reçois du spam ou du courrier non sollicité sur
  `darty-12ej39@…`, je sais exactement d'où vient la fuite : soit mon adresse a
  fuité de chez eux (piratage, base mal protégée), soit ils ont tout simplement
  revendu leur base client. L'adresse devient une balise : elle me dit qui a
  laissé filer mon contact. Ça m'est arrivé pour de vrai — avec Free, par
  exemple.
- **Le bouton d'arrêt.** Le jour où une de ces adresses est compromise, je n'ai
  qu'une seule chose à faire : changer le HASH. Pour Free, je suis retourné sur
  leur site et j'ai remplacé `free-123456@mondomaine.fr` par
  `free-987654@mondomaine.fr` — j'ai gardé le préfixe `free`, je n'ai changé que
  les six caractères. L'ancienne redirection n'existe plus : du jour au
  lendemain, plus aucun spam ne peut atterrir, plus de harcèlement possible sur
  cette adresse, rien. Et Free, lui, écrit désormais à la nouvelle.

C'est simple, robuste, et ça met la responsabilité du bon côté.

Et ce n'est pas une bidouille réservée à ceux qui hébergent leur mail : des
services grand public proposent exactement la même chose. Proton offre des
alias par site (via SimpleLogin ou Proton Pass), et iCloud+ d'Apple intègre
« Masquer mon adresse e-mail », qui génère une adresse unique et aléatoire par
service, réexpédiée vers votre vraie boîte et désactivable à tout moment. Le
principe est identique : une adresse par correspondant, qu'on peut couper.

### Une adresse par site, c'est aussi de la sécurité

Cette idée d'adresse unique va bien plus loin que l'anti-spam. Pour vraiment
verrouiller mes comptes, j'applique la même logique de cloisonnement à tout :
une adresse email par site, un mot de passe par site (unique, long, aléatoire),
et la double authentification (2FA) activée partout où c'est possible.

Avec ça, on limite fortement les dégâts. Si un site se fait pirater, la casse
reste contenue à ce seul compte : l'adresse ne sert nulle part ailleurs, le mot
de passe non plus, et si les deux fuitent, la 2FA ajoute une barrière
supplémentaire qui complique sérieusement l'accès — sans être infaillible pour
autant. Pas d'effet domino, là où une seule adresse et un seul mot de passe
réutilisés partout feraient tomber tous vos comptes d'un coup.

Le seul prérequis, c'est de tout garder dans un gestionnaire de mots de passe
(*password manager*) : personne ne peut retenir une adresse et un mot de passe
différents pour chaque site. Le gestionnaire stocke le tout chiffré ; il devient
forcément l'un des points les plus sensibles à protéger — au même titre que
votre compte email, vos mécanismes de récupération et vos appareils, qui restent
eux aussi des maillons critiques.

Reste que ces adresses dédiées cachent un autre atout que je n'ai pas encore
exploité : puisqu'une adresse ne sert qu'à un seul correspondant, je sais à
l'avance qui a le droit de m'y écrire.

Deuxième parade : n'autoriser que les bons expéditeurs
------------------------------------------------------

Reprenons `free-987654@mondomaine.fr`. Cette adresse, je l'ai donnée à Free et
à personne d'autre. Les emails légitimes que j'attends le plus souvent viennent
donc de chez Free — de domaines comme `@free.fr`, `@freetelecom.com` et quelques
autres. Ce qui sort de ce cadre n'est pas forcément illégitime, mais mérite au
moins un coup d'œil.

Je peux donc lier l'adresse à ses expéditeurs autorisés : j'autorise d'avance
les domaines de Free, et leurs mails passent directement.

Mieux : pour ne pas repartir de zéro, j'ai analysé mon INBOX. J'ai retrouvé tous
les mails que Free m'avait envoyés par le passé, j'en ai extrait les adresses
d'expéditeur réelles (`noreply@free.fr`, `service-client@…`, etc.) et je les ai
autorisées d'un coup. Résultat : le jour où j'active le filtrage, les courriers
de Free passent déjà tout seuls — aucune friction pour un correspondant que je
connais déjà.

C'est la bonne façon de démarrer un filtre : on le pré-remplit avec ce qu'on
sait déjà légitime.

### Et si un autre expéditeur écrit quand même ?

Sur une adresse aussi cadrée, un mail qui ne vient pas de Free est louche…
mais pas toujours illégitime. Un exemple concret : je change de Freebox, et
c'est Colissimo qui m'écrit pour la livraison, sur mon adresse `free-987654@…`.
Parfaitement normal — sauf que Colissimo n'était pas dans ma liste.

Dans ce cas, plutôt que de défier l'expéditeur, le filtre me prévient, moi : je
reçois une alerte du genre « un expéditeur inattendu écrit sur ton adresse
Free — légitime ? », et c'est moi qui tranche, oui (et je l'autorise pour la
suite) ou non. C'est le bon niveau de contrôle pour une adresse dédiée : les
livreurs et les services après-vente ponctuels passent quand je le décide, et
au passage, ça filtre une bonne partie des demandes d'avis après achat dont on
est bombardé. ;-)

C'est le point important : chaque adresse a sa propre politique. Pour un alias
dédié comme celui de Free, une liste d'autorisés doublée d'une alerte en cas
d'imprévu suffit amplement — pas besoin de défi-réponse. Ce dernier ne devient
utile que là où l'on ne peut pas tenir de liste fermée : typiquement l'adresse
principale, ouverte à tout le monde.

Troisième parade : le défi-réponse
----------------------------------

Sur cette adresse principale, impossible de tenir une liste fermée : n'importe
qui peut légitimement me découvrir et vouloir m'écrire. C'est là que j'active le
défi-réponse (*challenge-response* en anglais), une méthode un peu radicale et
assez peu connue. L'idée tient en une phrase : si je ne connais pas
l'expéditeur, je mets son message de côté et je lui demande une petite action de
confirmation avant de le lui délivrer.

Ça se place devant votre serveur mail habituel, en modifiant simplement
l'enregistrement MX pour que le courrier entrant passe d'abord par le filtre.

Le principe
-----------

Le filtre tient une liste des expéditeurs qu'il connaît. À l'arrivée d'un
message, il regarde d'abord si l'expéditeur est déjà validé et, s'il ne l'est
pas, il vérifie que le message vient réellement du domaine qu'il prétend avant
de faire quoi que ce soit. Trois cas :

- **Expéditeur connu** (déjà validé) → le message est délivré directement, comme
  si le filtre n'existait pas.
- **Expéditeur inconnu, message suffisamment authentifié** (il vient bien du
  domaine annoncé) → le message est mis en attente (ni jeté, ni délivré) et le
  filtre envoie à l'expéditeur un petit email de vérification. Le lien ouvre une
  page où il doit accomplir une action simple : résoudre une petite opération,
  un captcha ou équivalent.
- **Expéditeur inconnu, message non authentifié** (adresse d'expéditeur
  potentiellement usurpée) → le message est rejeté, sans rien lui envoyer. C'est
  capital : écrire à une adresse peut-être forgée reviendrait à harceler un
  innocent (j'y reviens dans les limites).

Quand l'expéditeur suit le lien et résout l'épreuve, on sait que quelqu'un ayant
accès à cette boîte a bien fait la démarche. Il est alors ajouté à la liste des
connus, son message en attente est délivré, et tous ses futurs emails passeront
sans nouvelle vérification.

Le pari est simple : un humain qui veut vraiment vous joindre fera la démarche
une fois ; un envoi de masse, lui, ne s'en donnera la plupart du temps pas la
peine. Suivre un lien, certains robots savent le faire ; enchaîner en plus une
petite épreuve pour chaque destinataire, c'est déjà nettement moins rentable
pour du spam industriel — sans être, là non plus, une garantie absolue.

Le parcours d'un mail
---------------------

![Parcours d'un mail dans le filtre : connu, authentifié ou rejeté]({static}/images/schema-parcours-mail.svg)

Ce que le filtre garde en mémoire
---------------------------------

La brique centrale, c'est une liste de correspondances (destinataire,
expéditeur) → statut. On peut y ajouter des règles générales pour ne pas défier
tout le monde à l'aveugle :

| Situation                             | Décision              |
|---------------------------------------|-----------------------|
| Expéditeur déjà validé                | délivré directement   |
| Expéditeur bloqué (indésirable)       | rejeté                |
| Domaine de confiance (règle)          | délivré sans défi     |
| Inconnu, message authentifié          | mis en attente + défi |
| Inconnu, non authentifié / usurpé     | rejeté, sans défi     |

Les limites, honnêtement
------------------------

Le défi-réponse a une mauvaise réputation dans le monde de l'email, et il faut
la connaître avant de se lancer. Les critiques sont réelles :

- **Le backscatter.** C'est le reproche numéro un. Les spammeurs usurpent
  fréquemment l'adresse d'expéditeur ; un filtre naïf enverrait alors son défi à
  un innocent dont l'adresse a été usurpée, et produirait du spam en voulant le
  combattre. C'est exactement pour ça que, comme vu plus haut, on ne doit défier
  que les messages suffisamment authentifiés — c'est-à-dire dont on a pu vérifier
  qu'ils proviennent bien du domaine annoncé (SPF, DKIM, idéalement alignés par
  DMARC) — et rejeter les autres sans leur écrire.
- **Le courrier qui ne peut pas répondre.** Confirmations de commande, reçus,
  notifications, newsletters, listes de diffusion… tout ce courrier automatique
  et légitime n'a personne pour cliquer sur un lien. Il faut donc des listes
  blanches solides, sinon on rate des mails importants.
- **L'expéditeur qui ne clique jamais.** Certains correspondants légitimes
  trouveront la démarche pénible, ou ne verront pas l'email de vérification (il
  finit lui-même en spam chez eux, ironie…). Leur premier message est au mieux
  retardé, au pire perdu.
- **Le premier contact est toujours ralenti.** Par construction, un nouvel
  expéditeur ne vous joint pas instantanément.

Alors, pour qui ?
-----------------

Aucune de ces parades n'est universelle, mais elles se complètent. Les adresses
jetables cloisonnent et permettent de révoquer d'un geste tout ce que je
distribue. Les listes d'expéditeurs donnent un contrôle fin sur les adresses
dédiées. Le défi-réponse, lui, protège une adresse ouverte des inconnus — à
condition de gérer sérieusement le backscatter.

Reste qu'il n'a rien d'une solution miracle. Sur une adresse de support, de
commande, ou une boîte qui reçoit beaucoup de courrier automatique, c'est une
mauvaise idée. Il prend tout son sens sur une boîte personnelle très exposée au
spam, où l'on échange surtout avec des humains et où l'on accepte qu'un premier
contact prenne quelques minutes de plus. Là, bien réglé, l'ensemble peut
transformer une boîte inondée en boîte quasi silencieuse.
