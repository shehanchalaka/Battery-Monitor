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

    for i in range (40, 61):
        print("Current wipre value = %f" % i)
        device.setVoltage(i)

        time.sleep(10)

    time.sleep(1)