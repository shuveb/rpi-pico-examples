import machine
import utime
button = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(15, machine.Pin.OUT)

print("Welcome to GPIO input polling")

while True:
    if button.value() == 1:
        print("You pressed the button!")
        led.toggle()
        utime.sleep(0.2)