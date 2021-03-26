# Timers can be used to periodically execute tasks without having to worry
# about them in the main thread. In this example, we move the tasks of
# blinking an LED to a timer callback. Timers are backed by real hardware
# timers that various microcontrollers generally have. You need to check
# the manual of the microcontroller you're working on to see how many
# hardware timers it supports.

# The circuit:
# Via 330 ohm resistor, connect an LED to ground from pin 15.

import machine
import utime

led = machine.Pin(15, machine.Pin.OUT)
timer = machine.Timer()
timer_calls = 0

# Timers interrupt the currently running task. The CPU saves the current
# task's state, executes the timer's interrupt handler and once it's done,
# restores the original task and continues to execute it.
def timer_int_handler(timer):
    global timer_calls
    timer_calls += 1
    led.toggle()

# Setup the timer interrupt handler. We set this up as a periodic timer.
timer.init(period=1000, mode=machine.Timer.PERIODIC, callback=timer_int_handler)

# In the main thread, we simply print the value of a variable once every second.
# Once every second, this main thread is interrupted by the timer hardware so
# that the interrupt handler can run. It increments that variable.
while True:
    utime.sleep(1)
    print("Timer calls:", timer_calls)
