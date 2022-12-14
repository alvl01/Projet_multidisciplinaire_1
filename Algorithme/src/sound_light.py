###### SOURCE ######
#https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/blob/main/adafruit_circuitplayground/circuit_playground_base.py
####################

import neopixel
import time
import board

class Solution:
    _audio_out = None
    def __init__(self) -> None:
        self._pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
    @property
    def pixels(self):
        return self._pixels
