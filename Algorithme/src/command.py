class Command():
    """
    var[negation,brosse_in,eject_dentifrisse,lumiere,pouce,
    timer,music,buton_onclick,brosse_detected,brosse_in_hand,nbr_end]
    """
    _var = [0,0,0,0,0,0,0,0,0,1,1]
    _last_command = []

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
    # LAST COMMAND
    @property
    def last_command(self):
        return self._last_command
    @last_command.setter
    def last_command(self, value):
        self._last_command = value

    def fbrosse_in(self):
        print("ejecte brosse à dent : {0}".format(self.var[0]))
        self.last_command = [2, self.var[0]]

    def feject_dentifrisse(self):
        print("ejecte dentifrisse : {0}".format(self.var[0]))
        self.last_command = [3, self.var[0]]


    def flumiere(self):
        print("lumière : {0}".format(self.var[0]))
        self.last_command = [4, self.var[0]]

    def fpouce(self):
        print("pouce : {0}".format(self.var[0])) # si pouce rotation 90° else rotation -90°
        self.last_command = [6, self.var[0]]

    def ftimer(self):
        print("timer : {0}".format(self.var[0]))
        self.last_command = [7, self.var[0]]

    def fmusic(self):
        print("music : {0}".format(self.var[0]))
        self.last_command = [8, self.var[0]]
        self._var[7] = 1

    def fbuton_onclick(self):
        print("buton_onclick : {0}".format(self.var[0]))
        self.last_command = [9, self.var[0]]

    def fbrosse_detect(self):
        print("brosse_detect : {0}".format(self.var[0]))
        self.last_command = [10, self.var[0]]
    def fwait(self):
        print("wait")
        self.last_command = [11, self.var[0]]
    def fbrosse_in_hand(self):
        print("brosse in hand")
        self.last_command = [12, self.var[0]]
    # UNCALLABLE FUNCTION
    def dc_motor_34(self, intensity):
        pass
    def servo_12(self, angle):
        pass
    def servo_3(self, angle):
        pass
    def lauch_sound(self, title):
        pass
