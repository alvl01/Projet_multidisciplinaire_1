from adafruit_crickit import crickit
import gc
import time

class Command:
    """
    var[negation,brosse_in,eject_dentifrisse,lumiere,pouce,
    timer,music,buton_onclick,brosse_detected,brosse_in_hand,nbr_end]
    """
    _var = [0,0,0,0,0,0,0,0,0,1,1]
    # VAR
    @property
    def var(self):
        return self._var
    @var.setter
    def var(self, value):
        self._var = value
    def get_var(self, index):
        return self._var[index]
    def set_var(self, index, value):
        self._var[index] = value
    ##### FUNCTION
    def brosse_in(self):# OK
        if negation:
            servo_12(0)
        else:
            servo_12(180)
        print("ejecte brosse à dent : {0}".format(self.var[0]))

    def eject_dentifrisse(self):# OK
        if negation:
            dc_motor_34(0)
        else:
            dc_motor_34(1)
        print("ejecte dentifrisse : {0}".format(self.var[0]))


    def lumiere(self):
        from sound_light import Solution
        self.var[6] = 1
        time.sleep(1)
        for i in range(10):
            sol.pixels[i] = (255, 0, 0)
        del sol
        gc.mem_free()
        gc.collect()
        print("lumière : {0}".format(self.var[0]))

    def pouce(self):# OK
        if negation:
            servo_3(-90)
        else:
            servo_3(90)
        print("pouce : {0}".format(self.var[0])) # si pouce rotation 90° else rotation -90°

    def timer(self, n):
        peak = 10 - n
        from sound_light import Solution
        for i in range(10):
            if i < peak:
                if (peak == 10):
                    sol.pixels[i] = (255, 0, 0)
                else:
                    sol.pixels[i] = (255//(10 - peak), 255//peak, 0)
            else:
                sol.pixels[i] = (0, 0, 0)
        if peak == 0:
            self.var[6] = 1
            time.sleep(1)
            for i in range(10):
                sol.pixels[i] = (0, 255, 0)
        sol.pixels.show()
        del sol
        gc.mem_free()
        gc.collect()
        self.var[6] = 1
        print("timer : {0}".format(self.var[0]))

    def hand_button_check(self):
        if crickit.seesaw.analog_read(crickit.SIGNAL1) < 100:
            self.var[7] = 1
        else:
            self.var[7] = 0
        print("buton_onclick : {0}".format(self.var[0]))

    def capteur_distance_on(self):
        if crickit.seesaw.analog_read(crickit.SIGNAL2) < 100:
            self.var[7] = 1
        else:
            self.var[7] = 0
        print("brosse_detect : {0}".format(self.var[0]))
    def wait(self):# OK
        time.sleep(20)
        print("wait")
    def music1(self):
        from sound_light import Solution
        sol = Solution()
        sol.play_file("music1.wav")
        del sol
        gc.mem_free()
        gc.collect()
        time.sleep(2)
    def music2(self):
        from sound_light import Solution
        sol.play_file("music2.wav")
        del sol
        gc.mem_free()
        gc.collect()
        time.sleep(2)
    def music3(self):
        from sound_light import Solution
        sol.play_file("music3.wav")
        del sol
        gc.mem_free()
        gc.collect()
        time.sleep(2)
    def music4(self):
        from sound_light import Solution
        sol.play_file("music4.wav")
        del sol
        gc.mem_free()
        gc.collect()
        time.sleep(2)
    def final(self):
        if (self.var[6]):
            self.good()
        else:
            self.not_good()
    # UNCALLABLE FUNCTION
    def good():
      self.pouce()
      self.music3() #"SUPER👌"
      self.wait()
      self.var[0] = 1
      self.pouce()
      self.var[0] = 0
    def not_good():
      self.var[0] = 1
      self.pouce()
      self.var[0] = 0
      self.lumiere() # rouge
      self.music4() #"NUUUUUUUUUUUUUUL, tu vas avoir des carries"
      self.wait()
      self.pouce()
    def dc_motor_34(self, intensity):
        crickit.driver_1.throttle = intensity
        crickit.driver_2.throttle = intensity
    def servo_12(self, angle):
        crickit.servo_1.angle = angle
        crickit.servo_2.angle = angle
        time.sleep(2)
    def servo_3(self, angle):
        crickit.servo_3.angle = angle
        time.sleep(2)
#liste_command = ["if","while","brosse_in","eject_dentifrisse","lumiere","not","pouce","timer","hand_button_check","capteur_distance_on","wait","music1","music2","music3","music4","and","or","","","","","","","","","","end"]
