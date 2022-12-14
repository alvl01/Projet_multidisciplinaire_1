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

def skip(buf):
    global indice
    count = 1
    while buf[indice] != 26:
        count += 1
        indice += 1
    indice += 1
    return count - 1

def execute_program(cmd, buf):
    global indice
    command = get_command(buf)
    time.sleep(1)
    count = 1
    while_count = 0
    while command != 26:
         if command == 0:
            get_command(buf)
            get_command(buf)
            if (cmd.var[1] == 0):
                count += execute_program(cmd, buf)
            else:
               count += skip(buf)
         elif command == 1:
            get_command(buf)
            get_command(buf)
            count += 2
            while (cmd.var[1] == 0):
                while_count = execute_program(cmd, buf)
                indice = indice - while_count - 2
            count += skip(buf)
         else:
            count += 1
            exec_simple_command(cmd, command)
         count += 1
         command = get_command(buf)
    return count

def exec_simple_command(cmd, cmd_i):
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
    elif (cmd_i == 25):
        cmd.final()
    cmd.var[0] = 0
