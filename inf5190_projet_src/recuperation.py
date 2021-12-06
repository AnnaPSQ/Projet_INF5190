"""Dans ce fichier sont écrites les fonctions qui seront 
réutilisées dans app.py pour la récupération des données
"""
    
import requests, csv
from db.database import Database
from flask import Flask, g
import xml.etree.ElementTree as ET

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database

def indices_donnees_piscine(row):
    """
    Entrée : row (list[str]) : ligne du document piscine.csv
    Sortie : liste_indices (list[int]) : nombre de colonnes concernees par le champ i dans la base de données    
    """
    
    liste_indices = [0]*12 #12 colonnes dans la table piscines
    i=0
    curseur = 0
    while i < (len(row)):
        mot = row[i]
        if mot.startswith('"') and not mot.endswith('"'):
            i+= 2
            liste_indices[curseur] = 1
            curseur+=1
        else:
            i+=1
            curseur += 1
    return liste_indices

def arrangement_ligne(liste_indices, row):
    """
    Entrée : row (list[str]) : ligne du document piscine.csv
             liste_indices (list[int]) : représente le nombre de colonnes concernees 
                                        par le champ i dans la base de données
    Sortie : good_row (list[str]) : ligne du document piscine.csv avec l'adresse dans une seule colonne
    """
    
    bonnes_donnees = []
    
    curseur=0
    for i in range(len(liste_indices)):
        if liste_indices[i] == 0:
            bonnes_donnees.append(row[curseur])
            curseur += 1
        else:
            mot1 = row[curseur][1:]
            mot2 = row[curseur+1][:-1]
            adresse = mot1+','+mot2
            bonnes_donnees.append(adresse)
            curseur += 2
    return bonnes_donnees
            
        
def importation_donnees_piscines():
    req = requests.get(
        "https://data.montreal.ca/dataset/4604afb7-a7c4-4626-a3ca-e136158133f2/resource/cbdca706-569e-4b4a-805d-9af73af03b14/download/piscines.csv")
    url_content = req.content
    csv_file = open('piscines.csv', 'wb')
    csv_file.write(url_content)
    csv_file.close()

    
def gestion_donnees_piscines():
    
    with open('piscines.csv', newline='') as csvfile:
        rows = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONE)

        for row in rows:
            
            liste_indices = indices_donnees_piscine(row)
            
            bonnes_donnees = arrangement_ligne(liste_indices, row)
            
            id_uev = bonnes_donnees[0]
            # on passe la première ligne
            if id_uev.startswith('ID'):
                pass
            else:
                resultat = get_db().get_piscine(id_uev)
                #on évite les doublons
                if len(resultat) == 0:
                    get_db().insert_piscine(bonnes_donnees)
                #on met à jour les données existantes
                else:
                    
                    get_db().update_piscine(bonnes_donnees)
    csvfile.close()

def importation_donnees_glissades():
    req = requests.get(
        "http://www2.ville.montreal.qc.ca/services_citoyens/pdf_transfert/L29_GLISSADE.xml")
    url_content = req.content
    csv_file = open('glissades.xml', 'wb')
    csv_file.write(url_content)
    csv_file.close()
    
def del_spaces(string):
    """
    Entrée : string (str) : chaine de caractère, le nom de l'arrondissement
    Sortie : nom_arrondissement (str) : le nom de l'arrondissement sans les espace autour du '-'
    
    Cela permet d'assurer que les noms d'arrondissement soit renseignés identiquement dans les trois tables.
    """
    correct = string
    for i in range(1,len(string)-1):
        if string[i] == '-' and string[i-1] == ' ' and string[i+1] == ' ':
            correct =  string[0:i-2]+string[i]+string[i+2:len(string)]
    return correct
    
def gestion_donnees_glissades():
    tree = ET.parse('glissades.xml')
    root = tree.getroot()
    
    for glissade in root.findall('glissade'):
        nom = glissade.find('nom').text
       
        for arrondissement in glissade.findall('arrondissement'):
            
            nom_arr = arrondissement.find('nom_arr').text
            nom_arr = del_spaces(nom_arr)
            cle = arrondissement.find('cle').text
            date_maj = arrondissement.find('date_maj').text
            
        ouvert = glissade.find('ouvert').text
        deblaye = glissade.find('deblaye').text
        condition = glissade.find('condition').text
        
        donnees = [nom, nom_arr, cle, date_maj, ouvert, deblaye, condition]
        resultat = get_db().get_glissade(nom)
        #on évite les doublons
        if len(resultat) == 0:
            get_db().insert_glissade(donnees)
        #on met à jour les données existantes
        else:
            print('true')
            get_db().update_glissade(nom, donnees)
        
def replace_none_by_zeros(liste):
    """
    Entrée : liste (list[str]) : liste de donnees dédiées à la base de données
    Sortie : liste (list[str]): liste de donnees dédiées à la base de données 
                                où les 'None' ont été remplacés par des 0
    """   
    for i in range(len(liste)):
        if liste[i] == 'None':
            liste[i] = '0'
    return liste   

def del_unwanted(liste):
    """
    Entrée : liste (list[str]) : liste de donnees dédiées à la base de données
    Sortie : liste (list[str]): liste de donnees dédiées à la base de données 
                                où les caractères non vuolus ont été supprimés 
                                (espaces, /n et () en début et fin de chaine)
    """ 
    unwanted = [' ', "\n", 'n', '(', ')']
    for i in range(len(liste)):
        indice_debut = 0
        mot = liste[i]
        while (
            indice_debut <= len(mot) and
            (mot[indice_debut] in unwanted or mot[indice_debut:indice_debut+1] in unwanted)):
            indice_debut += 1
        indice_fin = len(mot)-1
        while (
            indice_fin >= 0 and
            (mot[indice_fin] in unwanted or mot[indice_fin:indice_debut-1] in unwanted)):
            indice_fin -= 1
        liste[i] = liste[i][indice_debut:indice_fin+1]
    return liste

            
        
    
def importation_donnees_patinoires():
    req = requests.get(
        "https://data.montreal.ca/dataset/225ac315-49fe-476f-95bd-a1ce1648a98c/resource/5d1859cc-2060-4def-903f-db24408bacd0/download/l29-patinoire.xml")
    url_content = req.content
    csv_file = open('patinoires.xml', 'wb')
    csv_file.write(url_content)
    csv_file.close()

def gestion_donnees_patinoires():
    tree = ET.parse('patinoires.xml')
    root = tree.getroot()
    
    for arrondissement in root.findall('arrondissement'):
        nom_arr = arrondissement.find('nom_arr').text
        nom_arr = del_spaces(nom_arr)
        
        for patinoire in arrondissement.findall('patinoire'):
            nom_pat = patinoire.find('nom_pat').text
            
            for condition in patinoire.findall('condition'):
                date_heure = condition.find('date_heure').text
                ouvert = condition.find('ouvert').text
                deblaye = condition.find('deblaye').text
                arrose = condition.find('arrose').text
                resurface = condition.find('resurface').text
            donnees = [nom_pat, nom_arr, date_heure, ouvert, deblaye, arrose, resurface]
            
            donnees = del_unwanted(donnees)
            donnees = replace_none_by_zeros(donnees)
            
            resultat = get_db().get_patinoire(donnees[0])
            #on évite les doublons
            if len(resultat) == 0:
                get_db().insert_patinoire(donnees)
            #on met à jour les données existantes
            else:
                get_db().update_patinoire(nom_pat, donnees)

def importation_gestion_all():
    importation_donnees_piscines()
    gestion_donnees_piscines()
    importation_donnees_glissades()
    gestion_donnees_glissades()
    importation_donnees_patinoires()
    gestion_donnees_patinoires()
    