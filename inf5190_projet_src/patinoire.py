class Patinoire:
    """
    Classe qui sert à la manipulation des données patinoires.
    Les champs des objets patinoire sont les mêmes que les
    champs de la table patinoires.
    J'ai ajouté l'indication du type d'installation dans
    le dictionnaire associé.
    """
    def __init__(self, id, nom, nom_arrondissement,
                 date_maj, ouvert, deblaye,
                 arrose, resurface):
        self.id = id
        self.nom = nom
        self.nom_arrondissement = nom_arrondissement,
        self.date_maj = date_maj
        self.ouvert = ouvert
        self.deblaye = deblaye
        self.arrose = arrose
        self.resurface = resurface

    def asDictionary(self):
        return {"installation": "patinoire",
                "id": self.id,
                "nom": self.nom,
                "nom_arrondissement": self.nom_arrondissement,
                "date_maj": self.date_maj,
                "ouvert": self.ouvert,
                "deblaye": self.deblaye,
                "arrose": self.arrose,
                "resurface": self.resurface}
