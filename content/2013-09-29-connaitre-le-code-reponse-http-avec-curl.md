Pour connaitre le code réponse HTTP il suffit de faire : :

    curl -IL url

Voici l'exemble avec tumblr.com : :

    curl -IL http://tumblr.com

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
