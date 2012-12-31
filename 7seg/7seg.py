#
# 7seg print driver 
#
import time
import sys
import RPi.GPIO as GPIO


#
# 7seg led print driver
#
class Seg:
	"""
	7seg led class 
    .      a
	.    #####
    .   #     #
    . f #     # b
    .   #     #
	.    #####
    .   #  g  #
    . e #     # c
    .   #     #
	.    #####   # .
	.      d
	"""

	# gpio pins for seg parts
	pins = {}

	# GPIO pins for output
	io_pins = {
		# seg : gpio pin
		"a": 4,
		"b": 17,
		"c": 22,
		"d": 10,
		"e": 9,
		"f": 11,
		"g": 8,
		".": 7,
	}
	# charactor lists
	charactors = {
		# test pattern
		'a': [ 'a' ],
		'b': [ 'b' ],
		'c': [ 'c' ],
		'd': [ 'd' ],
		'e': [ 'e' ],
		'f': [ 'f' ],
		'g': [ 'g' ],

		# some parts of alphabet pattern
		'A': [ 'a', 'b', 'c', 'e', 'f', 'g'],
		'B': [ 'f', 'e', 'd', 'c', 'g'],
		'C': [ 'a', 'f', 'e', 'd'],
		'D': [ 'b', 'g', 'e', 'd', 'c'],
		'E': [ 'a', 'f', 'e', 'd', 'g'],
		'F': [ 'a', 'f', 'e', 'g'],

		'N': [ 'e', 'g', 'c'],
		'O': [ 'e', 'g', 'c', 'd'],

		# number pattern
		'1': [ 'b', 'c'],
		'2': [ 'a', 'b', 'g', 'e', 'd'],
		'3': [ 'a', 'b', 'g', 'c', 'd'],
		'4': [ 'f', 'g', 'b', 'c'],
		'5': [ 'a', 'f', 'g', 'c', 'd'],
		'6': [ 'a', 'f', 'e', 'd', 'c', 'g'],
		'7': [ 'a', 'b', 'c'],
		'8': [ 'a', 'b', 'c', 'd', 'e', 'f', 'g'],
		'9': [ 'a', 'b', 'c', 'd', 'f', 'g'],
		'0': [ 'a', 'b', 'c', 'd', 'e', 'f'],

		# dot pattern
		'.': [ '.'],
	}

	def __init__(self, pins):

		# set gpio pins for seg parts
		self.pins = pins

		#
		# GPIO setup
		#
		GPIO.setmode(GPIO.BCM)

		# for light
		for pno in list(self.io_pins.viewvalues()):
			GPIO.setup(pno, GPIO.OUT)

	def __del__(self):
		# GPIO cleanup
		GPIO.cleanup()

	# light charactor
	def put_char(self, char):
		# off all
		for pno in list(self.io_pins.viewvalues()):
			GPIO.output(pno, False)
		on_pins = self.charactors[char]
		time.sleep(.1)

		# on 
		for c in on_pins:
			GPIO.output(self.pins[c], True)

	# light string
	def light(self, string):
		for no in range(len(string)):
			self.put_char(string[no])
			time.sleep(1)

	# light testing
	def light_test(self):
		light_pattern = ( 'A', 'B', 'C', 'D', 'E', 'F',
			 '1', '2', '3', '4', '5', '6', '7', '8', '9', '.')

		for p in light_pattern:
			seg.put_char(p)
			time.sleep(.5)
		time.sleep(3)

# vim: ts=4 sw=4 sts=4:
