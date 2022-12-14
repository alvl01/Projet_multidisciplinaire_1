import time
from command import Command

indice = -1
#https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/blob/main/adafruit_circuitplayground/circuit_playground_base.py
#github adafruit_tcs34725
def get_command(buf):
    global indice
    indice += 1
    if buf[indice:] == []:
        return 26
    return buf[indice]

def Boolean_find(cmd, buf):
    ###
    # recoit une liste de nombre et un indice
    # Retourne TRUE ou FALSE
    ###
    neg = 0
    return_value = 0
    boolean = 0
    count = 0
    command = get_command(buf)
    count += 1
    while command != 26: # tant que c'est pas un END
        if command == 5: # Si c'est un NON
             cmd.var[0] = 1
        if(cmd.var[1] == 0):
             boolean = 1
        neg = cmd.var[0]
        return_value = (neg + boolean) % 2
        cmd.var[0] = 0
        command = get_command(buf)
        count += 1
    return return_value, count

def back(count):
    global indice
    indice -= count

def skip(buf):
    """
    cette fonction permet de passer du code, quand if ou while est false
    """
    global indice
    count = 1
    while buf[indice] != 26: # tant qu on est dans if/while
        count += 1
        indice += 1
    indice += 1
    return count - 1

def execute_program(cmd, buf):
    """
    detecte si c'est un if un while ou une commande simple
    si c'est un while ou un if, il verifie la condition
    dans le cas du if, si la condition est vérifiée,
    il execute par récursivité l'intérieur
    dans le cas du while, tant que la condition est vérifiée,
    il exectute par récursivité l'intérieur
    """
    command = get_command(buf)
    time.sleep(1)
    count = 1
    while_count = 0
    while command != 26: # tant que le programme n'est pas fini
         if command == 0: # si c est un if
            verif, count_bool = Boolean_find(cmd, buf) # check cond
            if (verif):
                count += execute_program(cmd, buf) # exec inter if
            else:
               count += skip(buf) # skip inter du if
         elif command == 1: # si c est un while
            verif, count_bool = Boolean_find(cmd, buf) # check cond
            count += count_bool
            while (verif):
                while_count = execute_program(cmd, buf) # exec inter while
                #print(while_count + count_bool)
                back(while_count + count_bool) # revient debut while
                verif, count_bool = Boolean_find(cmd, buf) # re-check cond
            count += skip(buf) # skip inter du if
         else: # si c est juste une action
            count += 1
            exec_simple_command(cmd, command)
         count += 1
         command = get_command(buf)
    return count

def exec_simple_command(cmd, cmd_i):
    """
    execute une commande sans boucle sans condition
    """
    if (cmd_i == 5):
        cmd.var[0] = 1
        return
    if (cmd_i == 2):
        cmd.brosse_in()
    elif (cmd_i == 3):
        cmd.eject_dentifrisse()
    elif (cmd_i == 4):
        cmd.lumiere()
    elif (cmd_i == 6):
        cmd.pouce()
    elif (cmd_i == 7):
        cmd.timer()
    elif (cmd_i == 8 or cmd_i == 9):
        cmd.button_check()
    elif (cmd_i == 10):
        cmd.wait()
    elif (cmd_i == 11):
        cmd.music1()
    elif (cmd_i == 12):
        cmd.music2()
    elif (cmd_i == 13):
        cmd.music3()
    elif (cmd_i == 14):
        cmd.music4()
    elif (cmd_i == 17):
        cmd.final()
    cmd.var[0] = 0
