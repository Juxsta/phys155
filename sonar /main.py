import board
import time
from digitalio import DigitalInOut, Direction
from adafruit_hcsr04 import HCSR04

leds = {
    'green': DigitalInOut(board.D3),
    'yellow': DigitalInOut(board.D4),
    'red': DigitalInOut(board.D0)
}

for led in leds:
    print(leds[led].direction)
    leds[led].direction = Direction.OUTPUT
    print(leds[led].direction)

with HCSR04(trigger_pin=board.D2, echo_pin=board.D1) as sonar:
    try:
        while True:
            print(sonar.distance)
            # if sonar.distance - 30 > 5:
            #     leds['red'].value = True
            # elif sonar.distance - 30 > 0:
            #     leds[yellow].value = True
            # else:
            #     leds['green'].value = True
            # time.sleep(2)
            # for led in leds:
            #     leds[led].value = False
            time.sleep(2)
    except KeyboardInterrupt:
        pass