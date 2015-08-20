Limiter la bande passante sous Mac Os X
#######################################
:date: 2010-07-12 11:59:00
:author: choiz
:category: text
:tags: Limit Brandwith, Limitation Bande Passante, Mac Os, Mac Os X, Tuyau, Tuyau Virtuel, Limit Brandwidth
:slug: 2010-07-12-limiter-la-bande-passante-sous-mac-os-x
:status: published

Pour limiter la bande passante sous Mac Os X il suffit de créer un tuyau
virtuel en console.

.. raw:: html

   </p>

Ici on créer un tuyau virtuel de 1Mbit/s.

.. raw:: html

   </p>

``sudo ipfw pipe 1 config bw 1Mbit/s``

.. raw:: html

   </p>

On applique ce tuyau au port 80 (pour le téléchargement de fichier via
un navigateur par exemple).

.. raw:: html

   </p>

``sudo ipfw add 1 pipe 1 proto tcp src-port 80``

.. raw:: html

   </p>

Pour voir le tuyau :

.. raw:: html

   </p>

``sudo ipfw pipe show``

.. raw:: html

   </p>

Pour supprimer la règle du port 80 :

.. raw:: html

   </p>

``sudo ipfw del 1``

.. raw:: html

   </p>

Pour supprimer le tuyau :

.. raw:: html

   </p>

``sudo ipfw pipe 1 delete``

.. raw:: html

   </p>

Bien entendu on peut créer plusieurs tuyau et plusieurs règles
différentes avec le même tuyau ;)

.. raw:: html

   </p>
