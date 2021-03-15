import machine
import utime
import _thread

led_red = machine.Pin(15, machine.Pin.OUT)
led_blue = machine.Pin(14, machine.Pin.OUT)

led_lock = _thread.allocate_lock()

def blue_thread():
    while True:
        led_lock.acquire()
        led_blue.value(1)
        utime.sleep(0.5)
        led_blue.value(0)
        utime.sleep(0.5)
        led_lock.release()


_thread.start_new_thread(blue_thread, ())

while True:
    led_lock.acquire()
    led_red.value(1)
    utime.sleep(0.5)
    led_red.value(0)
    utime.sleep(0.5)
    led_lock.release()


