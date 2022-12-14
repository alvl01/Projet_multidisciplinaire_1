from adafruit_crickit import crickit

class Check_button:
    def button_check(self):
        if crickit.seesaw.analog_read(crickit.SIGNAL2) > 100:
            return 1
        else:
            return 0
