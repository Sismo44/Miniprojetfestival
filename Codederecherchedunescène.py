from pagebiblio import *

def artiste_scene(artiste):
    """ Renvoi la scène pour un nom d'artiste, ainsi que ses coordonnées.
    E : nom de l'artiste (str)
    S : (tuple) scène, coordonnées, horaires
    """
    scene_order = list(scenes.keys())
    for horaires, artistes in running_order.items():
        for i in range(len(artistes)):
            if artiste == artistes[i]:
                scene = scene_order[i]
                coords = scenes[scene]
                return (scene, coords, horaires)
                    

    return None
    
        
print(artiste_scene("Ihsahn"))    # Test pour "Benediction", renvoie le tuple ("dave", (0,0))