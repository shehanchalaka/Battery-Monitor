import time
import battery_monitor

device = battery_monitor.Device()

while True:
    voltage = device.readVoltage()
    current = device.readCurrent()
    power = device.readPower()
    temperature = device.readTemperature()
    humidity = device.readHumidity()

    print(
        "Current: %.2f mA Voltage: %.2f V Power:%.2f mW\nTemperature: %0.1f C Humidity: %0.1f %%"
        % (voltage, current, power, temperature, humidity)
    )

    device.appendFile("./test.txt", "Temperature = {} Humidity = {}".format(voltage, current))

    time.sleep(1)