from adafruit_crickit import crickit
import gc
import time
from sound_light import Solution
class Command:
    """
    var[negation,brosse_in,eject_dentifrisse,lumiere,pouce,
    timer,music,buton_onclick,brosse_detected,brosse_in_hand,nbr_end]
    """
    _var = [0,0,0,0,0,0,0,0,0,1,1]
    _sol = Solution()
    # VAR
    @property
    def var(self):
        return self._var
    @property
    def sol(self):
        return self._sol
    @var.setter
    def var(self, value):
        self._var = value
    def get_var(self, index):
        return self._var[index]
    def set_var(self, index, value):
        self._var[index] = value
    ##### FUNCTION
    def brosse_in(self):# OK
        if self.var[0]:
            self.servo_12(0)
        else:
            self.servo_12(180)
        print("ejecte brosse à dent : {0}".format(self.var[0]))
        print(gc.mem_free())

    def eject_dentifrisse(self):# OK
        if self.var[0]:
            self.dc_motor_34(0)
        else:
            self.dc_motor_34(1)
        print("ejecte dentifrisse : {0}".format(self.var[0]))
        print(gc.mem_free())


    def lumiere(self):
        self.var[6] = 1
        time.sleep(1)
        for i in range(10):
            self.sol.pixels[i] = (255, 0, 0)
        gc.mem_free()
        gc.collect()
        print("lumière : {0}".format(self.var[0]))
        print(gc.mem_free())

    def pouce(self):# OK
        if self.var[0]:
            self.servo_3(0)
        else:
            self.servo_3(180)
        print("pouce : {0}".format(self.var[0])) # si pouce rotation 90° else rotation -90°
        print(gc.mem_free())

    def timer(self):
        n = 0
        self.var[1] = 0
        while not self.var[1]:
            print("OK CHEF")
            n += 1
            peak = 10 - n // 2
            for i in range(10):
                if i < peak:
                    if (peak == 10):
                        self.sol.pixels[i] = (255, 0, 0)
                    else:
                        self.sol.pixels[i] = (255//(10 - peak), 255//peak, 0)
                else:
                    self.sol.pixels[i] = (0, 0, 0)
            if peak == 0:
                self.var[6] = 1
                time.sleep(1)
                for i in range(10):
                    self.sol.pixels[i] = (0, 255, 0)
            self.sol.pixels.show()
            time.sleep(1)
            self.button_check()
        gc.mem_free()
        gc.collect()
        print("timer : {0}".format(self.var[0]))
        print(gc.mem_free())

    def button_check(self):
        print(crickit.seesaw.analog_read(crickit.SIGNAL2))
        if crickit.seesaw.analog_read(crickit.SIGNAL2) > 100:
            self.var[1] = 1
            print("OK")
        else:
            self.var[1] = 0
        print("buton_onclick : {0}".format(self.var[0]))
        print(gc.mem_free())

    def wait(self):# OK
        time.sleep(20)
        print("wait")
    def music1(self):
        self.sol.play_file("music1.wav")
        gc.mem_free()
        gc.collect()
        time.sleep(2)
        print(gc.mem_free())
    def music2(self):
        self.sol.play_file("music2.wav")
        gc.mem_free()
        gc.collect()
        time.sleep(2)
        print(gc.mem_free())
    def music3(self):
        self.sol.play_file("music3.wav")
        gc.mem_free()
        gc.collect()
        time.sleep(2)
        print(gc.mem_free())
    def music4(self):
        self.sol.play_file("music4.wav")
        gc.mem_free()
        gc.collect()
        time.sleep(2)
        print(gc.mem_free())
    def final(self):
        if (self.var[6]):
            self.good()
        else:
            self.not_good()
    # UNCALLABLE FUNCTION
    def good(self):
      self.pouce()
      #self.music3() #"SUPER👌"
      self.wait()
      self.var[0] = 0
      self.servo_3(90)
    def not_good(self):
      self.var[0] = 1
      self.pouce()
      self.var[0] = 0
      self.lumiere() # rouge
      #self.music4() #"NUUUUUUUUUUUUUUL, tu vas avoir des carries"
      self.wait()
      self.servo_3(90)
    def dc_motor_34(self, intensity):
        crickit.drive_1.fraction = intensity
        crickit.drive_2.fraction = intensity
    def servo_12(self, angle):
        crickit.servo_1.angle = angle
        crickit.servo_2.angle = angle
        time.sleep(2)
    def servo_3(self, angle):
        crickit.servo_3.angle = angle
        time.sleep(2)
#liste_command = ["if","while","brosse_in","eject_dentifrisse","lumiere","not","pouce","timer","hand_button_check","capteur_distance_on","wait","music1","music2","music3","music4","and","or","","","","","","","","","","end"]
