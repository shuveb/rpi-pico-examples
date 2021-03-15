import machine
import utime
import _thread

led_red = machine.Pin(15, machine.Pin.OUT)
led_blue = machine.Pin(14, machine.Pin.OUT)

def blue_thread():
    while True:
        led_blue.value(1)
        utime.sleep(0.5)
        led_blue.value(0)
        utime.sleep(0.5)


_thread.start_new_thread(blue_thread, ())

while True:
    led_red.value(1)
    utime.sleep(0.5)
    led_red.value(0)
    utime.sleep(0.5)

