class Piscine:
    """
    Classe qui sert à la manipulation des données piscines.
    Les champs des objets piscine sont les mêmes que les
    champs de la table piscines.
    J'ai ajouté l'indication du type d'installation dans
    le dictionnaire associé.
    """
    def __init__(self, id, id_uev, type, nom,
                 nom_arrondissement, adresse, propriete,
                 gestion, point_x, point_y, equipement, long, lat):
        self.id = id
        self.id_uev = id_uev
        self.type = type
        self.nom = nom
        self.nom_arrondissement = nom_arrondissement
        self.adresse = adresse
        self.propriete = propriete
        self.gestion = gestion
        self.point_x = point_x
        self.point_y = point_y
        self.equipement = equipement
        self.long = long
        self.lat = lat

    def asDictionary(self):
        return {"installation": "piscine",
                "id": self.id,
                "id_uev": self.id_uev,
                "type": self.type,
                "nom": self.nom,
                "nom_arrondissement": self.nom_arrondissement,
                "adresse": self.adresse,
                "propriete": self.propriete,
                "gestion": self.gestion,
                "point_x": self.point_x,
                "point_y": self.point_y,
                "equipement": self.equipement,
                "long": self.long,
                "lat": self.lat}
