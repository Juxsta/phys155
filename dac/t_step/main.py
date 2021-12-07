import board
import digitalio
import time
from math import sin,ceil,pi
from analogio import AnalogIn

pins = [] ## Array to reference digital pins
analog_in = AnalogIn(board.A2)
MAX_FREQ = 10e3

for pin,index in zip([board.D1,board.D2,board.D3,board.D4],range(0,5)): ## Initialize Digital Out Pins
    pins.append(digitalio.DigitalInOut(pin))
    pins[index].direction = digitalio.Direction.OUTPUT

def sin16(t): # 4 bit resolution
    return ceil(sin(t)*8+8) ## return int (0,16) 

def write_pins(num:int): # Write 4 bit binary to pins
    bit_mask = b'1000'
    i = 0
    while (bit_mask != 0):
        pins[i].value = (num & bit_mask) >> 3 - i ## Assign binary value starting from MSB to LSB. 
        bit_mask >> 1 ## shift the bit mask right until all pins have been assigned a value
        i+=1


def get_Freq(): # Get Frequency from potentiometer
    return (analog_in.value * MAX_FREQ) / 65536

t = 0
while True:
    f = get_Freq()
    t_step = 1/(4*f) ## sample at double the nyquist rate for better resolution
    scalar_out = sin16(2*pi*f*t)
    write_pins(scalar_out)
    t+=t_step
    time.sleep(t_step)