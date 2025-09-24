from pagebiblio import scenes, running_order, souhaits

listesouhait = list(souhaits.items())
liste_tuple = []

def artiste_scene(artiste):
    """ Renvoi une liste de tuple contenant une scène pour un nom d'artiste, ainsi que ses coordonnées et son horaire.
    E : nom de l'artiste (str)
    S : une liste de tuple, (tuple) : scène, coordonnées, horaires
    """
    scene_order = list(scenes.keys())    # Création d'une liste qui utilise les clés du dictio scenes situé sur la page biblio
    for horaires, artistes in running_order.items(): # utilisation du dictio running_order situé sur la page biblio
        for i in range(len(artistes)):
            if artiste == artistes[i]:
                scene = scene_order[i]
                coords = scenes[scene]
                (scene, coords, horaires)
        
    return liste_tuple
                    
for cle, val in souhaits.items():
    for groupe in val :
        print(artiste_scene(groupe))

liste_tuple.append(artiste_scene(groupe))
