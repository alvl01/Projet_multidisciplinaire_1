import time
import board
import adafruit_tcs34725
from adafruit_crickit import crickit
ss = crickit.seesaw
i2c = board.I2C()
sensor = adafruit_tcs34725.TCS34725(i2c)
sensor.integration_time = 60
sensor.gain = 4
# make two variables for the motors to make code shorter to type
motor_1 = crickit.dc_motor_1
motor_2 = crickit.dc_motor_2

while False:
    crickit.continuous_servo_1.throttle = 1.0 # Forwards
    crickit.continuous_servo_2.throttle = 1.0 # Forwards
    time.sleep(4)
    print("go")
    crickit.continuous_servo_1.throttle = 0   # Stop
    crickit.continuous_servo_2.throttle = 0   # Stop
    time.sleep(4)
motor_1.throttle = 0.8  # full speed forward
motor_2.throttle = -0.8
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
    blue = color[2] * 10
    count = 0
    txt_color=-1
    if red > blue and red > green:
        txt_color = 0
    elif green > blue and red < green:
        txt_color = 1
    else:
        txt_color = 2
    #print (str(median)+" "+str(red)+" "+str(green)+" "+str(blue)+" "+str(txt_color))
    return txt_color
def get_cmd(sensor):
    cmd = []
    colors = get_color(sensor)
    white_space = 0
    while len(cmd) < 3:
        while colors == white_space: # tant qu on est sur du blanc
            colors = get_color(sensor)  # recupère les couleurs
        # on est plus sur du blanc
        cmd.append(colors)
        while colors == cmd[-1]:  # tant qu'on est sur du la couleur
            colors = get_color(sensor)  # recupère les couleurs
        # on est plus sur de la couleur
        white_space = colors
        print(cmd)
    command = format_command(cmd)
    del cmd
    return command
last = 0
while True:
    a = get_color(sensor)
    if a != last:
        last = a
        print(a)



import gc
import time
import board
import digitalio
import busio
import os
import adafruit_tcs34725
#import source as sc
from adafruit_crickit import crickit
#from adafruit_circuitplayground.express import cpx
#del cpx
#cpx.play_file("rimshot.wav")

#import pwmio
ss = crickit.seesaw
#pot = crickit.SIGNAL1
#i2c = board.I2C()
#sensor = adafruit_tcs34725.TCS34725(i2c)
#sensor.integration_time = 100
#sensor.gain = 4
while True:
    crickit.continuous_servo_1.throttle = 1.0 # Forwards
    crickit.continuous_servo_2.throttle = 1.0 # Forwards
    time.sleep(4)
    print("go")
    crickit.continuous_servo_1.throttle = 0   # Stop
    crickit.continuous_servo_2.throttle = 0   # Stop
    time.sleep(4)
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
while True:
    """
    il reste:
        -la creation des fonction commandes
        -la fonction error_music
        -la fonction couleur
    """
    while (1):
        print(sc.get_color(sensor))


