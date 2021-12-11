# Helper to convert analog input to voltage
from analogio import  AnalogIn
import board
import pwmio
from digitalio import DigitalInOut, Direction, Pull
import time
MAX_FREQ= 100e3
analog_in = AnalogIn(board.A3)

def get_frequency() -> float:
    return (analog_in.value * MAX_FREQ) / 65536

class State:
    freq:float = 10
    pwm = pwmio.PWMOut(board.D0, frequency=freq) # Set PWM Pin
    is_freq_low = DigitalInOut(board.D1)
    is_freq_high = DigitalInOut(board.D2)

    def __init__(self):
        self.is_freq_low.direction = Direction.OUTPUT
        self.is_freq_high.direction = Direction.OUTPUT



    def set_freq(self, freq):
        if (freq < 10e3):
            self.is_freq_low.value = True
            self.is_freq_high.value = False
        else:
            self.is_freq_high.value = True
            self.is_freq_low.value = False
        self.pwm.frequency = freq

    frequency = property(freq,set_freq)
    

state = State()

while True:
    state.frequency = get_frequency()
    time.sleep(13e-3) # 13ms 
    
    
