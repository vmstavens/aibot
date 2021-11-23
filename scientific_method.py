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

def cs():
    while True:
        try:
            hw.print_cs()
    

        except KeyboardInterrupt:
            print("\n\nInterrupted via CTRL+C")
            app.exit()


def grap_can():
    hw.motors.on(-50,-50)
    while True:
        try:
            if hw.ts.is_pressed:
                print("PRESSED")
                hw.motors.off()
                hw.mot_g.on(-10)

        except KeyboardInterrupt:
            hw.mot_g.on(0)
            print("\n\nInterrupted via CTRL+C")
            app.exit()


grap_can()


#hw.motors.follow_line_dual(4.0, 0.0, 0.0, -90)
   



    
