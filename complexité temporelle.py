#modules
from random import randint
from time import time, perf_counter
from matplotlib import pyplot as plt
from gloutonetexhaustif.py import *

#echelle 
nbre_elements_total = 500
ensemble_listes = [ [randint(1, 1000) for _ in range(n)] for n in range(2, nbre_elements_total)]
for liste in ensemble_listes:
    liste.sort(reverse=True)

# Calculs des durées
def calculs_durees(fonction, scene):
    """ Mesure des durées d'exécution de la fonction
    E:  fonction (object) fonction à exécuter
        scene (list) liste des scenes
    S:  mesures_temps (list)
    """
    mesures_temps = []
    for i in scenes:
        start = perf_counter()
        exhaustif(scene)     # exécution de la focntion
        end = perf_counter()
        mesures_temps.append(end-start)
    return mesures_temps

#creation du repere
duree_exhaustif = calculs_durees(exhaustif(scenes), scenes) 
duree_glouton = calculs_durees(glouton(scenes), scenes)     # ordonnées
nbre_elements = [n for n in range(0, len(scenes))]  # abscisses

# Tracé
plt.plot(nbre_elements_total, duree_exhaustif, "+", color="blue", label="algorithme exhaustif")
plt.plot(nbre_elements_total, duree_glouton, ".", color="red", label="algorithme glouton")
plt.legend()
plt.grid()
plt.show()