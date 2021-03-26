# In this example, we read ADC channel 4, on to which the on-chip
# temperature sensor is connected. We convert the temperature sensor's analogue
# value into a number and print it on the console.

import machine
import utime

# We need a reference to ADC channel 4
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

# Read number, convert and print every 2 seconds
while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    print("Chip temperature is:", temperature)
    utime.sleep(2)