import board
import time
from digitalio import DigitalInOut, Direction
from adafruit_hcsr04 import HCSR04


button = DigitalInOut(board.D0) #toggle switch
gate = DigitalInOut(board.D1) #activation voltage of npn transistor
button.direction = Direction.INPUT
gate.direction = Direction.OUTPUT

while True:
    if button.value:
        gate.value = ~gate.value
    time.sleep(.1)