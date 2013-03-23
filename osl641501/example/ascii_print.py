#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep
import sys
sys.path.append('./../..')
from nju3711.nju3711 import NJU3711
from osl641501.osl641501 import OSL641501

sys.path.append('./fonts')
import atari_small as font


# ascii string output
def ascii_print (str):

	# for osl641501 pin 1-8
	nju1 = NJU3711(pin_clr=24, pin_stb=25, pin_clk=8, pin_data=7, DEBUG=0)

	# for osl641501 pin 9-16
	nju2 = NJU3711(pin_clr=22, pin_stb=10, pin_clk=9, pin_data=11, DEBUG=0)

	nju1.reset()
	nju2.reset()

	# matirx pattern to pin pattern
	mtx = OSL641501()

	str_len = len(str)
	for i in [x for x in range(str_len) if x % 2 == 0]:
		# make ascii str charactor
		char_code = ord(str[i])
		pattern = font.codes[char_code]
		if i < str_len-1:
			# second char
			char_code = ord(str[i+1])
			pre_shift_pattern = font.codes[char_code]
			for n in range(len(pattern)):
				pattern[n] |= (pre_shift_pattern[n]>>4)
		mtx.set_pattern_hex(pattern)
		mtx.output_text()

		# dynamic light on 
		pattern = mtx.get_matrix_pins_pattern()
		for n in range(24):
			for pat12 in pattern:
				pat1 = pat12[0:8]
				pat2 = pat12[8:16]
				nju1.cmd(pat1)
				nju2.cmd(pat2)
	print 'complete'

	nju1.reset()
	nju2.reset()


#
# test light on osl641501 operated by nju3711
# 

if __name__ == '__main__':

	str = u'hellow world.'
	argvs = sys.argv
	if len(argvs) > 1:
		str = argvs[1]

	ascii_print(str)

	print 'complete'


# vim: ts=4 sw=4 sts=4: 
