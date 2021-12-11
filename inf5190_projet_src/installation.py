class Installation:
    """
    Classe qui sert à la manipulation de tous les types d'installations.
    Les champs des objets installation sont les champs communs
    aux trois types d'installations.
    """
    def __init__(self, id, nom, nom_arrondissement):
        self.id = id
        self.nom = nom
        self.nom_arrondissement = nom_arrondissement

    def asDictionary(self):
        return {"id": self.id,
                "nom": self.nom,
                "nom_arrondissement": self.nom_arrondissement}
