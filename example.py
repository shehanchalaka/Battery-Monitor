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

    text = "Temperature = {voltage:.2f} Humidity = {current:.2f}\n".format(voltage = voltage, current = current)
    device.appendFile("./test.txt", text)

    time.sleep(0.1)