Connaitre le code réponse HTTP avec curl
########################################
:date: 2013-09-29 19:10:00
:author: choiz
:category: text
:tags: curl, http, response, code, 301, 302, 404, 200
:slug: 2013-09-29-connaitre-le-code-réponse-http-avec-curl
:status: published

| 
| Pour connaitre le code réponse HTTP il suffit de faire :

.. raw:: html

   </p>

``curl -IL url``

.. raw:: html

   </p>

Voici l'exemble avec tumblr.com :

.. raw:: html

   </p>

``curl -IL http://tumblr.com``

.. raw:: html

   </p>

::

    HTTP/1.1 301 Moved Permanently
    Content-length: 0
    Location: http://www.tumblr.com/
    Connection: close

    HTTP/1.1 302 Moved Temporarily
    Server: nginx
    Date: Sun, 29 Sep 2013 17:06:40 GMT
    Content-Type: text/html
    Connection: close
    P3P: CP="ALL ADM DEV PSAi COM OUR OTRo STP IND ONL"
    Location: https://www.tumblr.com/

    HTTP/1.1 200 OK
    Server: nginx
    Date: Sun, 29 Sep 2013 17:06:42 GMT
    Content-Type: text/html; charset=utf-8
    Connection: keep-alive
    Vary: Accept-Encoding
    P3P: CP="ALL ADM DEV PSAi COM OUR OTRo STP IND ONL"
    Set-Cookie: tmgioct=52485e21d628b00096885790; expires=Wed, 27-Sep-2023 17:06:41 GMT; path=/; httponly

.. raw:: html

   </p>
