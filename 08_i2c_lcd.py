import machine
from machine import I2C, Pin
import utime
from i2c_lcd import *


i2c = I2C(0, sda=Pin(0), scl=Pin(1))
lcd = I2cLcd(i2c, 0x27, 2, 16)

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    lcd.clear()
    lcd.move_to(0, 0)
    temp_str = "Chip temp: {:2.2f}".format(temperature)
    lcd.putstr(temp_str)
    utime.sleep(2)