#!/usr/bin/python

import RPi.GPIO as GPIO
import sys
import time
sys.path.append('./..')
from mcp3002 import MCP3002


if __name__ == '__main__':

	mcp = MCP3002()

	for i in range(32):
		result = mcp.read_sensor(1)
		volt = (result/1024.0)*3.3
		lux = volt * 1000
		print 'adc_result: %d, voltage: %0f, lux: %d' % (result, volt, lux)
		time.sleep(1)

	print 'complate'

# vim: ts=4 sw=4 sts=4: 
