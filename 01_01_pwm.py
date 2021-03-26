# This example uses PWM to continuously fade an
# LED in and out.

# The circuit:
# Via 330 ohm resistor, connect a LED to ground
# from pin 15. If you don't want to use an
# external LED, you can change the LED_PIN
# variable to 25, which is the pin on which the
# internal LED is connected.

import time
from machine import Pin, PWM

LED_PIN = 15

# Construct PWM object, with LED on Pin().
pwm = PWM(Pin(LED_PIN))

# Set the PWM frequency.
pwm.freq(1000)

duty = 0
direction = 1

# Fade the LED in and out continuously.
while True:
    duty += direction
    if duty > 255:
        duty = 255
        direction = -1
        time.sleep(0.5)
    elif duty < 0:
        duty = 0
        direction = 1
        time.sleep(0.5)
    pwm.duty_u16(duty * duty)
    time.sleep(0.01)
