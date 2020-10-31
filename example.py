import time
import battery_monitor

device = battery_monitor.Device()

device.setVoltage(4.0)

while True:
    voltage = device.readVoltage()
    current = device.readCurrent()
    power = device.readPower()
    temperature = device.readTemperature()
    humidity = device.readHumidity()

    text = "V {:.3f} C {:.3f} Temperature = {:.2f} Humidity = {:.2f}\n".format(voltage, current, temperature, humidity)
    
    print(text)

    device.appendFile("./test.txt", text)

    time.sleep(1)