# We used GPIO earlier to light LEDs up. Here's we used GPIOs for output
# In this example, we use GPIOs for input. We detect whenever an input goes
# high with a push button connected to Vcc

# The circuit:
# Via 330 ohm resistor, connect a LED to ground from pin 15.
# Connect a push button from pin 13 to Vcc.

import machine
import utime

# Setup pin 13 as input and set the programmable internal resistor to
# pull down. This makes pin 13 normally be low. Connecting it to Vcc
# via the push button will pull it high, which we can detect.
button = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Configure GPIO pin 15 as an output to light our LED
led = machine.Pin(15, machine.Pin.OUT)

# Be nice and greet people.
print("Welcome to GPIO input polling")

# In a loop see if the GPIO pin was pulled up, meaning the button was
# pressed. If it was, toggle our LED. Sleep a bit to debounce the
# push button.
while True:
    if button.value() == 1:
        print("You pressed the button!")
        led.toggle()
        utime.sleep(0.2)