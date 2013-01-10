import time
import RPi.GPIO as GPIO
import sys

# GPIO setup
GPIO.setmode(GPIO.BCM)

# GPIO4(PIN7) setup for output
pins = [ 4, 17, 21, 22, 10, 9, 11, 14, 15, 18, 23, 24, 25, 8, 7]

# 1sec on and 0.5sec off 
for pin in pins:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, False)

# GPIO cleanup
GPIO.cleanup()


