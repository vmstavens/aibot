#!/usr/bin/env python3

# navigation constants
SPEED_MAX_NATIVE          = 1050 # native units (immutable)
SPEED_FWD                 = 45.0 # percent (60)
SPEED_FWD_FAST            = 70 # SPEED_FWD * 1.2 # percent (70) || 1.2
SPEED_TURN                = 30 # SPEED_FWD * 0.5 # percent (30) || 0.5
SPEED_REV                 = 40 # SPEED_FWD * 0.8 # percent (60) || 0.8
SPEED_OFFSET              = 40 # SPEED_FWD * 0.5 # percent (30) || 0.5

# hw constants
ADDR_GS                   = "ev3-ports:in3"
ADDR_CS_L                 = "ev3-ports:in1"
ADDR_CS_R                 = "ev3-ports:in2"
ADDR_TS                   = "ev3-ports:in4"

ADDR_MOT_L                = "ev3-ports:outB"
ADDR_MOT_R                = "ev3-ports:outA"
ADDR_MOT_G                = "ev3-ports:outC"

# threshold species value before it is categorized as BLACK
# white 100 <---> 0 black
CS_TH_BLACK               = 10 
LS_TH_BLACK               = 10 

# line follower PID (dual)
SLEEP_TIME                = None # dt
LP_CUTOFF_FREQ            = 10 # Hz
FOLLOW_LINE_DUAL_P        = 3.2
FOLLOW_LINE_DUAL_I        = 0.51
FOLLOW_LINE_DUAL_D        = 0.5

# gyro follower PID
FOLLOW_GYRO_P             = 3.0
FOLLOW_GYRO_I             = 0.05
FOLLOW_GYRO_D             = 2.0

#STATES
IDLE = 0
FOLLOW_LINE_FORWARD = 1
RAMP_UP = 2
GRAB_CAN = 3
RAMP_DOWN = 4
FOLLOW_LINE_BACKWARD = 5
MISSION_DONE = 6
global STATE 
STATE = IDLE 