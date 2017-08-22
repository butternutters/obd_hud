# Kenneth Latimer
# 8/21/17
# Description
# 	Sets up LED pins and does a gauge sweep

import RPi.GPIO as GPIO
import time

def toggle_leds (led_pins, state): # state is GPIO.HIGH or GPIO.LOW
	for pin in led_pins:
		GPIO.output(pin, state)

def sweep_leds (led_pins, delay): # Turns on led_pins in sequence, leaving them on
	for pin in led_pins:
		GPIO.output(pin, GPIO.HIGH)
		time.sleep(delay)

delay = 0.2
GPIO.setmode(GPIO.BCM)
led_pins = [0, 5, 6, 13, 19, 26, 12, 16]
sweep_leds(led_pins, delay)
toggle_leds(led_pins, GPIO.LOW)
time.sleep(delay)
toggle_leds(led_pins, GPIO.HIGH)
time.sleep(2 * delay)
toggle_leds(led_pins, GPIO.LOW)