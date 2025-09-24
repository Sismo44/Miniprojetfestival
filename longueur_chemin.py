def longueur_chemin(p):
    """ Longueur totale d'une liste de scènes parcourue
    """
    total = 0
    for i in range (len(p)-1):
        total = total + distance(scenes,p[i],p[i+1])
    return total
    