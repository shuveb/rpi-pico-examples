from DHT22 import DHT22
import utime
import machine
from machine import I2C, Pin
from i2c_lcd import *


i2c = I2C(0, sda=Pin(0), scl=Pin(1))
lcd = I2cLcd(i2c, 0x27, 2, 16)


dht_data = Pin(12,Pin.IN,Pin.PULL_UP)
dht_sensor=DHT22(dht_data)

while True:
    T,H = dht_sensor.read()
    if T is None:
        print(" sensor error")
    else:
        print("{:3.1f}'C  {:3.1f}%".format(T,H))
        
    lcd.clear()
    lcd.move_to(0, 0)
    temp_str = "Temp : {:3.1f}'C".format(T)
    lcd.putstr(temp_str)
    lcd.move_to(0, 1)
    humid_str = "Humid: {:3.1f}".format(H)
    lcd.putstr(humid_str)
    #DHT22 not responsive if delay to short
    utime.sleep_ms(1000)
