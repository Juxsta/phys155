# LED traffic light
# https://sjsu.instructure.com/courses/1431665/assignments/5770945

import time
import board
from digitalio import DigitalInOut, Direction, Pull

# init LEDs
leds = []
for i in range(3):
    leds[i] = exec(f'DigitalInOut(board.D{i}')

# main loop
n = 0
while True:
    time.sleep(50)
    leds[n].value = True
    time.sleep(200)
    leds[n].value = False
    n = n + 1
    if n > 2:
        n = 0