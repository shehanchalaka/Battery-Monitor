import time
import battery_monitor

device = battery_monitor.Device()

while True:
    voltage = device.readVoltage()

    print("Voltage: %.2f V" % voltage)

    time.sleep(1)