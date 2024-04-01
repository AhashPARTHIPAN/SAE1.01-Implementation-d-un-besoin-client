from math import *
from numpy import *
from random import shuffle

##############
# SAE S01.01 #
##############

def nb_villes(villes):
    """renvoie le nombre de ville à visiter contenu dans le tableau ville"""
    return len(villes) // 3

def noms_villes(villes):
    """renvoie le tableau qui contient les noms des villes à visiter"""
    noms = []
    i = 0
    while i < len(villes):
        noms.append(villes[i])
        i += 3
    return noms

def distance(long1, lat1, long2, lat2):
    """calcule et renvoie la distance entre deux villes grace à leurs coordonnées"""
    r = 6370.7
    lat1 *= pi/180
    lat2 *= pi/180
    long1 *= pi/180
    long2 *= pi/180
    res = r * arccos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(long2 - long1))
    return round(res, 2)

def indexCity(ville, villes):
    """renvoie l'indice de la ville ville contenu dans le tableau villes, -1 si la ville n'est pas dans le tableau"""
    if ville in villes:
        return villes.index(ville)
    return -1

def distance_noms(nom1,nom2, villes):
    """calcule et renvoie la distance entre deux villes si les villes sont dans villes, -1 sinon"""
    ind_v1 = indexCity(nom1, villes)
    ind_v2 = indexCity(nom2, villes)
    if ind_v1 == -1 or ind_v2 == -1:
        return -1
    d = distance(villes[ind_v1+1], villes[ind_v1+2], villes[ind_v2+1], villes[ind_v2+2])
    return d

def lecture(path):
    """renvoie un tableau (à partir du fichier path) contenant les données sur les villes à visiter"""
    tab_villes = []
    fichier = open(path, "r")
    ligne = fichier.readline()
    while ligne != "":
        ligne = ligne.strip().split(";")
        tab_villes += ligne
        ligne = fichier.readline()
    fichier.close()
    return tab_villes

def long_tour(villes, tournee):
    """prend en parametre un tableau de villes et l'ordre (tournee) et renvoie la longueur de la tournee"""
    i = 0
    longueur = 0
    while i < len(tournee) - 1:
        longueur += (distance_noms(tournee[i], tournee[i+1], villes))
        i += 1
    longueur += (distance_noms(tournee[-1], tournee[0], villes))
    return longueur
