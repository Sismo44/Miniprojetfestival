from math import sqrt

scenes = {"dave": (0, 0),
          "suppo": (50, 50),
          "massey": (300, 300),
          "bruce": (450, 250)
          }

def distance(scene, A, B):
    x1, y1 = scene[A]
    x2, y2 = scene[B]
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def glouton(scene):
    d_massey = distance(scene, "dave", "massey")
    d_suppo = distance(scene, "dave", "suppo")

    parcours = ["dave"]

    if d_massey < d_suppo:
        parcours = parcours + ["massey", "suppo"]
    else:
        parcours = parcours + ["suppo", "massey"]

    parcours.append("dave")  # retour
    dist = 0
    for i in range(len(parcours) - 1):
        dist = dist + distance(scene, parcours[i], parcours[i+1])

    return parcours, round(dist, 1)

print(glouton(scenes))


def exhaustif(scene):
    # Chemin 1
    chemin1 = ["dave", "massey", "suppo", "dave"]
    d1 = sum(distance(scene, chemin1[i], chemin1[i+1])for i in range(3))

    # Chemin 2
    chemin2 = ["dave", "suppo", "massey", "dave"]
    d2 = sum(distance(scene, chemin2[i], chemin2[i+1]) for i in range(3))

    if d1 < d2:
        return chemin1, round(d1, 1)
    else:
        return chemin2, round(d2, 1)

print(exhaustif(scenes))