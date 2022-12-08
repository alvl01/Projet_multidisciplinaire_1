import time
import source as sc
from command import Command

indice = 7
Buffer_ = []
BUFFERSIZE = 7

def Boolean_find(cmd, sensor):
    ###
    # recoit une liste de nombre et un indice
    # Retourne TRUE ou FALSE
    ###
    neg = 0
    return_value = 0
    boolean = 0
    count = 0
    command = read_program(sensor, cmd)
    count += 1
    while command != 26: # tant que c'est pas un END
        if command == 5: # Si c'est un NON
             neg = 1
        elif((command == 2 and cmd.var[1] == 0) or command == 11):
             boolean = 1
             return_value = (neg + boolean) % 2
             neg = 0
        elif(cmd.get_var(command - 1)):
             boolean = 1
             return_value = (neg + boolean) % 2
             neg = 0
        else:
            return_value = (neg + boolean) % 2, count
            neg = 0
        command = read_program(sensor, cmd)
        count += 1
    return return_value, count

def read_program(sensor, cmd, sens=1):
    """
    algorithme permetant de lire la bande
    retourne une liste de 0 et de 1
    """
    global indice, Buffer_, BUFFERSIZE
    #print(Buffer_)
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
            if not 0 in Buffer_[:-1] and not 1 in Buffer_[:-1]:
                Buffer_ = Buffer_[-1:]
    indice = 0
    sc.motor12(0)  # arrete les moteurs
    ######################
    return read_program(sensor, cmd)

def back(sensor, cmd, count):
    global indice, Buffer_
    if indice >= len(Buffer_) - 1:
        indice = 0
    else:
        indice -= count

def skip(sensor, cmd):
    """
    cette fonction permet de passer du code, quand if ou while est false
    """
    global indice, Buffer_
    command = read_program(sensor, cmd)
    count = 1
    count_end = 1
    while count_end > 0: # tant qu on est dans if/while
        count += 1
        if command == 26: # si on a un end  -1
            count_end -= 1
        elif command == 0 or command == 1: # si on a un if/while +2 (passer le if/while)
            count_end += 2
        if Buffer_[indice:] != []:
            command = read_program(sensor, cmd)
    command = read_program(sensor, cmd, -1)
    return count - 1
def interpret_program(cmd, sensor):
    """
    detecte si c'est un if un while ou une commande simple
    si c'est un while ou un if, il verifie la condition
    dans le cas du if, si la condition est vérifiée,
    il execute par récursivité l'intérieur
    dans le cas du while, tant que la condition est vérifiée,
    il exectute par récursivité l'intérieur
    """
    command = read_program(sensor, cmd)
    count = 1
    while_count = 0
    while command != 26: # tant que le programme n'est pas fini
         if command == 0: # si c est un if
            verif, count_bool = Boolean_find(cmd, sensor) # check cond
            if (verif):
                count += interpret_program(cmd, sensor) # exec inter if
            else:
               count += skip(sensor, cmd) # skip inter du if
         elif command == 1: # si c est un while
            verif, count_bool = Boolean_find(cmd, sensor) # check cond
            count += count_bool
            while (verif):
                while_count = interpret_program(cmd, sensor) # exec inter while
                print(while_count + count_bool)
                back(sensor, cmd, while_count + count_bool) # revient debut while
                verif, count_bool = Boolean_find(cmd, sensor) # re-check cond
            count += skip(sensor, cmd) # skip inter du if
         else: # si c est juste une action
            count += 1
            sc.exec_simple_command(cmd, command)
         count += 1
         command = read_program(sensor, cmd)
    return count
