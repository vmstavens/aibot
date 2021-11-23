#!/usr/bin/env python3

from aibot import app
from aibot import scientific_method

print("hello from main")

if __name__ == "__main__":

	try:
		
		app.init()
		#app.run()
		scientific_method.test()
	except KeyboardInterrupt:
		
		print("\n\nInterrupted via CTRL+C")
		app.exit()


