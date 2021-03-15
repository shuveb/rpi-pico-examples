import machine
import utime
button = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(15, machine.Pin.OUT)
button_presses = 0

print("Welcome to GPIO interrupt handling!")

def button_press_handler(pin):
    global button_presses
    led.toggle()
    button_presses += 1

button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_press_handler)

while True:
    print("Button presses so far:", button_presses)
    utime.sleep(1)