from aibot import app
from aibot import hw
from aibot.constants import *
import time


def cali_test():
    if hw.motors.cs_r.reflected_light_intensity > 0:
        hw.motors.right_motor.on(30)
        time.sleep(1)
        hw.motors.right_motor.off()
    if hw.motors.cs_l.reflected_light_intensity > 0:
        hw.motors.left_motor.on(30)
        time.sleep(1)
        hw.motors.left_motor.off()


def test():
    try:
        while True:
            hw.motors.follow_line_dual(
            kp    = 4.3, 
            ki    = 5.6, 
            kd    = 0.01, 
            speed = 10)

    except KeyboardInterrupt:
        print("\n\nInterrupted via CTRL+C")
        app.exit()



    
