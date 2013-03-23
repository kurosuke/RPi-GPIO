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

	matrix_size = 8
	font_width = 4

	str_len = len(str)
	matrix_width = (font_width * str_len)

	matrixes = matrix_size*['']
	for char_no in range(str_len):
		char_code = ord(str[char_no])
		hex_pattern = font.codes[char_code]
		for n in range(len(hex_pattern)):
			bits_str = format(hex_pattern[n]>>4, '04b')
			bits_str = bits_str.replace('0', '.').replace('1', 'o')
			matrixes[n] += bits_str

	print '\n'.join(matrixes).replace('.', ' ')
	pattern = matrix_size*['']
	for i in range(len(matrixes[0])-matrix_size):
		for row_no in range(matrix_size):
			pattern[row_no] = matrixes[row_no][i:i+matrix_size]
		mtx.set_pattern_char(pattern)
		mtx.output_text()
		
		pattern = mtx.get_matrix_pins_pattern()
	
		# dynamic light on 
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
