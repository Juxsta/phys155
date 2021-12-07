import board
import time
from digitalio import DigitalInOut, Direction
from adafruit_hcsr04 import HCSR04


button = DigitalInOut(board.D0) #toggle switch
gate = DigitalInOut(board.D1) #activation voltage of npn transistor
button.direction = Direction.INPUT
gate.direction = Direction.OUTPUT

open_loop = True
while True:
    if open_loop and button.value:
        open_loop = True #relay is open and load is off
        gate.value = False
    elif !open_loop and button.value:
        open_loop = False #relay is closed and load is on
        gate.value = True
    time.sleep(2)