import unittest
import sys
sys.path.append("../src/")
import prog
from command import Command

def create_sensor(nb):
    c = []
    for n in nb:
        a = []
        a.append(n // 9)
        a.append((n - a[0] * 9) // 3)
        a[0] = n - a[0] * 9 - a[1] * 3
        a.append(n // 9)
        for b in a:
            if b == 0:
                c.append("red")
            elif b == 1:
                c.append("green")
            else:
                c.append("blue")
            c.append("white")
    return c
def return_test(nb):
    sensor = create_sensor(nb)
    #print(sensor)
    #print(sensor)
    cmd = Command();
    cmd.var[7] = 0
    a = prog.interpret_program(cmd, sensor)
    b = cmd.last_command
    del cmd
    prog.sc.test_again()
    #print(nb)
    return b

class TestProg(unittest.TestCase):
    """def test_read_prog(self):
        test = []
        test.append(0)
        test.append(26)
        for i in range(1,27):
            cmd = Command();
            test[0] = i
            test_1 = create_sensor(test)
            a = prog.read_program(test_1, cmd)
            prog.sc.test_again()
            prog.buffer_again()
            del cmd
            self.assertEqual(a,i)"""
    def test_interpret_prog(self):
        # TEST 1
        print("########################")
        print("######## TEST 1 ########")
        print("########################")
        nb = [ 8, 7, 26]
        a = return_test(nb)
        self.assertEqual(a,[7,0])

        # TEST 2
        print("########################")
        print("######## TEST 2 ########")
        print("########################")
        nb = [0, 5, 8, 26, 8, 26, 26]
        a = return_test(nb)
        self.assertEqual(a,[8,0])

        # TEST 3
        print("########################")
        print("######## TEST 3 ########")
        print("########################")
        nb = [0, 5, 8, 26, 5, 8, 26, 26]
        a = return_test(nb)
        self.assertEqual(a,[8,1])
        # TEST 4

        print("########################")
        print("######## TEST 4 ########")
        print("########################")
        nb = [1, 5, 8, 26, 5, 8, 26, 26]
        a = return_test(nb)
        self.assertEqual(a,[8,1])

        # TEST 5
        print("########################")
        print("######## TEST 5 ########")
        print("########################")
        nb = [1, 5, 8, 26, 0, 5, 8, 26, 5, 8, 26, 26, 26]
        a = return_test(nb)
        self.assertEqual(a,[8,1])

        # TEST 6
        print("########################")
        print("######## TEST 6 ########")
        print("########################")
        nb = [6, 0, 5, 7, 26, 1, 5, 8, 26, 5, 8, 26, 26, 8, 26]
        a = return_test(nb)
        self.assertEqual(a,[8,1])
if __name__ == '__main__':
    unittest.main()
