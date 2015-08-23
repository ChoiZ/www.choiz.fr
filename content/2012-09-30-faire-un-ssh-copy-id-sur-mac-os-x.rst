Faire un ssh-copy-id sur Mac OS X
#################################
:date: 2012-09-30 11:50:54
:author: choiz
:category: text
:tags: ssh-copy-id, mac os x, copy ssh key, copier clé ssh, ssh, copy-id
:slug: 2012-09-30-faire-un-ssh-copy-id-sur-mac-os-x
:status: published

Si vous avez tenté d’utiliser la commande ssh-copy-id sur Mac OS X, vous
avez dû vous rendre compte que, même si openssh est installé nativement,
cette commande n’est pas disponible.

Cette commande n'est pas disponible par defaut sur Mac OS X. Mais on
peut la rendre disponible facilement en quelques étapes.
Créer un fichier "ssh-copy-id" dans le dossier "/usr/bin/" avec ce
contenu :

    | #!/bin/sh
    | # Shell script to install your public key on a remote machine
    | # Takes the remote machine name as an argument.
    | # Obviously, the remote machine must accept password authentication,
    | # or one of the other keys in your ssh-agent, for this to work.
    |
    | ID_FILE="${HOME}/.ssh/id_rsa.pub"
    |
    | if [ "-i" = "$1" ]; then
    |   shift
    |   # check if we have 2 parameters left, if so the first is the new ID file
    |   if [ -n "$2" ]; then
    |     if expr "$1" : ".*\.pub" > /dev/null ; then
    |       ID_FILE="$1"
    |     else
    |       ID_FILE="$1.pub"
    |     fi
    |     shift         # and this should leave $1 as the target name
    |   fi
    | else
    |   if [ x$SSH_AUTH_SOCK != x ] ; then
    |     GET_ID="$GET_ID ssh-add -L"
    |   fi
    | fi
    |
    | if [ -z "`eval $GET_ID`" ] && [ -r "${ID_FILE}" ] ; then
    |   GET_ID="cat ${ID_FILE}"
    | fi
    |
    | if [ -z "`eval $GET_ID`" ]; then
    |   echo "$0: ERROR: No identities found" >&2
    |   exit 1
    | fi
    |
    | if [ "$#" -lt 1 ] || [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
    |   echo "Usage: $0 [-i [identity_file]] [user@]machine" >&2
    |   exit 1
    | fi
    |
    | { eval "$GET_ID" ; } | ssh $1 "umask 077; test -d .ssh || mkdir .ssh ; cat >> .ssh/authorized_keys" || exit 1
    |
    | cat <<EOF
    | Now try logging into the machine, with "ssh '$1'", and check in:
    |
    |   .ssh/authorized_keys
    |
    | to make sure we haven't added extra keys that you weren't expecting.
    |
    | EOF

Il ne reste qu'a donner les droits au fichier :

    $ chmod 755 /usr/bin/ssh-copy-id

Vous pouvez maintenant copier votre clé ssh sur un serveur distant en
tapant :

    ssh-copy-id -i id\_rsa.pub user@machine.distante

