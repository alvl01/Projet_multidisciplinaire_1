import board
from adafruit_crickit import crickit
import adafruit_tcs34725
import digitalio
import src
import prog
"""
il reste:
    -la creation des fonction commandes
    -la fonction error_music
    -la fonction couleur
"""
ss = crickit.seesaw
pot = crickit.SIGNAL1
i2c = board.I2C()
sensor = adafruit_tcs34725.TCS34725(i2c)
sensor.integration_time = 50
sensor.gain = 4

def main():
    while True:
        try:
            if fork():
                if (ss.analog_read(pot) < 100):
                    print("hello")
                    prog.interpret_program(sensor)
            else:
                prog.do_in_parallele()
        except 1:
            src.error_music()


if __name__ = "__main__":
    main()
