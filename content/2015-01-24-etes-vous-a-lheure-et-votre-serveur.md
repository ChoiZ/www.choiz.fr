Title: Êtes-vous à l'heure ? (Et votre serveur ?)
Date: 2015-01-24 16:54:00
Author: choiz
Category: text
Tags: debian, ntp, time, linux
Slug: 2015-01-24-êtes-vous-à-lheure-et-votre-serveur
Status: published

Je suis à l'heure, et mes serveurs le sont également (normalement).

Normalement oui, mais le serveur NTP que j'utilisais ne répond plus… Mes
serveurs ont donc 1mn30 de retard pour l'un, et 40mn de retard pour
l'autre !

J'utilisais ntpdate avec le serveur de l'université de Nice
(ntp.unice.fr).

J'ai donc installé ntp grâce aux paquets debian, et maintenant mes
serveurs sont à l'heure.
