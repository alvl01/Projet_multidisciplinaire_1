import time
import source as sc
from command import Command

BUFFERSIZE = 7
Buffer_ = []

def error_music():
    ###
    # execute une serie du signaux alarmant permetant a l'utilisateur de comprendre qu'il a fait une erreur
    ###
    pass

command_name = ["if", "while", "sortir brosse à dent", "ejecter dentifrisse", "lumimière", "négation", "pouce", "timer", "musique", "appuyé sur bouton","detecte brosse a dent", "True", "end", "and", "or"]

def Boolean_find(cmd, sensor):
    ###
    # recoit une liste de nombre et un indice
    # Retourne TRUE ou FALSE
    ###
    neg = 0
    and_ = 0
    or_ = 0
    boolean = 0
    count = 0
    liste = []
    command = read_program(sensor)
    count += 1
    while command != 26:
        if command == 15:
            and_ = 1
        elif command == 16:
            or_ = 1
        elif command == 5:
             neg = 1
        elif((command == 2 and cmd._brosse_in == 0) or (command == 3 and cmd._eject_dentifrisse) or (command == 4 and cmd._lumiere) or (command == 6 and cmd._pouce) or (command == 7 and cmd._timer) or (command == 8 and cmd._music)or (command == 9 and cmd._buton_onclick) or (command == 10 and cmd._brosse_detected) or command == 11):
             boolean = 1
             liste.append((neg + boolean) % 2)
             neg = 0
        else:
            liste.append((neg + boolean) % 2)
            neg = 0
        command = read_program(sensor)
        count += 1
    return_value = 0
    if and_:
        return_value = 1
    elif or_:
        return_value = 0
    for el in liste:
        if return_value and or_:
            break
        elif (not return_value) and and_:
            break
        elif and_:
            return_value *= el
        elif or_:
            return_value += el
        else:
            return_value = el
    return return_value, count
def get_cmd(sensor):
    cmd = []
    colors = sc.get_color(sensor)
    while len(cmd) < 3:
        # tant qu'il n'y a pas de code de sortie c'est a dire 1,1,1,1
        # quel couleur
        while colors == "white":
            # quand on arrive sur du blanc
            colors = sc.get_color(sensor)  # recupère les couleurs
        # on est plus sur du blanc
        if colors == "red":
            cmd.append(0)
        elif colors == "green":  # si c'est rouge
            cmd.append(1)  # ajoute 0 a la liste
        elif colors == "blue":  # si c'est bleu
            cmd.append(2)  # ajoute 1 a la liste
        while colors == "red" or colors == "blue" or colors == "green":  # tant qu'on a pas changé de case
            colors = sc.get_color(sensor)  # recupère les couleurs
        # on est plus sur de la couleur
    return cmd
def read_program(sensor, sens=1):
    """
    algorithme permetant de lire la bande
    retourne une liste de 0 et de 1
    """
    global BUFFERSIZE, Buffer_
    sc.motor12(1*sens)
    if (sens == -1):
        Buffer_ = []
        get_cmd(sensor)
        return 0
    if len(Buffer_) > 0:
        return_value = sc.format_command(Buffer_[0])
        Buffer_ = Buffer_[1:len(Buffer_)]
        return return_value
    Buffer_ = [[3,0,0]]
    while ((not sc.code_exit(Buffer_[len(Buffer_)-1])) and len(Buffer_) < BUFFERSIZE):
        if Buffer_[0][0] == 3:
            Buffer_ = []
        cmd = get_cmd(sensor)
        Buffer_.append(cmd)
    return_value = sc.format_command(Buffer_[0])
    Buffer_ = Buffer_[1:len(Buffer_)]
    sc.motor12(0)  # arrete les moteurs
    return return_value

def back(sensor, count):
    while count > 2:
         count -= 1
         Buffer_ = read_program(sensor, -1)
    del Buffer_

def skip(sensor):
    command = read_program(sensor)
    count = 1
    count_end = 1
    while count_end > 0:
        count += 1
        if command == 26:
            count_end -= 1
        elif command == 0 or command == 1:
            count_end += 2
        command = read_program(sensor)
    command = read_program(sensor, -1)
    return count - 1
def buffer_again():
    global Buffer_
    Buffer_ = []
def interpret_program(cmd, sensor):
    """
    recoit une liste de nombre
    detecte si c'est un if un while ou une commande simple
    si c'est un while ou un if, il verifie la condition
    dans le cas du if, si la condition est vérifiée,
    il execute par récursivité l'intérieur
    dans le cas du while, tant que la condition est vérifiée,
    il exectute par récursivité l'intérieur
    """
    print("open")
    command = read_program(sensor)
    count = 1
    while_count = 0
    while command != 26:
         if command == 0:
            verif, count_bool = Boolean_find(cmd, sensor)
            if (verif):
                count += interpret_program(cmd, sensor)
            else:
               count += skip(sensor)
         elif command == 1:
            verif, count_bool = Boolean_find(cmd, sensor)
            count += count_bool
            while (verif):
                while_count = interpret_program(cmd, sensor)
                back(sensor, while_count + count_bool)
                verif, count_bool = Boolean_find(cmd, sensor)
            count += skip(sensor)
         else:
            count += 1
            sc.exec_simple_command(cmd, command)
         count += 1
         command = read_program(sensor)
    print("close")
    return count
