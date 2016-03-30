Faire un patch de "x" commit(s) avec git
========================================

date  
2014-05-06 11:21:00

author  
choiz

category  
text

tags  
git, patch, commit

slug  
2014-05-06-faire-un-patch-de-x-commits-avec-git

status  
published

Voici mon historique des commits : :

    c0004 -- dernier commit
    c0003 -- avant dernier commit
    c0002 -- second commit
    c0001 -- premier commit

Je veux faire un patch du commit c0001 et c0002 je dois donc faire : :

    git format-patch -2 c0002 --stdout > mon.patch

le "-2" sert à récupérer 2 commits à partir du commit c0002.
