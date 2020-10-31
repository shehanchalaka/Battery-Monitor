import time
import board
import adafruit_ina260
import adafruit_si7021

class Device:
    """
    Battery Monitor Library
    """
    def __init__(self):
        self.i2c = board.I2C()
        self.ina260 = adafruit_ina260.INA260(self.i2c)
        self.si7021 = adafruit_si7021.SI7021(self.i2c)

        print("Device initialized")

    def readVoltage(self):
        return self.ina260.voltage

    def readCurrent(self):
        return self.ina260.current

    def readPower(self):
        return self.ina260.power

    def readTemperature(self):
        return self.si7021.temperature

    def readHumidity(self):
        return self.si7021.relative_humidity