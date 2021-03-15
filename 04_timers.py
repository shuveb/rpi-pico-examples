import machine
import utime

led = machine.Pin(15, machine.Pin.OUT)
timer = machine.Timer()
timer_calls = 0
 
def timer_int_handler(timer):
    global timer_calls
    timer_calls += 1
    led.toggle()
 
timer.init(period=1000, mode=machine.Timer.PERIODIC, callback=timer_int_handler)

while True:
    utime.sleep(1)
    print("Timer calls:", timer_calls)
