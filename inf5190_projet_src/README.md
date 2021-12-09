# Projet - INF5190

Anna Pasquier PASA27559908

## Lancement de l'application

Modification dans le Makefile pour le lancement de l'application:

flask run --host=0.0.0.0

Dans le fureteur :

http://172.28.128.6:5000/

## Gestion de la base de données

Les fonctions permettant la création et l'accès à la base de données sont dans le dossier 'db', fichier 'database.py'.

Les fonctions permettant la récupération et l'insertion des données dans la base de données sont dans le fichier 'recuperation.py'.
### Piscines

On considère que l'id_uev est unique.

### Glissades

On considère que le nom de l'installation est unique.

### Mofification des données

Dans les fichiers .xml, les noms des arrondissement ne sont pas enregistrés de la même manière que dans le fichier .csv. Par exemple, on trouve des espaces entre les tirets des fichiers .xml pour les noms des arrondissements. On supprime donc ces espaces pour avoir des noms d'arrodissements identiques.

## Services REST

### C1

Ce service ne concerne que les glissades et les patinoires, nous n'avons en effet pas d'informations sur la date de mise à jour des données concercant les piscines.