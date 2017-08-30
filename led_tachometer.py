# Kenneth Latimer
# 8/29/17
# Description:
# 	Class containing information about LEDs and behavior for displaying information 
# 	to the user.

import RPi.GPIO as GPIO
import time

class LED_Tachometer:
	def __init__(self, led_pins, redline):
		self.led_pins = led_pins
		self.num_leds = len(led_pins)
		self.current_rpm = 0
		self.max_rpm = int(1000 * num_leds) # Using 1 LED per 1k RPM (for now)
		# Set up the GPIO
		GPIO.setmode(GPIO.BCM)
		for pin in led_pins:
			GPIO.setup(pin, GPIO.OUT)

	def display_rpm(self, current_rpm):
		led_pins = self.led_pins
		num_leds_on = int(round(current_rpm))
		# Turn on the proper number of LEDs
		for i in range(num_leds_on):
			GPIO.output(led_pins(i), GPIO.HIGH)

	def clear_rpm(self):
		for pin in self.led_pins:
			GPIO.output(pin, GPIO.LOW)