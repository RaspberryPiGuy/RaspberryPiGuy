#!/usr/bin/env python

# Scott Flemings Rainbow HAT Python Script
# Displays the TEMPERATURE, PRESSURE AND CLEARS SCREEN USING THE A,B,C BUTTONS
# Cycles a single LED from Right to Left in RED and highlights the current pressure in CYAN

import time
import rainbowhat as rh

A = 0
B = 1
C = 2

mode = A # Starting mode  = Temperature

# define touch for A,B,C

@rh.touch.press()
def touch_press(channel):
	global mode
	mode = channel

while True: #Main Loop
	
	for pixel in range(7):
			rh.rainbow.clear()
			rh.rainbow.set_pixel(pixel, 128, 0, 0, brightness=0.1)
			rh.rainbow.show()
			time.sleep(0.05)
	
	pressure = int(rh.weather.pressure()) / 100
	temperature = (rh.weather.temperature())
	rh.display.clear()
		
	#Prints the current temperature on screen and on the Rainbow HAT display when you press A
	
	if mode == A:
		rh.lights.rgb(1,0,0)
		rh.display.print_float(temperature)
		rh.display.show()
		print('Current temperature in Degrees is\t\t'),(temperature)
	
	#Prints the current pressure on screen and on the Rainbow HAT display when you press B
				
	if mode == B:
		rh.lights.rgb(0,1,0)
		rh.display.print_float(pressure, decimal_digits=0, justify_right=True)
		rh.display.show()
		print('Current Pressure in Millibars is\t\t'),(pressure)
		
	#Clears the Rainbow HAT display when you press C
				
	if mode == C:
		rh.lights.rgb(0,0,1)
		rh.rainbow.show()
		rh.rainbow.clear()
		rh.display.show()
		rh.display.clear()
		print('Rainbow HAT is running\t\t\t\tDISPLAY OFF')
		
	if pressure >= float(1030): # Light up Pixel 0 (DRY)
		pass
		rh.rainbow.set_pixel(0, 0, 128, 0,brightness=1.0)
		rh.rainbow.show()
		rh.rainbow.clear()
		
	elif pressure >= float(1020) <= float(1029): # Light up Pixel 1 (FAIR)
		pass
		rh.rainbow.set_pixel(1, 0, 128, 0,brightness=1.0)
		rh.rainbow.show()
		rh.rainbow.clear()
		
	elif pressure >= float(1010) <= float(1019): # Light up Pixel 2 (FAIR TO CHANGE)
		pass
		rh.rainbow.set_pixel(2, 0, 128, 0,brightness=1.0)
		rh.rainbow.show()
		rh.rainbow.clear()
		
	elif pressure >= float(1000) <= float(1009): #Light up Pixel 3 (CHANGE)
		pass
		rh.rainbow.set_pixel(3, 0, 128, 0,brightness=1.0)
		rh.rainbow.show()
		rh.rainbow.clear()
	
	elif pressure >= float(990) <= float(999): #Light up Pixel 4 (CHANGE TO RAIN)
		pass
		rh.rainbow.set_pixel(4, 0, 128, 0,brightness=1.0)
		rh.rainbow.show()
		rh.rainbow.clear()
	
	elif pressure >= float(980) <= float(989): #Light up Pixel 5 (RAIN)
		pass
		rh.rainbow.set_pixel(5, 0, 128, 0,brightness=1.0)
		rh.rainbow.show()
		rh.rainbow.clear()

	elif pressure <= float(979): # Light up Pixel 6 (STORMY)
		pass
		rh.rainbow.set_pixel(6, 0, 128, 0,brightness=1.0)
		rh.rainbow.show()
		rh.rainbow.clear()
		
		
	
		
		

