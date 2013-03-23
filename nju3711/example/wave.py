#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep
import sys
sys.path.append('./..')
from nju3711 import NJU3711

#
# wave from center to around
#
# 1. xxxx xxxx
# 2. xxxo oxxx
# 3. xxoo ooxx
# 4. xooo ooox
# 5. oooo oooo
# ...
#

if __name__ == '__main__':

	nju = NJU3711()
	nju.reset()

	# alternating
	sts_wave_array = [ '00000000', '00011000', '00111100', '01111110', '11111111']
	sts_wave = []

	for nwa in range(len(sts_wave_array)):
		wave = []
		wave_str = sts_wave_array[nwa]
		for nstr in range(8):
			wave.append(int(wave_str[nstr]))
		sts_wave.append(wave)

	for count in range(128):
		nju.cmd(sts_wave[count % 4])
		sleep(0.05)

	nju.reset()

	print 'complete'

# vim: ts=4 sw=4 sts=4: 
