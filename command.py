from adafruit_circuitplayground.express import cpx
from adafruit_crickit import crickit
import time
import supervisor
supervisor.set_next_stack_limit(5100)

class Command():
    """
    var[negation,brosse_in,eject_dentifrisse,lumiere,pouce,
    timer,music,buton_onclick,brosse_detected,brosse_in_hand,nbr_end]
    """
    _var = [0,0,0,0,0,0,0,0,0,1,1]
    _color = (0,0,0)
    _start = 0
    _ss = crickit.seesaw
    # potentiometer connected to signal #3
    _pot = crickit.SIGNAL1
    _pot2 = crickit.SIGNAL2
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
            servo_12(1)
        print("ejecte brosse à dent : {0}".format(self.var[0]))

    def eject_dentifrisse(self):# OK
        if negation:
            dc_motor_34(0)
            self._start = int(time.time())
        else:
            dc_motor_34(1)
        print("ejecte dentifrisse : {0}".format(self.var[0]))


    def lumiere(self):
        if negation:
            self._color = (255,0,0)
        else:
            self._color = (0,255,0)
        print("lumière : {0}".format(self.var[0]))

    def pouce(self):# OK
        if negation:
            servo_3(-90)
        else:
            servo_3(90)
        print("pouce : {0}".format(self.var[0])) # si pouce rotation 90° else rotation -90°

    def timer(self):
        peak = 10 - (int(time.time()) - self._start)//18
        for i in range(10):
            if i < peak:
                if (peak == 10):
                    cp.pixels[i] = (255, 0, 0)
                else:
                    cp.pixels[i] = (255//(10 - peak), 255//peak, 0)
            else:
                cp.pixels[i] = (0, 0, 0)
        if peak == 0:
            time.sleep(1)
            for i in range(10):
                cp.pixels[i] = (0, 255, 0)
        cp.pixels.show()
        print("timer : {0}".format(self.var[0]))

    def hand_button_check(self):
        if self._ss.analog_read(self._pot) < 100:
            self.var[7] = 1
        else:
            self.var[7] = 0
        print("buton_onclick : {0}".format(self.var[0]))

    def capteur_distance_on(self):
        if self._ss.analog_read(self._pot2) < 100:
            self.var[7] = 1
        else:
            self.var[7] = 0
        print("brosse_detect : {0}".format(self.var[0]))
    def wait(self):# OK
        time.sleep(20)
        print("wait")
    def music1(self):
        cpx.play_file("music1.wav")
        time.sleep(2)
    def music2(self):
        cpx.play_file("music2.wav")
        time.sleep(2)
    def music3(self):
        cpx.play_file("music3.wav")
        time.sleep(2)
    def music4(self):
        cpx.play_file("music4.wav")
        time.sleep(2)
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
        crickit.dc_motor_2.throttle = intensity
        crickit.dc_motor_1.throttle = intensity
    def servo_12(self, intensity):
        crickit.continuous_servo_1.throttle = intensity
        crickit.continuous_servo_1.throttle = intensity
        time.sleep(2)
    def servo_3(self, angle):
        crickit.servo_1.angle = angle
        time.sleep(2)
liste_command = ["if","while","brosse_in","eject_dentifrisse","lumiere","not","pouce","timer","hand_button_check","capteur_distance_on","wait","music1","music2","music3","music4","and","or","","","","","","","","","","end"]
