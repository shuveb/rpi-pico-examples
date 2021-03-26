# In this example, we read the temperature and humidity from a DHT22 sensor and
# display it on an LCD.

# The circuit:
# LCD's SDA -> Pico Pin 0
# LCD's SCL -> Pico Pin 1
# DHT22's data -> Pico Pin 12

from DHT22 import DHT22
import utime
import machine
from machine import I2C, Pin
from i2c_lcd import *

# The first argument is the I2C block. Pico has 2 blocks,
# 0 and 1. The blocks depends on the pin. See a pin out
# to understand this better.

i2c = I2C(0, sda=Pin(0), scl=Pin(1))
lcd = I2cLcd(i2c, 0x27, 2, 16)

# the DHT22's data pin is connected on the Pico's pin number 12
dht_data = Pin(12,Pin.IN,Pin.PULL_UP)
# Initialize the DHT22
dht_sensor = DHT22(dht_data)

while True:
    # read values from the DHT22
    T,H = dht_sensor.read()
    if T is None:
        print(" sensor error")
    else:
        print("{:3.1f}'C  {:3.1f}%".format(T,H))

    # clear the LCD screen and print formatted values
    lcd.clear()
    lcd.move_to(0, 0)
    temp_str = "Temp : {:3.1f}'C".format(T)
    lcd.putstr(temp_str)
    lcd.move_to(0, 1)
    humid_str = "Humid: {:3.1f}".format(H)
    lcd.putstr(humid_str)
    #DHT22 not responsive if delay to short
    utime.sleep_ms(1000)
