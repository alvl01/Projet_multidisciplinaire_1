def find_good_end(liste, i):
    """
    recoit une liste de nombre et un indice
    Retourne l'indice de fin des commandes a l'interieur de boucle ou de condition en
    tenant compte des imbrication de boucles et de condition
    """
    j = i
    end = 2
    while (end != 0):
        if (liste[j] == 13):  # 13 = end
            end -= 1
        elif (liste[j] == 0 or liste[j] == 1):  # 0 = if and 1 = while
            end += 1
        j += 1
    return j
def find_end_condition(liste, i):
    """
    recoit une liste de nombre et un indice
    Retourne l'indice de fin de la condition
    """
    j = i
    while (liste[j] != 13):  # 13 = end
        j += 1
    return j
