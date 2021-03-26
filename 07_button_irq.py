# In the previous example, we used GPIO polling to continuously monitor the
# state of a push button connected on a GPIO pin. Here, we get smart and
# let the CPU interrupt us and tell us if the button was pushed.

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

# Counter for button presses
button_presses = 0

# Be nice and greet people.
print("Welcome to GPIO interrupt handling!")

# IRQ handler for the button press
def button_press_handler(pin):
    global button_presses
    led.toggle()
    button_presses += 1

# setup the IRQ handler based on the pin object connected to the push button
button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_press_handler)

# In the main thread, we do not poll for button activity anymore. We print
# the value of the button_presses variable every second and go back to sleep.
# Whenever a button press occurs, the CPU interrupts the main thread and
# services the interrupt handler.
while True:
    print("Button presses so far:", button_presses)
    utime.sleep(1)