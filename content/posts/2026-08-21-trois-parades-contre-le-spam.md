---
title: "Trois parades contre le spam : cloisonner, autoriser, défier"
date: 2026-08-21T10:00:00
slug: "2026-08-21-trois-parades-contre-le-spam"
author: choiz
tags: ["mail", "antispam", "smtp"]
---

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

L'intérêt est double. D'abord la traçabilité : si je reçois du spam ou du
courrier non sollicité sur `darty-12ej39@…`, je sais exactement d'où vient la
fuite — soit mon adresse a fuité de chez eux (piratage, base mal protégée),
soit ils ont tout simplement revendu leur base client. L'adresse devient une
balise qui me dit qui a laissé filer mon contact ; ça m'est arrivé pour de
vrai, avec Free par exemple. Ensuite le bouton d'arrêt : le jour où une de ces
adresses est compromise, je n'ai qu'une chose à faire, changer le HASH. Pour
Free, je suis retourné sur leur site et j'ai remplacé `free-123456@mondomaine.fr`
par `free-987654@mondomaine.fr` — même préfixe `free`, seuls les six caractères
changent. L'ancienne redirection n'existe plus : du jour au lendemain, plus
aucun spam ne peut atterrir, plus de harcèlement possible, rien. Et Free, lui,
écrit désormais à la nouvelle.

C'est simple, robuste, et ça met la responsabilité du bon côté. Et ce n'est pas
une bidouille réservée à ceux qui hébergent leur mail : des services grand
public proposent exactement la même chose. Proton offre des alias par site (via
SimpleLogin ou Proton Pass), et iCloud+ d'Apple intègre « Masquer mon adresse
e-mail », qui génère une adresse unique et aléatoire par service, réexpédiée
vers votre vraie boîte et désactivable à tout moment.

Cette idée d'adresse unique va d'ailleurs bien plus loin que l'anti-spam. Pour
vraiment verrouiller mes comptes, j'applique la même logique de cloisonnement à
tout : une adresse par site, un mot de passe par site (unique, long, aléatoire),
et la double authentification activée partout où c'est possible. On limite ainsi
fortement les dégâts — si un site se fait pirater, la casse reste contenue à ce
seul compte, et même si l'adresse et le mot de passe fuitent, la 2FA ajoute une
barrière qui complique sérieusement l'accès, sans être infaillible pour autant.
Le seul prérequis, c'est de tout garder dans un gestionnaire de mots de passe :
personne ne peut retenir une adresse et un mot de passe différents pour chaque
site. Il devient forcément l'un des points les plus sensibles à protéger, au
même titre que votre compte email, vos mécanismes de récupération et vos
appareils.

Deuxième parade : n'autoriser que les bons expéditeurs
------------------------------------------------------

Puisqu'une adresse ne sert qu'à un seul correspondant, je sais à l'avance qui a
le droit de m'y écrire. Reprenons `free-987654@mondomaine.fr` : je l'ai donnée à
Free et à personne d'autre. Les emails que j'attends le plus souvent viennent
donc de chez Free — de domaines comme `@free.fr`, `@freetelecom.com` et quelques
autres. Ce qui sort de ce cadre n'est pas forcément illégitime, mais mérite au
moins un coup d'œil.

Je peux donc lier l'adresse à ses expéditeurs autorisés : j'autorise d'avance
les domaines de Free, et leurs mails passent directement. Mieux : pour ne pas
repartir de zéro, j'ai analysé mon INBOX, retrouvé tous les mails que Free
m'avait envoyés par le passé, et extrait leurs adresses réelles
(`noreply@free.fr`, `service-client@…`, etc.) pour les autoriser d'un coup.
Résultat : le jour où j'active le filtrage, les courriers de Free passent déjà
tout seuls, aucune friction pour un correspondant que je connais déjà. C'est la
bonne façon de démarrer un filtre : on le pré-remplit avec ce qu'on sait déjà
légitime.

Reste le cas d'un autre expéditeur qui écrit quand même. Sur une adresse aussi
cadrée, c'est louche, mais pas toujours illégitime : je change de Freebox, et
c'est Colissimo qui m'écrit pour la livraison sur `free-987654@…` —
parfaitement normal, sauf que Colissimo n'était pas dans ma liste. Dans ce cas,
plutôt que de défier l'expéditeur, le filtre me prévient, moi : je reçois une
alerte du genre « un expéditeur inattendu écrit sur ton adresse Free —
légitime ? », et c'est moi qui tranche. Les livreurs et les services
après-vente ponctuels passent quand je le décide, et au passage ça filtre une
bonne partie des demandes d'avis après achat dont on est bombardé. ;-) Chaque
adresse a donc sa propre politique : pour un alias dédié comme celui de Free,
une liste d'autorisés doublée d'une alerte suffit — pas besoin de défi-réponse.
Ce dernier ne devient utile que là où l'on ne peut pas tenir de liste fermée :
l'adresse principale, ouverte à tout le monde.

Troisième parade : le défi-réponse
----------------------------------

Sur cette adresse principale, impossible de tenir une liste fermée : n'importe
qui peut légitimement me découvrir et vouloir m'écrire. C'est là que j'active le
défi-réponse (*challenge-response* en anglais), une méthode un peu radicale et
assez peu connue. L'idée tient en une phrase : si je ne connais pas
l'expéditeur, je mets son message de côté et je lui demande une petite action de
confirmation avant de le lui délivrer. Ça se place devant votre serveur mail
habituel, en modifiant simplement l'enregistrement MX pour que le courrier
entrant passe d'abord par le filtre.

Le filtre tient une liste des expéditeurs qu'il connaît. À l'arrivée d'un
message, il regarde d'abord si l'expéditeur est déjà validé et, s'il ne l'est
pas, il vérifie que le message vient réellement du domaine qu'il prétend avant
de faire quoi que ce soit. Trois cas se présentent alors. Si l'expéditeur est
connu, le message est délivré directement, comme si le filtre n'existait pas.
S'il est inconnu mais que le message est suffisamment authentifié (il vient bien
du domaine annoncé), le message est mis en attente et le filtre lui envoie un
petit email de vérification, dont le lien ouvre une page où accomplir une action
simple : résoudre une petite opération, un captcha ou équivalent. Enfin, si
l'expéditeur est inconnu et le message non authentifié (adresse potentiellement
usurpée), le message est rejeté sans que rien ne lui soit envoyé — c'est
capital, écrire à une adresse peut-être forgée reviendrait à harceler un
innocent, j'y reviens plus bas.

Quand l'expéditeur suit le lien et résout l'épreuve, on sait que quelqu'un ayant
accès à cette boîte a bien fait la démarche. Il est alors ajouté à la liste des
connus, son message en attente est délivré, et tous ses futurs emails passeront
sans nouvelle vérification. Le pari est simple : un humain qui veut vraiment
vous joindre fera la démarche une fois ; un envoi de masse, lui, ne s'en
donnera la plupart du temps pas la peine. Suivre un lien, certains robots savent
le faire ; enchaîner en plus une petite épreuve pour chaque destinataire, c'est
déjà nettement moins rentable pour du spam industriel, sans être là non plus une
garantie absolue.

Voici le parcours d'un mail, selon qu'il est connu, authentifié, ou suspect :

![Parcours d'un mail dans le filtre : connu, authentifié ou rejeté](/images/schema-parcours-mail.svg)

Au cœur du filtre, une liste de correspondances (destinataire, expéditeur) →
statut, qu'on peut compléter par des règles générales pour ne pas défier tout le
monde à l'aveugle :

| Situation                             | Décision              |
|---------------------------------------|-----------------------|
| Expéditeur déjà validé                | délivré directement   |
| Expéditeur bloqué (indésirable)       | rejeté                |
| Domaine de confiance (règle)          | délivré sans défi     |
| Inconnu, message authentifié          | mis en attente + défi |
| Inconnu, non authentifié / usurpé     | rejeté, sans défi     |

Les limites
-----------

Le défi-réponse a une mauvaise réputation dans le monde de l'email, et il faut
la connaître avant de se lancer. Le reproche numéro un, c'est le backscatter :
les spammeurs usurpent fréquemment l'adresse d'expéditeur, et un filtre naïf
enverrait alors son défi à un innocent dont l'adresse a été usurpée — produisant
du spam en voulant le combattre. C'est exactement pour ça qu'on ne doit défier
que les messages suffisamment authentifiés, dont on a pu vérifier qu'ils
proviennent bien du domaine annoncé (SPF, DKIM, idéalement alignés par DMARC),
et rejeter les autres sans leur écrire.

Il y a aussi tout le courrier qui ne peut pas répondre — confirmations de
commande, reçus, notifications, newsletters, listes de diffusion — qui n'a
personne pour cliquer sur un lien : sans listes blanches solides, on rate des
mails importants. Certains correspondants légitimes, eux, ne cliqueront jamais,
par agacement ou parce que l'email de vérification finit lui-même en spam chez
eux ; leur premier message est au mieux retardé, au pire perdu. Et par
construction, ce premier contact est toujours ralenti.

Conclusion
----------

Aucune de ces parades n'est universelle, mais elles se complètent. Les adresses
jetables cloisonnent et permettent de révoquer d'un geste tout ce que je
distribue ; les listes d'expéditeurs donnent un contrôle fin sur les adresses
dédiées ; le défi-réponse protège une adresse ouverte des inconnus, à condition
de gérer sérieusement le backscatter. Reste qu'il n'a rien d'une solution
miracle : sur une adresse de support, de commande, ou une boîte qui reçoit
beaucoup de courrier automatique, c'est une mauvaise idée. Il prend tout son
sens sur une boîte personnelle très exposée au spam, où l'on échange surtout
avec des humains et où l'on accepte qu'un premier contact prenne quelques
minutes de plus. Là, bien réglé, l'ensemble peut transformer une boîte inondée
en boîte quasi silencieuse.
