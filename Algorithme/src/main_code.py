from color import TCS34725
import read
import time
import gc
sensor = TCS34725(board.I2C())
sensor.integration_time = 50
sensor.gain = 4
Buffer_ = []
while True:
    if crickit.seesaw.analog_read(crickit.SIGNAL3) < 100:
        Buffer_ = prog.read_program(sensor)
        del(read.read_program)
        del(read.get_color)
        del(read.code_exit)
        del(read.format_command)
        del(read.get_cmd)
        del(read.motor12)
        del(sensor)
        del(TCS34725)
        gc.mem_free()
        gc.collect()
        import execute as ex
        from command import Command
        cmd = Command()
        ex.execute_program(cmd, Buffer_)
