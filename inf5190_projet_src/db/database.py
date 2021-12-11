import sqlite3
import csv
from piscine import Piscine
from glissade import Glissade
from patinoire import Patinoire
from installation import Installation


class Database:

    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db/database.db',
                                              check_same_thread=False)
        return self.connection

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def get_piscine(self, id_uev):
        cursor = self.get_connection().cursor()
        cursor.execute("SELECT * from piscines "
                       "where id_uev = ?", (id_uev,))
        piscine = cursor.fetchall()
        return piscine

    def insert_piscine(self, row):
        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO piscines(id_uev, type, "
            "nom, nom_arrondissement, adresse, propriete, "
            "gestion, point_x, point_y, equipement, long, lat)"
            " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],
             row[8], row[9], row[10], row[11]))

        connection.commit()

    def update_piscine(self, row):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE piscines "
            "SET id_uev=?, type=?, nom=?, nom_arrondissement=?, "
            "adresse=?, propriete=?, gestion=?, point_x=?, "
            "point_y=?, equipement=?, long=?, lat=? "
            "WHERE id_uev = ?;",
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],
             row[8], row[9], row[10], row[11], row[0]))
        connection.commit()

    def get_glissade(self, nom):
        cursor = self.get_connection().cursor()
        cursor.execute("SELECT * from glissades "
                       "where nom = ?;", (nom,))
        glissade = cursor.fetchall()
        return [Glissade(instal[0], instal[1],
                         instal[2], instal[3],
                         instal[4], instal[5],
                         instal[6], instal[7])
                for instal in glissade]

    def insert_glissade(self, row):
        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO glissades(nom, nom_arrondissement, "
            "cle_arrondissement, date_maj_arrondissement, "
            "ouvert, deblaye, condition)"
            " VALUES (?, ?, ?, ?, ?, ?, ?);",
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

        connection.commit()

    def update_glissade(self, nom, row):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE glissades "
            "SET nom=?, nom_arrondissement=?, cle_arrondissement=?, "
            "date_maj_arrondissement=?, ouvert=?, deblaye=?, condition=?"
            "WHERE nom = ?;",
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6],
             nom))
        connection.commit()

    def get_patinoire(self, nom):
        cursor = self.get_connection().cursor()
        cursor.execute("SELECT * from patinoires "
                       "where nom = ?;", (nom,))
        patinoire = cursor.fetchall()
        return [Patinoire(instal[0], instal[1], instal[2],
                          instal[3], instal[4], instal[5],
                          instal[6], instal[7])
                for instal in patinoire]

    def insert_patinoire(self, row):
        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO patinoires(nom, nom_arrondissement, "
            "date_maj, ouvert, deblaye, arrose, resurface)"
            " VALUES (?, ?, ?, ?, ?, ?, ?);",
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

        connection.commit()

    def update_patinoire(self, nom, row):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE patinoires "
            "SET nom=?, nom_arrondissement=?, "
            "date_maj=?, ouvert=?, deblaye=?, "
            "arrose=?, resurface=? "
            "WHERE nom = ?;",
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6],
             nom))
        connection.commit()

    def get_piscines_by_arrondissement(self, nom_arrondissement):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM piscines "
            "WHERE nom_arrondissement=?;",
            (nom_arrondissement,))
        piscines = cursor.fetchall()
        return [Piscine(instal[0], instal[1], instal[2],
                        instal[3], instal[4], instal[5], instal[6],
                        instal[7], instal[8], instal[9], instal[10],
                        instal[11], instal[12]) for instal in piscines]

    def get_glissades_by_arrondissement(self, nom_arrondissement):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM glissades "
            "WHERE nom_arrondissement=?;",
            (nom_arrondissement,))
        glissades = cursor.fetchall()
        return [Glissade(instal[0], instal[1], instal[2],
                         instal[3], instal[4], instal[5], instal[6],
                         instal[7]) for instal in glissades]

    def get_patinoires_by_arrondissement(self, nom_arrondissement):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM patinoires "
            "WHERE nom_arrondissement=?;",
            (nom_arrondissement,))
        patinoire = cursor.fetchall()
        return [Patinoire(instal[0], instal[1], instal[2],
                          instal[3], instal[4], instal[5], instal[6],
                          instal[7]) for instal in patinoire]

    def get_glissades_updated_in_2021(self):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM glissades "
            "WHERE date_maj_arrondissement LIKE '%2021%' "
            "ORDER BY nom;")
        glissades = cursor.fetchall()
        return [Glissade(instal[0], instal[1], instal[2],
                         instal[3], instal[4], instal[5], instal[6],
                         instal[7]) for instal in glissades]

    def get_patinoires_updated_in_2021(self):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM patinoires "
            "WHERE date_maj LIKE '%2021%' "
            "ORDER BY nom;")
        patinoires = cursor.fetchall()
        return [Patinoire(instal[0], instal[1], instal[2],
                          instal[3], instal[4], instal[5], instal[6],
                          instal[7]) for instal in patinoires]

    def get_installations_updated_in_2021(self):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT id, nom, nom_arrondissement FROM patinoires "
            "WHERE date_maj LIKE '%2021%' "
            "UNION SELECT id, nom, nom_arrondissement FROM glissades "
            "WHERE date_maj_arrondissement LIKE '%2021%' "
            "ORDER BY nom;")
        installations = cursor.fetchall()
        return [Installation(instal[0], instal[1], instal[2])
                for instal in installations]

    def get_all_names(self):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT nom FROM piscines "
            "UNION SELECT nom FROM glissades "
            "UNION SELECT nom FROM patinoires "
            "ORDER BY nom;"
        )
        nom = cursor.fetchall()
        return nom

    def get_installation_by_name(self, nom):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT id, nom, nom_arrondissement FROM piscines "
            "WHERE nom=? "
            "UNION SELECT id, nom, nom_arrondissement FROM glissades "
            "WHERE nom=? "
            "UNION SELECT id, nom, nom_arrondissement FROM patinoires "
            "WHERE nom=? "
            "ORDER BY nom;",
            (nom, nom, nom))
        installation = cursor.fetchall()
        return [Installation(instal[0], instal[1], instal[2])
                for instal in installation]
