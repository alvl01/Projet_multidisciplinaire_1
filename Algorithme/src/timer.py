from sound_light import Solution
from Check_button import Check_button
import time
class Timer:
        _sol = Solution()
        _check = Check_button()
        @property
        def sol(self):
            return self._sol
        @property
        def check(self):
            return self._check
        def timer(self):
            n = 0
            var = 0
            checker = 0
            while not checker:
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
                    var = 1
                    time.sleep(1)
                    for i in range(10):
                        self.sol.pixels[i] = (0, 255, 0)
                self.sol.pixels.show()
                time.sleep(1)
                checker = self.check.button_check()
            if not var:
                for i in range(10):
                    self.sol.pixels[i] = (255, 0, 0)
            else:
                for i in range(10):
                    self.sol.pixels[i] = (0, 255, 0)
            return var
