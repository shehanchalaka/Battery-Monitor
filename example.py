import time
import battery_monitor

device = battery_monitor.Device()

while True:
    voltage = device.readVoltage()
    current = device.readCurrent()
    power = device.readPower()
    temperature = device.readTemperature()
    humidity = device.readHumidity()

    text = "Temperature = {voltage:.2f} Humidity = {current:.2f}\n".format(voltage = voltage, current = current)
    
    print(text)

    device.appendFile("./test.txt", text)

    time.sleep(1)