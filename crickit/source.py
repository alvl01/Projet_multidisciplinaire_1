import board
import time
import adafruit_tcs34725
from adafruit_crickit import crickit

def read_program(sensor):
    """
    algorithme permetant de lire la bande
    retourne une liste de 0 et de 1
    """
    print("ok")
    Buffer_ = []
    colors = sc.get_color(sensor)
    print("ok")
    sc.motor12(1)  # lance les moteurs
    while len(Buffer_) % 3 == 2 or not sc.code_exit(Buffer_):
        # tant qu'il n'y a pas de code de sortie c'est a dire 1,1,1,1
        # quel couleur
        print(colors)
        if colors == "red" :  # si c'est rouge
            Buffer_.append(0)  # ajoute 0 a la liste
        elif(colors == "green"):  # si c'est bleu
            Buffer_.append(1)  # ajoute 1 a la liste
        elif(colors == "blue"):  # si c'est bleu
            Buffer_.append(2)  # ajoute 1 a la liste
        while colors == "red" or colors == "blue" or colors == "green":
            # tant qu'on a pas changé de case
            colors = sc.get_color(sensor)  # recupère les couleurs
        # on est plus sur de la couleur
        while colors == "white":
            # quand on arrive sur du blanc
            colors = sc.get_color(sensor)  # recupère les couleurs
        # on est plus sur du blanc
        print(Buffer_)
    print("exit code well play ;)")
    time.sleep(2000)  # faire sortir la bande
    sc.motor12(0)  # arrete les moteurs`
    print("ok")
    return [Buffer_]

def interpret_program(liste: any):
    """
    recoit une matrice de nombre
    detecte si c'est un if un while ou une commande simple
    si c'est un while ou un if, il verifie la condition
    dans le cas du if, si la condition est vérifiée,
    il execute par récursivité l'intérieur
    dans le cas du while, tant que la condition est vérifiée,
    il exectute par récursivité l'intérieur
    """
    skip = 0
    command = sc.format_command(liste)
    for i in range(0, len(command)):
        if not skip:
            if command[i] == 0:
                end_indice = sc.find_good_end(liste, i)
                if (sc.Boolean_find(command, i)):
                    a = sc.find_end_condition(liste, i) - 1
                    b = sc.find_good_end(liste, i) - 2
                    interpret_program(liste[a:b])
                skip = end_indice - i
            elif command[i] == 1:
                end_indice = sc.find_good_end(liste, i)
                while (sc.Boolean_find(command, i)):
                    a = sc.find_end_condition(liste, i) - 1
                    b = sc.find_good_end(liste, i) - 2
                    interpret_program(liste[a:b])
                skip = end_indice - i
            else:
                sc.exec_simple_command(command[i])
        else:
            skip -= 1
def code_exit(liste):
    """
    Retourne un TRUE ou FALSE en fonction de si le code 1 1 1 1 est lu par la machine
    de turing
    """
    i = len(liste) - 1  # longeur de la liste - 1
    if (i >= 3):  # si il y a 4 éléments dans la liste
        if (liste[i] and liste[i - 1] and liste[i - 2] and liste[i - 3]):
            # 1 == TRUE and 0 == FALSE ex: liste[1] = 1 = TRUE
            return 1
    return 0
def format_command(liste: any):
    """
    recoit une liste de nombre
    renvoie une liste de nombre entre 0 et 15 etant donné que une commande
    est constitué de 4 bits
    """
    new_liste = []
    n = 0
    for i in range(0, len(liste) // 4):
        n = liste[i * 4 + 0] + 2 * liste[i * 4 + 1]
        n += 4 * liste[i * 4 + 2] + 8 * liste[i * 4 + 3]
        new_liste.append(n)
    return new_liste

def get_color(sensor):
    color = sensor.color_rgb_bytes
    while (color[0] == 0 and color[1] == 0 and color[2] == 0):
        color = sensor.color_rgb_bytes
    red = color[0] * 10
    green = color[1] * 10
    blue = color[2] * 5
    median = ((red+1) * green * blue)**(1/3)
    valeur = 40
    count = 0
    txt_color=""
    for col in color:
        if col - median > valeur:
            count += 1
    if count > 1:
        txt_color = "white";
    elif red - median > valeur:
        txt_color = "red"
    elif green -median > valeur:
        txt_color = "green"
    elif blue - median > valeur:
        txt_color = "blue"
    else:
        txt_color= "white"
    return txt_color

def motor12(intensity):
    """
    Lance ou arrète les moteurs en fonction de intensity
    """
    crickit.dc_motor_1.throttle = intensity
    crickit.dc_motor_2.throttle = intensity
