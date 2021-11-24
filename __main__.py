#!/usr/bin/env python3

from aibot import app
from aibot import scientific_method

print("hello from main")

if __name__ == "__main__":

	try:
		print("initializing")
		app.init()
		print("Initialization done")
		scientific_method.ramp_climb()
	except KeyboardInterrupt:
		
		print("\n\nInterrupted via CTRL+C")
		app.exit()


