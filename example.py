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

    # for i in range (3, 4.5, 0.1):
    #     print("Current loop value = %f" % i)
    #     device.setVoltage(i)

    #     time.sleep(10)

    device.setVoltage(3.5)
    time.sleep(10)

    device.setVoltage(4.2)
    time.sleep(10)

    device.setVoltage(3.85)
    time.sleep(10)

    device.setVoltage(3.98)
    time.sleep(10)

    device.setVoltage(4.05)
    time.sleep(10)