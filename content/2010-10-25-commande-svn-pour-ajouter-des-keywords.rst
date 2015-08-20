Commande SVN pour ajouter des keywords
######################################
:date: 2010-10-25 14:27:33
:author: choiz
:category: text
:tags: SVN, Subversion, Keyword, Id, Revision, Date, Author, URL, PHP, Code, Subversion
:slug: 2010-10-25-commande-svn-pour-ajouter-des-keywords
:status: published

Pour ajouter le numéro de révision ainsi que pas mal d'autres
informations dans vos projets il suffit de taper cette commande :

.. raw:: html

   </p>

    .. raw:: html

       </p>

    svn propset svn:keywords "Id" index.php

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

Ce qui permet d'ajouter le keyword "Id" sur le fichier index.php

.. raw:: html

   </p>

Pour afficher l'Id dans votre fichier index.php ajouter dans celui-ci :

.. raw:: html

   </p>

    .. raw:: html

       </p>

    $Id:$

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

Une fois le fichier comité vous obtiendrez :

.. raw:: html

   </p>

    .. raw:: html

       </p>

    $Id: ajax\_modif.php 481 2010-10-25 12:02:50Z choiz $

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

D'autres keywords sont disponible tel que :

.. raw:: html

   </p>

    .. raw:: html

       </p>

    | $Revision:$
    | $Date:$
    | $Author:$
    | $URL:$

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

Vous pouvez les ajouter les uns a la suite des autres par exemple pour
notre fichier index.php je veux ajouter les 4 keywords précédents grâce
à la commande :

.. raw:: html

   </p>

    .. raw:: html

       </p>

    svn propset svn:keywords "Revision Date Author URL" index.php

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

Ce qui affichera :

.. raw:: html

   </p>

    .. raw:: html

       </p>

    |  $Revision: 481 $
    |  $Date: 2010-10-25 14:02:50 +0200 (lun., 25 oct. 2010) $
    |  $Author: choiz $
    |  $URL: svn://svn.choiz.fr/projet/branches/prod/index.php $

    .. raw:: html

       </p>
       <p>

.. raw:: html

   </p>

N'hésitez pas à ajouter des commentaires si vous avez des questions ;)

.. raw:: html

   </p>
