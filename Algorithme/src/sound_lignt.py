###### SOURCE ######
#https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/blob/main/adafruit_circuitplayground/circuit_playground_base.py
####################

import neopixel
import audiocore
import time
import audioio
import digitalio
import board

class Solution:
    _audio_out = None
    def __init__(self) -> None:
        # CHRONO
        self.speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
        self.speaker_enable.switch_to_output(value=False)
        self.a = audioio.AudioOut(board.SPEAKER)
        self._pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
    @property
    def pixels(self):
        return self._pixels
    # MUSIC
    def play_file(self, file_name: str) -> None:
        self.speaker_enable.value = True
        with audiocore.WaveFile(open(file_name, "rb")) as wavefile:
            self.a.play(wavefile)
            while self.a.playing:
                pass
        self.speaker_enable.value = False
        gc.mem_free()
        gc.collect()
