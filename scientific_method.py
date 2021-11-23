from aibot import app
from aibot import hw
from aibot.constants import *
import time

def test():
    try:
        hw.motors.follow_line_dual(
            kp    = 4.3, 
            ki    = 5.6, 
            kd    = 0.01, 
            speed = 50)

    except KeyboardInterrupt:
        print("\n\nInterrupted via CTRL+C")
        app.exit()



    
