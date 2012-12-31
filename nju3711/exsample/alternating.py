#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep
import sys
sys.path.append('./..')
from nju3711 import NJU3711

#
# alternating
#
# 1. oxox oxox
# 2. xoxo xoxo
# 3. oxox oxox
# 4. xoxo xoxo
# ...
#

if __name__ == '__main__':

	nju = NJU3711()
	nju.reset()

	# alternating
	sts_pat1 = range(8)
	sts_pat2 = sts_pat1[:]
	for n in range(8):
		if n % 2 == 0:
			sts_pat1[n] = 0
			sts_pat2[n] = 1
		else:
			sts_pat1[n] = 1
			sts_pat2[n] = 0

	for i in range(32):
		nju.cmd(sts_pat1)
		sleep(0.5)
		nju.cmd(sts_pat2)
		sleep(0.5)

	nju.reset()

	print 'complete'

# vim: ts=4 sw=4 sts=4: 
