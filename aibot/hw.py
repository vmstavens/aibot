#!/usr/bin/env python3

import time
from math import pi
from aibot.constants import *


from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor.lego import LightSensor
from ev3dev2.sensor.lego import GyroSensor

from ev3dev2.motor import Motor
from ev3dev2.motor import MoveTank, follow_for_ms, follow_for_forever
from ev3dev2.motor import SpeedPercent, speed_to_speedvalue, SpeedNativeUnits
from ev3dev2.wheel import EV3Tire

# ----------------------------------------------------------------------

# sensor objects
cs_r           = ColorSensor(ADDR_CS_R)
cs_l           = ColorSensor(ADDR_CS_L)
gs             = GyroSensor(ADDR_GS)
ts             = TouchSensor(ADDR_TS)

# motor objects
mot_r          = Motor(ADDR_MOT_R)
mot_l          = Motor(ADDR_MOT_L)
motors         = MoveTank(ADDR_MOT_L, ADDR_MOT_R)
mot_g		   = Motor(ADDR_MOT_G)

# set object of motors
motors.cs_r    = cs_r
motors.cs_l    = cs_l
motors.gyro    = gs
motors.ts      = ts

# ----------------------------------------------------------------------
	
# helper methods

def print_cs():

	cs_l  = motors.cs_l.reflected_light_intensity
	cs_r  = motors.cs_r.reflected_light_intensity

	print(cs_l, cs_r)

def min(lhs, rhs):
	return (lhs if lhs < rhs else rhs)

def max(lhs, rhs):
	return (lhs if lhs > rhs else rhs)

def abs(val):
	# return val * (-1 if val < 0 else 1)
	return val * ((val > 0) - (val < 0))

def saturate(val, limit):
	return max(min(val, limit), -limit)

# MoveTank.reset()
def reset(self):
	self.left_motor.reset()
	self.right_motor.reset()
	
# MoveTank.current_pos()
def current_pos(self):
	return { "left": self.left_motor.position, "right": self.right_motor.position }
	
# MoveTank.follow_for_dist()
def follow_for_dist(self, dist, pos_start):

	# callback function, in order to know when to stop line following

	pos_l = abs(self.left_motor.position  - pos_start["left"])
	pos_r = abs(self.right_motor.position - pos_start["right"])
	avg   = (pos_l + pos_r) / 2

	return (avg <= dist)

# ----------------------------------------------------------------------

def line_follow(self, state, kp=3.5, ki=0.30, kd=0.65, speed=-10):	

	# PID line follower with two color sensors
	# requires defintion of color sensors cs_l and cs_r

	e = e_prev = i  = 0.0

	speed = speed_to_speedvalue(speed)
	speed_native_units = speed.to_native_units(self.left_motor)
	max_speed = SPEED_MAX_NATIVE

	while True:
		print("GYRO: ", gs.value(), "    STATE: ", state)

		if gs.value() < -10 and state == FOLLOW_LINE_FORWARD:
			return RAMP_UP
		if ts.value():
			print("TS PRESSED")
			return GRAB_CAN
		if gs.value() > -5 and state == RAMP_UP:
			return FOLLOW_LINE_FORWARD
		if gs.value() < -10 and state == FOLLOW_LINE_BACKWARD:
			return RAMP_DOWN
		if gs.value() > -5 and state == RAMP_DOWN:
			return FOLLOW_LINE_BACKWARD


		e = self.cs_l.reflected_light_intensity - self.cs_r.reflected_light_intensity
		i += e
		d = (e - e_prev)
		u = (kp * e) + (ki * i) + (kd * d)
		e_prev = e

		# convert to native speed units (saturated)
		speed_left  = SpeedNativeUnits(saturate(speed_native_units - u, max_speed))
		speed_right = SpeedNativeUnits(saturate(speed_native_units + u, max_speed))

		#print("Speed LEFT: ", speed_left, "    SPEED RIGHT: ", speed_right)
		self.on(speed_left, speed_right)
				


# MoveTank.follow_line_for_dist()
def follow_line_for_dist(self, dist, speed):

	# follow the line for a specified distance at a specified speed
	# using dual color sensor

	pos_start = { "left": self.left_motor.position, "right": self.right_motor.position }

	self.follow_line_dual(
		kp           = FOLLOW_LINE_DUAL_P,
		ki           = FOLLOW_LINE_DUAL_I,
		kd           = FOLLOW_LINE_DUAL_D,
		speed        = SpeedPercent(speed),
		sleep_time   = SLEEP_TIME,
		follow_for   = follow_for_dist,
		dist         = dist,
		pos_start    = pos_start
	)

# MoveTank.follow_gyro_for()
def follow_gyro_for(self, dist, speed, angle = 0):

	# follow specified gyro angle at set speed and distance

	pos_start = { "left": motors.left_motor.position, "right": motors.right_motor.position }

	self.follow_gyro_angle(
		kp           = FOLLOW_GYRO_P,
		ki           = FOLLOW_GYRO_I,
		kd           = FOLLOW_GYRO_D,
		speed        = speed,
		target_angle = angle,
		sleep_time   = SLEEP_TIME,
		follow_for   = follow_for_dist,
		dist         = dist,
		pos_start    = pos_start
	)


# append extensions
MoveTank.reset                              = reset
MoveTank.current_pos                        = current_pos
MoveTank.follow_for_dist                    = follow_for_dist
MoveTank.follow_line_for_dist               = follow_line_for_dist
MoveTank.follow_gyro_for                    = follow_gyro_for
MoveTank.line_follow						= line_follow
