import time
import battery_monitor

device = battery_monitor.Device()

while True:
    voltage = device.readVoltage()
    current = device.readCurrent()
    power = device.readPower()
    temperature = device.readTemperature()
    humidity = device.readHumidity()
    device.setVoltage(4.0)

    text = "Voltage = {:.2f} Current = {:.2f}\n".format(voltage, current)
    print(text)
    device.appendFile("./test.txt", text)
    time.sleep(1)