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
#from adafruit_circuitplayground.express import cpx
import gc
print(gc.mem_free())
from source import Command

#cmd = Command()
print(gc.mem_free())
import source2 as sc
sc = 0
print(gc.mem_free())
gc.collect()
import time
time.sleep(1)
#print(time.time()
import board
print(gc.mem_free())
print("import TCS34725")
from adafruit_tcs34725 import TCS34725
time.sleep(0.5)
print(gc.mem_free())
print("import cricit")
from adafruit_crickit import crickit
time.sleep(0.5)
print(gc.mem_free())
print(gc.mem_free())
gc.collect()
time.sleep(0.5)
print(gc.mem_free())
time.sleep(200)
ss = crickit.seesaw
i2c = board.I2C()
sensor = TCS34725(i2c)
sensor.integration_time = 50
sensor.gain = 4
sc.motor12(0.9)
while False:
    cmd.servo_12(0)
    time.sleep(2)
    cmd.servo_12(1)
    time.sleep(2)
while True:
    print(sc.get_cmd(sensor))

sc.motor12(0)
while(True):
    cmd.timer()
    cmd.start_1()
    time.sleep(2)
    cmd.timer()
    cmd.start_1()
    time.sleep(2)
    cmd.timer()
    cmd.start_1()
    time.sleep(2)
    cmd.timer()
    cmd.start_1()
    time.sleep(2)
    cmd.timer()
    cmd.start_1()
    time.sleep(2)
    cmd.timer()
    cmd.start_1()
    time.sleep(2)
    cmd.timer()
    cmd.start_1()
    time.sleep(2)
    cmd.timer()
    cmd.start_1()
    time.sleep(2)
    cmd.timer()
    cmd.start_1()
    time.sleep(2)
    cmd.timer()
    cmd.start_1()
    time.sleep(2)
while False:
    cmd.servo_3(180)
    time.sleep(2)
    cmd.servo_3(0)
    time.sleep(2)
