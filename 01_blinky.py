# This is the "Hello World" of embedded systems programs, blinking an LED.

# The circuit:
# Via 330 ohm resistor, connect a LED to ground
# from pin 15. If you don't want to use an
# external LED, you can change the LED_PIN
# variable to 25, which is the pin on which the
# internal LED is connected.

import machine
import utime

LED_PIN = 15

led = machine.Pin(LED_PIN, machine.Pin.OUT)

while True:
    led.value(1)
    utime.sleep(1)
    led.value(0)
    utime.sleep(1)