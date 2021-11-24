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
            kp    = 3.5, 
            ki    = 0.30, 
            kd    = 0.65, 
            speed = -10)
    except KeyboardInterrupt:
        print("\n\nInterrupted via CTRL+C")
        app.exit()

def cs():
    while True:
        try:
            hw.print_cs()
    

        except KeyboardInterrupt:
            print("\n\nInterrupted via CTRL+C")
            app.exit()


def grap_can():
    print("HELLO FROM GRAP CAN")

    INIT = 0
    FOLLOW_LINE = 1
    GRAP_CAN = 2
    FIND_LINE = 3
    STATE = INIT

    while True:
        if STATE == INIT:
            STATE = FOLLOW_LINE
        if STATE == FOLLOW_LINE:
            hw.motors.line_follow()
            if hw.ts.ispressed():
                STATE = GRAP_CAN
        if STATE == GRAP_CAN:
            hw.motors.off()
            hw.mot_g.on(-10)
            STATE = FIND_LINE
        if STATE == FIND_LINE:
            hw.motors.line_follow(speed=10)
            time.sleep(5)
            hw.mot_g.off()










def ramp_climb():
    while True:
        if(hw.gs.value() >= 10):
            hw.motors.on(-30)
        if(hw.gs.value() < 10):
            hw.line_follow()



    
