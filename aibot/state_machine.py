#!/usr/bin/env python3

from aibot import hw
from aibot.constants import *


def execute_mission():
    global STATE
    

    while True:
        if STATE == IDLE:
            STATE = FOLLOW_LINE_FORWARD
        if STATE == FOLLOW_LINE_FORWARD:           
            STATE = hw.motors.line_follow(state=STATE, speed=-10)
        if STATE == RAMP_UP:
            STATE = hw.motors.line_follow(state=STATE, kp=1.2, ki=0.1, kd=0.1, speed=-50,)
        if STATE == GRAB_CAN:
            hw.mot_g.on(-10)
            hw.time.sleep(2)
            STATE = FOLLOW_LINE_BACKWARD
        if STATE == FOLLOW_LINE_BACKWARD:
            STATE = hw.motors.line_follow(state=STATE, speed=10)
        if STATE == RAMP_DOWN:
            STATE = hw.motors.line_follow(state=STATE, speed=10)
        if STATE == MISSION_DONE:
            hw.motors.off()
            hw.mot_g.on(10)
            hw.mot_g.on(0)

