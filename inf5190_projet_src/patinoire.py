class Patinoire:
    def __init__(self, id, nom, nom_arrondissement,
                 cle_arrondissement, date_maj_arrondissement,
                 ouvert, deblaye, condition):
        self.id = id
        self.nom = nom
        self.nom_arrondissement = nom_arrondissement,
        self.cle_arrondissement = cle_arrondissement
        self.date_maj_arrondissement = date_maj_arrondissement
        self.ouvert = ouvert
        self.deblaye = deblaye
        self.condition = condition
        
    def asDictionary(self):
        return {"id": self.id,
                "nom": self.nom,
                "nom_arrondissement": self.nom_arrondissement,
                "cle_arrondissement": self.cle_arrondissement,
                "date_maj_arrondissement": self.date_maj_arrondissement,
                "ouvert": self.ouvert,
                "deblaye": self.deblaye,
                "condition": self.condition}