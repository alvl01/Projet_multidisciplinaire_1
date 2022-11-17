import time
import source as sc
from command import Command

indice = 7
Buffer_ = []
BUFFERSIZE = 7

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
    command = read_program(sensor, cmd)
    count += 1
    while command != 26:
        if command == 15:
            and_ = 1
        elif command == 16:
            or_ = 1
        elif command == 5:
             neg = 1
        elif((command == 2 and cmd.var[1] == 0) or command == 11):
             boolean = 1
             liste.append((neg + boolean) % 2)
             neg = 0
        elif(cmd.get_var(command - 1)):
             boolean = 1
             liste.append((neg + boolean) % 2)
             neg = 0
        else:
            liste.append((neg + boolean) % 2)
            neg = 0
        command = read_program(sensor, cmd)
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

def read_program(sensor, cmd, sens=1):
    """
    algorithme permetant de lire la bande
    retourne une liste de 0 et de 1
    """
    global indice, Buffer_, BUFFERSIZE

    # ERROR ON ESSAYE DE RECULER ALORS QUE LA LISTE EST VIDE
    if (sens == -1 and Buffer_[:indice] == []):
        raise 1
    # 0N RECULE
    elif (sens == -1):
        indice -= 1
        return Buffer_[indice]
    # SI BUFFER N EST PAS VIDE
    elif len(Buffer_[indice:]) > 0:
        return_value = Buffer_[indice]
        indice += 1
        #print(return_value)
        return return_value
    # SI BUFFER EST VIDE
    sc.motor12(1)
    Buffer_ = [50]
    if_while = 1
    while ((not sc.code_exit(cmd, Buffer_[-1])) and len(Buffer_) * if_while < BUFFERSIZE):
        if Buffer_[0] == 50:
            Buffer_ = []
        Buffer_.append(sc.get_cmd(sensor))
        if Buffer_[-1] <= 1:
            if_while = -1
    indice = 0
    sc.motor12(0)  # arrete les moteurs
    ######################
    return read_program(sensor, cmd)

def back(sensor, cmd, count):
    while count > 2:
         count -= 1
         Buffer_ = read_program(sensor, cmd, -1)
    del Buffer_

def skip(sensor, cmd):
    command = read_program(sensor, cmd)
    count = 1
    count_end = 1
    while count_end > 0:
        count += 1
        if command == 26:
            count_end -= 1
        elif command == 0 or command == 1:
            count_end += 2
        command = read_program(sensor, cmd)
    command = read_program(sensor, cmd, -1)
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
    command = read_program(sensor, cmd)
    count = 1
    while_count = 0
    while command != 26:
         if command == 0:
            verif, count_bool = Boolean_find(cmd, sensor)
            if (verif):
                count += interpret_program(cmd, sensor)
            else:
               count += skip(sensor, cmd)
         elif command == 1:
            verif, count_bool = Boolean_find(cmd, sensor)
            count += count_bool
            while (verif):
                while_count = interpret_program(cmd, sensor)
                back(sensor, cmd, while_count + count_bool)
                verif, count_bool = Boolean_find(cmd, sensor)
            count += skip(sensor, cmd)
         else:
            count += 1
            sc.exec_simple_command(cmd, command)
         count += 1
         command = read_program(sensor, cmd)
    print("close")
    return count
