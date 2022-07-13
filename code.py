"""
Rotate servo back and forth
Amanda Zhang
2022/13/7
"""

from adafruit_motor import servo
import board
import time
import pwmio

# create variable for pwm
pwm = pwmio.PWMOut(board.A1, duty_cycle=2**15, frequency=50, variable_frequency=False)
# create variable for servo
srv = servo.Servo(pwm)

# main loop
while True:
    for ang in range(0, 185, 5):
        srv.angle = ang
        time.sleep(0.1)
    for ang in range(185, 0, 5):
        srv.angle = ang
        time.sleep(0.1)
