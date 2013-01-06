#!/usr/bin/python

import RPi.GPIO as GPIO
import sys
import time

class MCP3002:

	def __init__(self, pin_clk=11, pin_mosi=10, pin_miso=9, pin_cs=18):
		# setup pins

		self.pin_clk = pin_clk
		self.pin_mosi = pin_mosi
		self.pin_miso = pin_miso
		self.pin_cs = pin_cs

		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.pin_clk, GPIO.OUT)
		GPIO.setup(self.pin_mosi, GPIO.OUT)
		GPIO.setup(self.pin_miso, GPIO.IN)
		GPIO.setup(self.pin_cs, GPIO.OUT)

	def __del__(self):
		GPIO.cleanup()

	def read_sensor(self, ch_no = 0):
		if (ch_no == 0):
			cmd = 0x6	# CH0
		else:
			cmd = 0x7	# CH1

		# init pins low
		GPIO.output(self.pin_clk, False)
		GPIO.output(self.pin_cs, False)

		# write first 3 bits to MOSI
		cmd <<= 5
		for bno in range(3):
			if (cmd & 0x80):
				GPIO.output(self.pin_mosi, True)
			else:
				GPIO.output(self.pin_mosi, False)
			cmd <<= 1
			GPIO.output(self.pin_clk, True)
			GPIO.output(self.pin_clk, False)

		# read 2(empty and null bit) + 10 ADC bits from MISO
		adc_result = 0
		for bit_no in range(12):
			GPIO.output(self.pin_clk, True)
			GPIO.output(self.pin_clk, False)
			adc_result <<= 1
			if (GPIO.input(self.pin_miso)):
				adc_result |= 0x1

		GPIO.output(self.pin_cs, True)

		adc_result /= 2    # first bit is 'null' so drop it
		return adc_result

if __name__ == '__main__':

	mcp = MCP3002()

	result = mcp.read_sensor(0)
	print 'result: %d' % (result)
	print 'complate'

# vim: ts=4 sw=4 sts=4: 
