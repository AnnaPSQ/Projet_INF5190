## Fonctionnalités à corriger

Les fonctionnalités réalisées sont :
A1, A2, A3, A4, A5, A6, C1, C2, C3, B1 et B2.

### A1

Pour tester A1 vous devez créer une nouvelle base de données dans le répertoire db puis la remplir en lançant l'application.
Pour créer les trois tables de la BDD, utilisez les fichiers 'glissades.sql', 'patinoires.sql' et 'piscines.sql' dans le répertoire db.
Le remplissage de la db se fait au lancement de l'application,  la fonction 'importation_gestion_all' est appelée une première fois dans app_context (l.32 du 'app.py').
L'opération peut prendre un peu de temps mais les étapes de la progression apparaîtront dans l'invite de commande.
Les données sont toutes importées quand le message 'importation des données terminée' apparaît.
De même, le premier chargement de la page d'accueil peut prendre un peu de temps.


Le code relatif à cette fonctionnalité est présent dans 'recuperation.py'. 
Les fonctions sont appelées dans 'app.py'.

### A2

Le background scheduler est lancé à minuit et fonctionne quand l'application est lancée. 
Pour le tester, vous pouvez changer l'heure de lancement. 
Où bien décommenter le code indiqué à la ligne 38 ed 'app.py'.

### A3

Pour voir la documentation REST, rendez-vous à la route "/doc" .

### A4

Pour tester cette fonctionnalité, rendez-vous à la route '/api/installations?arrondissement=LaSalle' .

### A5

Pour tester cette fonctionnalité, rendez-vous à la route '/'.

En bas de page, vous trouverez un champ texte. Remplissez le et lancez la recherche pour trouver le tableau des installations correspondantes à la recherche.
Les données affichées sont les champs communs aux trois types d'installations. C'est donc pour cela que toutes l'information connue n'est pas affichée.

### A6

Pour tester cette fonctionnalité, rendez-vous à la route "/".

En bas de page, vous trouverez un champ sélection. Sélectionnez un nom d'installation pour voir l'information apparaître dans un tableau. Même remarque concernant les colonnes affichées que pour A5.
Pensez à descendre dans la page pour voir les informations associées.

Le service REST associé est disponible à la route : '/api/installation?nom=Bain Quintal' où un autre nom.

### C1

Pour tester C1, rendez-vous à la route '/api/installations/2021'.
Ici, toutes les informations connues sont données.
Le fichier est donc composé de deux types d'installations différents.
En effet, seules les glissades et les patinoires sont concernées.
Nous n'avons pas d'information sur la date de mise à jour des piscines.

### C2

Pour tester C1, rendez-vous à la route '/api/installations/2021/xml'.
Ici, toutes les informations connues sont données.
Le fichier est donc composé de deux types d'installations différents.
Pour voir l'affichage correcte du fichier, enregistrez le contenu de la page dans un format xml (clique droit 'enregistrer sous', nommez le fichier avec .xml)

### C3

Pour tester C1, rendez-vous à la route '/api/installations/2021/csv'.
Un fichier csv sera automatiquement téléchargé sur votre machine.
Ici, les données sont de type Installation.
En effet, un fichier csv ne peut comporter qu'un seul type de données.

### B1

### B2

Apparement j'ai été bannie de twitter et l'application ne m'est vraiment pas familière alors je n'ai pas réussi à implémenter cette fonctionnalité.
