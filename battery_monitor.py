import time
import board
import adafruit_ina260
 
class Device:
    """
    Battery Monitor Library
    """
    def __init__(self):
        self.i2c = board.I2C()
        self.ina260 = adafruit_ina260.INA260(self.i2c)
        
        print("Device initialized")

    def readVoltage():
        return self.ina260.voltage