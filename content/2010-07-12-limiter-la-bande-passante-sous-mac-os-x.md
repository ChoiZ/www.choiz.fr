Pour limiter la bande passante sous Mac Os X il suffit de créer un tuyau
virtuel en console.

Ici on créer un tuyau virtuel de 1Mbit/s.

`sudo ipfw pipe 1 config bw 1Mbit/s`

On applique ce tuyau au port 80 (pour le téléchargement de fichier via
un navigateur par exemple).

`sudo ipfw add 1 pipe 1 proto tcp src-port 80`

Pour voir le tuyau :

`sudo ipfw pipe show`

Pour supprimer la règle du port 80 :

`sudo ipfw del 1`

Pour supprimer le tuyau :

`sudo ipfw pipe 1 delete`
