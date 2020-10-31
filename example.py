import time
import battery_monitor

device = battery_monitor.Device()

while True:
    voltage = device.readVoltage()
    current = device.readCurrent()
    power = device.readPower()
    temperature = device.readTemperature()
    humidity = device.readHumidity()

    text = "Temperature = {temperature:.2f} Humidity = {humidity:.2f}\n".format(temperature = temperature, humidity = humidity)
    
    print(text)

    device.appendFile("./test.txt", text)

    time.sleep(1)