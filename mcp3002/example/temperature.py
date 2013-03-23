#!/usr/bin/python

import RPi.GPIO as GPIO
import sys
import time
sys.path.append('./..')
from mcp3002 import MCP3002


if __name__ == '__main__':

	mcp = MCP3002()

	try_gauge_num = 10	# check 10 times
	for i in range(30):
		total_result = 0
		for n in range(try_gauge_num):
			result = mcp.read_sensor(0)
			total_result += result

		# calc avarage
		avg_result = total_result /try_gauge_num

		# calc temperature
		volt = (avg_result/1024.0) *3.3		# 10bits A/D convert 3.3Vref
		temp = (volt / 5.96) * 100			# LM75D temperature is 1C / 10mA
		print 'adc_result: %d, voltage: %0f, temperature: %f' % (result, volt, temp)
		time.sleep(1)

	print 'complate'

# vim: ts=4 sw=4 sts=4: 
