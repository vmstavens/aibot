#!/usr/bin/env python3

from time import sleep
from aibot import hw
from aibot.constants import *


def init():

	print("initializing aibot...")
	# halt and reset motors
	hw.motors.stop()
	hw.motors.reset()
	hw.mot_g.on(10)
	sleep(1)
	hw.mot_g.on(0)
	

	# calibrate gyroscope
	hw.gs.calibrate()
	print("aibot has been initialized")


def exit():
	hw.motors.stop()
	hw.mot_g.on(10)
	sleep(1)
	hw.mot_g.on(0)




