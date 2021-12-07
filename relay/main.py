import board
import time
from digitalio import DigitalInOut, Direction
from adafruit_hcsr04 import HCSR04


button = DigitalInOut(board.D0)
gate = DigitalInOut(board.D1)
gate.direction = Direction.OUTPUT

open_loop = True
while True:
    if open_loop and button.value:
        open_loop = True
        gate.value = False
    elif !open_loop and button.value:
        open_loop = False
        gate.vale = True
    time.sleep(2)