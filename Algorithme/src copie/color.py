import time
import board
import gc
from adafruit_bus_device import i2c_device
from micropython import const

try:
    from typing import Tuple
    from busio import I2C
except ImportError:
    pass
#https://github.com/adafruit/Adafruit_CircuitPython_TCS34725.git

# Register and command constants:
_COMMAND_BIT = const(0x80)
_REGISTER_ENABLE = const(0x00)
_REGISTER_ATIME = const(0x01)
_REGISTER_ID = const(0x12)
_REGISTER_APERS = const(0x0C)
_REGISTER_CONTROL = const(0x0F)
_REGISTER_SENSORID = const(0x12)
_REGISTER_STATUS = const(0x13)
_REGISTER_CDATA = const(0x14)
_REGISTER_RDATA = const(0x16)
_REGISTER_GDATA = const(0x18)
_REGISTER_BDATA = const(0x1A)
_ENABLE_AIEN = const(0x10)
_ENABLE_AEN = const(0x02)
_ENABLE_PON = const(0x01)
_GAINS = (1, 4, 16, 60)
_CYCLES = (0, 1, 2, 3, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60)
#_INTEGRATION_TIME_THRESHOLD_LOW = 2.4
#_INTEGRATION_TIME_THRESHOLD_HIGH = 614.4


class TCS34725:
    _BUFFER = bytearray(3)

    def __init__(self, i2c: I2C, address: int = 0x29):
        self._device = i2c_device.I2CDevice(i2c, address)
        self._active = False
        self.integration_time = 2.4
        # Check sensor ID is expectd value.
        sensor_id = self._read_u8(_REGISTER_SENSORID)
        if sensor_id not in (0x44, 0x10):
            raise RuntimeError("Could not find sensor, check wiring!")

    @property
    def color_rgb_bytes(self):##################################################  OK
        """Read the RGB color detected by the sensor.  Returns a 3-tuple of
        red, green, blue component values as bytes (0-255).
        """
        r, g, b, clear = self.color_raw

        # Avoid divide by zero errors ... if clear = 0 return black
        if clear == 0:
            return (0, 0, 0)

        # Each color value is normalized to clear, to obtain int values between 0 and 255.
        # A gamma correction of 2.5 is applied to each value as well, first dividing by 255,
        # since gamma is applied to values between 0 and 1
        red = int(pow((int((r / clear) * 256) / 255), 2.5) * 255)
        green = int(pow((int((g / clear) * 256) / 255), 2.5) * 255)
        blue = int(pow((int((b / clear) * 256) / 255), 2.5) * 255)

        # Handle possible 8-bit overflow
        red = min(red, 255)
        green = min(green, 255)
        blue = min(blue, 255)
        return (red, green, blue)

    @property
    def active(self):################################################## OK
        """The active state of the sensor.  Boolean value that will
        enable/activate the sensor with a value of True and disable with a
        value of False.
        """
        return self._active

    @active.setter
    def active(self, val: bool):##################################################  OK
        val = bool(val)
        if self._active == val:
            return
        self._active = val
        enable = self._read_u8(_REGISTER_ENABLE)
        if val:
            self._write_u8(_REGISTER_ENABLE, enable | _ENABLE_PON)
            time.sleep(0.003)
            self._write_u8(_REGISTER_ENABLE, enable | _ENABLE_PON | _ENABLE_AEN)
        else:
            self._write_u8(_REGISTER_ENABLE, enable & ~(_ENABLE_PON | _ENABLE_AEN))

    @property
    def integration_time(self):##################################################  OK
        """The integration time of the sensor in milliseconds."""
        return self._integration_time

    @integration_time.setter
    def integration_time(self, val: float):##################################################  OK
        cycles = int(val / 2.4)
        self._integration_time = (
            cycles * 2.4
        )  # pylint: disable=attribute-defined-outside-init
        self._write_u8(_REGISTER_ATIME, 256 - cycles)

    @property
    def gain(self):##################################################  OK
        """The gain of the sensor.  Should be a value of 1, 4, 16,
        or 60.
        """
        return _GAINS[self._read_u8(_REGISTER_CONTROL)]

    @gain.setter
    def gain(self, val: int):##################################################  OK
        if val not in _GAINS:
            raise ValueError(
                "Gain should be one of the following values: {0}".format(_GAINS)
            )
        self._write_u8(_REGISTER_CONTROL, _GAINS.index(val))

    @property
    def interrupt(self):
        """True if the interrupt is set. Can be set to False (and only False)
        to clear the interrupt.
        """
        return bool(self._read_u8(_REGISTER_STATUS) & _ENABLE_AIEN)

    @interrupt.setter
    def interrupt(self, val: bool):
        if val:
            raise ValueError(
                "Interrupt should be set to False in order to clear the interrupt"
            )
        with self._device:
            self._device.write(b"\xe6")

    @property
    def color_raw(self):################################################## OK
        """Read the raw RGBC color detected by the sensor.  Returns a 4-tuple of
        16-bit red, green, blue, clear component byte values (0-65535).
        """
        was_active = self.active
        self.active = True
        while not self._valid():
            time.sleep((self._integration_time + 0.9) / 1000.0)
        data = tuple(
            self._read_u16(reg)
            for reg in (
                _REGISTER_RDATA,
                _REGISTER_GDATA,
                _REGISTER_BDATA,
                _REGISTER_CDATA,
            )
        )
        self.active = was_active
        return data

    @property
    def cycles(self):
        """The persistence cycles of the sensor."""
        if self._read_u8(_REGISTER_ENABLE) & _ENABLE_AIEN:
            return _CYCLES[self._read_u8(_REGISTER_APERS) & 0x0F]
        return -1

    @cycles.setter
    def cycles(self, val: int):
        enable = self._read_u8(_REGISTER_ENABLE)
        if val == -1:
            self._write_u8(_REGISTER_ENABLE, enable & ~(_ENABLE_AIEN))
        else:
            self._write_u8(_REGISTER_ENABLE, enable | _ENABLE_AIEN)
            self._write_u8(_REGISTER_APERS, _CYCLES.index(val))

    def _valid(self) -> bool:################################################## OK
        # Check if the status bit is set and the chip is ready.
        return bool(self._read_u8(_REGISTER_STATUS) & 0x01)

    def _read_u8(self, address: int) -> int:################################################## OK
        # Read an 8-bit unsigned value from the specified 8-bit address.
        with self._device as i2c:
            self._BUFFER[0] = (address | _COMMAND_BIT) & 0xFF
            i2c.write_then_readinto(self._BUFFER, self._BUFFER, out_end=1, in_end=1)
        return self._BUFFER[0]

    def _read_u16(self, address: int) -> int:################################################## OK
        # Read a 16-bit unsigned value from the specified 8-bit address.
        with self._device as i2c:
            self._BUFFER[0] = (address | _COMMAND_BIT) & 0xFF
            i2c.write_then_readinto(self._BUFFER, self._BUFFER, out_end=1, in_end=2)
        return (self._BUFFER[1] << 8) | self._BUFFER[0]

    def _write_u8(self, address: int, val: int):################################################## OK
        # Write an 8-bit unsigned value to the specified 8-bit address.
        with self._device as i2c:
            self._BUFFER[0] = (address | _COMMAND_BIT) & 0xFF
            self._BUFFER[1] = val & 0xFF
            i2c.write(self._BUFFER, end=2)
