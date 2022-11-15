class Command():
    _negation = 0
    _brosse_in = 0
    _eject_dentifrisse = 0
    _lumiere = 0
    _pouce = 0
    _timer = 0
    _music = 0
    _buton_onclick = 0
    _brosse_detected = 0
    _brosse_in_hand = 1
    _last_command = []

    # NEGATION
    @property
    def negation(self):
        return self._negation
    @negation.setter
    def negation(self, value):
        self._negation = value
    # BROSSE IN
    @property
    def brosse_in(self):
        return self._brosse_in
    @brosse_in.setter
    def brosse_in(self, value):
        self._brosse_in = value
    # EJECT DENTIFRISSE
    @property
    def eject_dentifrisse(self):
        return self._eject_dentifrisse
    @eject_dentifrisse.setter
    def eject_dentifrisse(self, value):
        self._eject_dentifrisse = value
    # LUMIERE
    @property
    def lumiere(self):
        return self._lumiere
    @lumiere.setter
    def lumiere(self, value):
        self._lumiere = value
    # POUCE
    @property
    def pouce(self):
        return self._pouce
    @pouce.setter
    def pouce(self, value):
        self._pouce = value
    # TIMER
    @property
    def timer(self):
        return self._timer
    @timer.setter
    def timer(self, value):
        self._timer = value
    # MUSIC
    @property
    def music(self):
        return self._music
    @music.setter
    def music(self, value):
        self._music = value
    # BUTTON ON CLICK
    @property
    def buton_onclick(self):
        return self._buton_onclick
    @buton_onclick.setter
    def buton_onclick(self, value):
        self._buton_onclick = value
    # BROSSE DETECTED
    @property
    def brosse_detected(self):
        return self._brosse_detected
    @brosse_detected.setter
    def brosse_detected(self, value):
        self._brosse_detected = value
    # BROSSE IN HAND
    @property
    def brosse_in_hand(self):
        return self._brosse_in_hand
    @brosse_in_hand.setter
    def brosse_detected(self, value):
        self._brosse_in_hand = value
    # LAST COMMAND
    @property
    def last_command(self):
        return self._last_command
    @last_command.setter
    def last_command(self, value):
        self._last_command = value

    def fbrosse_in(self):
        print("ejecte brosse à dent : {0}".format(self.negation))
        self.last_command = [2, self.negation]

    def feject_dentifrisse(self):
        print("ejecte dentifrisse : {0}".format(self.negation))
        self.last_command = [3, self.negation]


    def flumiere(self):
        print("lumière : {0}".format(self.negation))
        self.last_command = [4, self.negation]

    def fpouce(self):
        print("pouce : {0}".format(self.negation)) # si pouce rotation 90° else rotation -90°
        self.last_command = [6, self.negation]

    def ftimer(self):
        print("timer : {0}".format(self.negation))
        self.last_command = [7, self.negation]

    def fmusic(self):
        print("music : {0}".format(self._negation))
        self.last_command = [8, self._negation]
        if not self._buton_onclick:
            self._buton_onclick = 1
        else:
            self.music += 1

    def fbuton_onclick(self):
        print("buton_onclick : {0}".format(self.negation))
        self.last_command = [9, self.negation]

    def fbrosse_detect(self):
        print("brosse_detect : {0}".format(self.negation))
        self.last_command = [10, self.negation]
    def fwait(self):
        print("wait")
        self.last_command = [11, self.negation]
    def fbrosse_in_hand(self):
        print("brosse in hand")
        self.last_command = [12, self.negation]
