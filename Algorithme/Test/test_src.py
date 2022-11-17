import unittest
import sys
sys.path.append("../src/")
import source as sc

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
    print(sensor)
    #print(sensor)
    cmd = Command();
    a = prog.interpret_program(cmd, sensor)
    b = cmd.last_command
    del cmd
    prog.sc.test_again()
    print(nb)
    return b

class TestProg(unittest.TestCase):
    def test_format_command(self):
        for i in range(1,27):
            a = []
            a.append(i // 9)
            a.append((i - a[0] * 9) // 3)
            a[0] = i - a[0] * 9 - a[1] * 3
            a.append(i // 9)
            self.assertEqual(sc.format_command(a),i)
    def test_interpret_prog(self):
        pass

if __name__ == '__main__':
    unittest.main()
