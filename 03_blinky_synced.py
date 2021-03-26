# This program is essentially the same as 02_blinky_thread.py. This one however
# uses MicroPython's lock primitive to coordinate activity between two threads

# The circuit
# Via 330 ohm resistors, connect two LEDs to ground
# from pins 14 and 15.

import machine
import utime
import _thread

# create 2 Pin objects from pins 14 and 15 where our 2 LEDs are connected
led_red = machine.Pin(15, machine.Pin.OUT)
led_blue = machine.Pin(14, machine.Pin.OUT)

# create a lock object. This acts as a mutex.
led_lock = _thread.allocate_lock()

# common function that blinks an LED
def blink_an_led(the_led):
    the_led.value(1)
    utime.sleep(0.5)
    the_led.value(0)
    utime.sleep(0.5)

# our thread function that simply calls blink_an_led() in a tight loop
def blue_thread(led):
    while True:
        led_lock.acquire()
        blink_an_led(led) # critical section controlled by the mutex
        led_lock.release()

# Start a thread. This causes the MicroPython runtime to utilize the
# second CPU core automatically. The Raspberry Pi Pico has only 2 cores.
# This means that you can create only one thread in addition to the already
# running main thread.
_thread.start_new_thread(blue_thread, (led_blue,))

# Our main thread is used to link the red LED
while True:
    led_lock.acquire()
    blink_an_led(led_red) # critical section controlled by the mutex
    led_lock.release()


