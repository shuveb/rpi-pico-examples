# The last time we read values from the the on-chip temperature sensor via ADC
# channel 4, we printed it on to the serial console. This time, we do the same,
# but we display the temperature on a I2C LCD screen.

# The circuit:
# LCD's SDA -> Pico Pin 0
# LCD's SCL -> Pico Pin 1

import machine
from machine import I2C, Pin
import utime
from i2c_lcd import *

# Configure I2C with SDA as pin 0 and SCL as pin 1
i2c = I2C(0, sda=Pin(0), scl=Pin(1))
# setup our LCD with IC2 address 0x27, 2 rows and 16 columns
lcd = I2cLcd(i2c, 0x27, 2, 16)

# We want to read value from the on-chip temperature sensor which is connected
# to ADC channel 4
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

while True:
    # read the temperature and convert it
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    # clear the LCD
    lcd.clear()
    # move to row 0, col 0
    lcd.move_to(0, 0)
    # display the formatted string on the LCD
    temp_str = "Chip temp: {:2.2f}".format(temperature)
    lcd.putstr(temp_str)
    utime.sleep(2)