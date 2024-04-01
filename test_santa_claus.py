from santa_claus import *

def test_nb_villes():
    assert nb_villes(villes) == 10
    assert nb_villes(villes) > 5
    print("test de la fonction ville: ok")

def test_noms_villes():
    assert noms_villes(villes) == ['Paris', 'Lyon', 'Marseille', 'Lille', 'Strasbourg', 'Rennes', 'Clermont-Ferrand', 'Bordeaux', 'Toulouse', 'Grenoble']
    print("test de la fonction nom_villes: ok")

def test_distance():
    assert distance(2.33, 48.86, 5.40, 43.30 ) == 661.86
    print("test de la fonction distance: ok")

def test_indexCity():
    assert indexCity("Paris", villes) == 0
    assert indexCity("Clermont-Ferrand",villes) == 18
    assert indexCity("Villetaneuse",villes) == -1
    print("test de la fonction indexCity: ok")

def test_distance_noms():
    assert distance_noms("Paris", "Marseille", villes) == 661.86
    assert distance_noms("Paris", "Madrid", villes) == -1
    print("test de la fonction distance_noms: ok")

def test_long_tour():
    assert long_tour(villes, tournee) == 4458.66
    print("test de la fonction long_tour : ok")


villes = ["Paris",2.33,48.86, "Lyon",4.85,45.75, 
          "Marseille", 5.40,43.30, "Lille",3.06,50.63, 
          "Strasbourg",7.75,48.57, "Rennes",-1.66,48.11, 
          "Clermont-Ferrand",3.08,45.77, "Bordeaux", -0.57, 44.83]

villes += ["Toulouse", 1.43, 46.60] + ["Grenoble", 5.72, 45.18]

tournee = noms_villes(villes)

test_nb_villes()
test_noms_villes()
test_distance()
test_indexCity() 
test_distance_noms()
test_long_tour()


long_init = long_tour(villes, tournee)
compteur = 0
while compteur < 10000:
    shuffle(tournee)
    nouv_long = long_tour(villes, tournee)
    if nouv_long < long_init:
        long_init = nouv_long
        nouv_long = tournee
    compteur += 1

print(round(long_init, 2))
print(tournee)
