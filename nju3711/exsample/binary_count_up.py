#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep
import sys
sys.path.append('./..')
from nju3711 import NJU3711

#
# binary count up 
#
# 1. oxxx xxxx
# 2. xoxx xxxx
# 3. ooxx xxxx
# 4. xxox xxxx
# ...
# 254. xooo oooo
# 255. oooo oooo
#

if __name__ == '__main__':

	nju = NJU3711()
	nju.reset()

	# binary count up 1 to 255
	for n in range(255):
		sts_bin_str = list(format(n, 'b').zfill(8))
		sts_cur = []
		for x in range(8):
			sts_cur.append(int(sts_bin_str[x]))
		nju.cmd(sts_cur)
		sleep(0.5)

	nju.reset()

	print 'complete'

# vim: ts=4 sw=4 sts=4: 
