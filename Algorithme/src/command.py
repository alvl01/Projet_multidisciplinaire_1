from adafruit_crickit import crickit
import gc
import time
class Command:
    _var = [0,0,0,0]
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
    def brosse_in(self):
        if self.var[0]:
            self.servo_12(0)
        else:
            self.servo_12(180)
            time.sleep(3)
            if crickit.seesaw.analog_read(crickit.SIGNAL2) > 100:
                self.var[1] = 1
            else:
                self.var[1] = 0
            self.var[1] += 1
            self.var[1] %= 2
        print(gc.mem_free())
        gc.collect()
    def eject_dentifrisse(self):
        self.dc_motor_34()
        print(gc.mem_free())
        gc.collect()
    def button_check(self):
        if crickit.seesaw.analog_read(crickit.SIGNAL2) > 100:
            self.var[1] = 1
        else:
            self.var[1] = 0
    def pouce(self):
        if self.var[0]:
            self.servo_3(0)
        else:
            self.servo_3(180)
        print(gc.mem_free())
        gc.collect()
    def timer(self):
        from timer import Timer
        time = Timer()
        self.var[3] = time.timer()
        del(time)
        del (Timer)
        print(gc.mem_free())
        gc.collect()
    def wait(self):
        time.sleep(2)
        print("wait")
    def final(self):
        if (self.var[3]):
            self.good()
        else:
            self.not_good()
    def good(self):
        self.pouce()
        self.wait()
        self.var[0] = 0
        self.servo_3(90)
        print(gc.mem_free())
        gc.collect()
    def not_good(self):
        self.var[0] = 1
        self.pouce()
        self.var[0] = 0
        self.wait()
        self.servo_3(90)
        print(gc.mem_free())
        gc.collect()
    def dc_motor_34(self):
        crickit.drive_1.fraction = 1
        crickit.drive_2.fraction = 1
        time.sleep(2)
        crickit.drive_1.fraction = 0
        crickit.drive_2.fraction = 0
    def servo_12(self, angle):
        crickit.servo_1.angle = angle
        crickit.servo_2.angle = angle
        time.sleep(2)
    def servo_3(self, angle):
        crickit.servo_3.angle = angle
        time.sleep(2)
