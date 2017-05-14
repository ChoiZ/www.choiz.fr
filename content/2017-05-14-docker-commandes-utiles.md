Title: Docker commandes utiles
Date: 2017-05-14 21:47:35
Author: choiz
Category: text
Tags: docker, linux, container
Slug: 2017-05-14-docker-commandes-utiles
Status: published

Voici quelques commandes très utiles si vous utilisez docker.

Supprimer tous les containers qui sont arétés :

```
docker ps -q | xargs docker rm
```

Supprimer toutes les images non utilisées :

```
docker images -q | xargs docker rmi
```

Se connecter a un conteneur docker lancé par son id :

```
docker exec -it id_de_votre_container /bin/bash
```

Se connecter a un conteneur docker lancé par son nom :

```
docker exec -it nom_de_votre_container /bin/bash
```
