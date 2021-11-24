#!/usr/bin/env python3

from aibot import app
from aibot import testing
from aibot import state_machine

print("hello from main")

if __name__ == "__main__":

	try:
		print("initializing")
		app.init()
		print("Initialization done")
		state_machine.execute_mission()
	except KeyboardInterrupt:
		
		print("\n\nInterrupted via CTRL+C")
		app.exit()


