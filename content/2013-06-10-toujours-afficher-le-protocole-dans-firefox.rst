Toujours afficher le protocole dans Firefox
###########################################
:date: 2013-06-10 14:22:00
:author: choiz
:category: text
:tags: firefox, config, http, urlbar, browser
:slug: 2013-06-10-toujours-afficher-le-protocole-dans-firefox
:status: published

Souvent lorsque je copie/colle une url depuis firefox j'ajoute http://
or lors de la copie celui-ci est copié… Je me retrouve donc avec deux
fois http://…

.. raw:: html

   </p>

Pour résoudre ce problème j'affiche toujours le protocole dans Firefox :

.. raw:: html

   </p>

Ecrire dans la barre d'adresse :

.. raw:: html

   </p>

``about:config``

.. raw:: html

   </p>

Rechercher :

.. raw:: html

   </p>

``browser.urlbar.trimURLs``

.. raw:: html

   </p>

Modifier la valeur par :

.. raw:: html

   </p>

``false``

.. raw:: html

   </p>
