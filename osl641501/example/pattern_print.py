#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep
import sys
sys.path.append('./../..')
from nju3711.nju3711 import NJU3711
from osl641501.osl641501 import OSL641501



#
#

if __name__ == '__main__':

	pat = [ '........', 
 			'.o......',
 			'..o.....',
 			'...o....',
 			'....o...',
 			'.....oo.',
 			'....o...',
 			'...o....', ]

	# for osl641501 pin 1-8
	nju1 = NJU3711(pin_clr=24, pin_stb=25, pin_clk=8, pin_data=7, DEBUG=0)

	# for osl641501 pin 9-16
	nju2 = NJU3711(pin_clr=22, pin_stb=10, pin_clk=9, pin_data=11, DEBUG=0)

	nju1.reset()
	nju2.reset()

	# matirx pattern to pin pattern
	mtx = OSL641501()


	mtx = OSL641501()

	mtx.set_pattern_char(pat)
	mtx.output_text()

	# dynamic light on
	pattern = mtx.get_matrix_pins_pattern()
	for n in range(24):
		for pat12 in pattern:
			pat1 = pat12[0:8]
			pat2 = pat12[8:16]
			nju1.cmd(pat1)
			nju2.cmd(pat2)

	nju1.reset()
	nju2.reset()

	print 'complete'

# vim: ts=4 sw=4 sts=4: 
