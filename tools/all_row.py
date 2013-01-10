import RPi.GPIO as GPIO

# GPIO setup
GPIO.setmode(GPIO.BCM)

# all GPIO pins list
pins = [ 4, 17, 21, 22, 10, 9, 11, 14, 15, 18, 23, 24, 25, 8, 7]

for pin in pins:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, False)

# GPIO cleanup
GPIO.cleanup()


