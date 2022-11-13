import gc
import time
import board
import digitalio
import time
import busio
print(gc.mem_free())
#import adafruit_tcs34725
#import source as sc
#from adafruit_crickit import crickit
from adafruit_ht16k33 import segments
print(gc.mem_free())
#ss = crickit.seesaw
#pot = crickit.SIGNAL1
#led = digitalio.DigitalInOut(board.LED)
#led.direction = digitalio.Direction.OUTPUT
#i2c = board.I2C()
#sensor = adafruit_tcs34725.TCS34725(i2c)
#sensor.integration_time = 50
#sensor.gain = 4

while True:
    """
    il reste:
        -la creation des fonction commandes
        -la fonction error_music
        -la fonction couleur
    """

    #led.value = True
    """
    if (0):
        red = sensor.color_rgb_bytes[0] * 10
        green = sensor.color_rgb_bytes[1] * 10
        blue = sensor.color_rgb_bytes[2] * 5
        median = ((red+1) * green * blue)**(1/3)
        valeur = 40
        count = 0
        for col in [red, blue, green]:
            if col - median > valeur:
                count += 1
        if count > 1:
            color = "white"
        elif red - median > valeur:
            color = "red"
        elif green - median > valeur:
            color = "green"
        elif blue - median > valeur:
            color = "blue"
        if (red != 0 or green != 0 or blue != 0):
            print('Color: ({0}, {1}, {2} {3})'.format(red, green, blue, color))
    try:
        if (ss.analog_read(pot) < 1):
            print("hello")
            interpret_program(read_program(sensor))
    except 1:
        sc.error_music()
    """


