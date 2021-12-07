import time
import board
import pwmio

# For the M0 boards:
piezo = pwmio.PWMOut(board.A2, duty_cycle=0, frequency=440, variable_frequency=True)

# For the M4 boards:
# piezo = pwmio.PWMOut(board.A1, duty_cycle=0, frequency=440, variable_frequency=True)

while True:
        piezo.frequency = 1000
        piezo.duty_cycle = 65535 // 2  # On 50%
        # time.sleep(0.25)  # On for 1/4 second
        piezo.duty_cycle = .5  # Off
        # time.sleep(0.05)  # Pause between notes
    # time.sleep(0.5)
