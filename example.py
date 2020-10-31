import time
import battery_monitor

device = battery_monitor.Device()

while True:
    voltage = device.readVoltage()
    current = device.readCurrent()
    power = device.readPower()
    temperature = device.readTemperature()
    humidity = device.readHumidity()

    # print(
    #     "Current: %.2f mA Voltage: %.2f V Power:%.2f mW\nTemperature: %0.1f C Humidity: %0.1f %%"
    #     % (voltage, current, power, temperature, humidity)
    # )

    device.setVoltage(45)
    time.sleep(5)
    device.setVoltage(46)
    time.sleep(5)
    device.setVoltage(47)
    time.sleep(5)
    device.setVoltage(48)
    time.sleep(5)
    device.setVoltage(49)
    time.sleep(5)
    device.setVoltage(50)
    time.sleep(5)
    device.setVoltage(51)
    time.sleep(5)
    device.setVoltage(52)
    time.sleep(5)
    device.setVoltage(53)
    time.sleep(5)
    device.setVoltage(54)
    time.sleep(5)
    device.setVoltage(55)
    time.sleep(5)
    device.setVoltage(56)
    time.sleep(5)
    device.setVoltage(57)
    time.sleep(5)