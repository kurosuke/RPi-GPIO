#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep
import sys

class NJU3711:

	def __init__(self, pin_clk=10, pin_stb=9, pin_clr=11, pin_data=4, DEBUG=0, output_pin_num=8):
		self.DEBUG = DEBUG
		self.output_pin_num = output_pin_num

		# setup pins
		self.pin_clk = pin_clk
		self.pin_stb = pin_stb
		self.pin_clr = pin_clr
		self.pin_data = pin_data

		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.pin_clk, GPIO.OUT)
		GPIO.setup(self.pin_stb, GPIO.OUT)
		GPIO.setup(self.pin_clr, GPIO.OUT)
		GPIO.setup(self.pin_data, GPIO.OUT)

	def __del__(self):
		GPIO.cleanup()

	def reset(self):
		# reset
		GPIO.output(self.pin_clr, True)

		GPIO.output(self.pin_stb, True)
		GPIO.output(self.pin_data, False)
		GPIO.output(self.pin_clk, False)
		sleep(0.001)

		for no in range(self.output_pin_num):
			GPIO.output(self.pin_clk, True)
			GPIO.output(self.pin_clk, False)

		GPIO.output(self.pin_stb, False)
		GPIO.output(self.pin_stb, True)

	def cmd(self, pin_sts):

		# send data
		GPIO.output(self.pin_stb, True)
		if self.DEBUG:
			print pin_sts
		for no in range(self.output_pin_num):
			# set data bit
			GPIO.output(self.pin_data, pin_sts[self.output_pin_num-no-1])

			# clock
			GPIO.output(self.pin_clk, True)
			GPIO.output(self.pin_clk, False)

		# send ratch
		GPIO.output(self.pin_stb, False)
		GPIO.output(self.pin_stb, True)
		
	def demo(self):

		# light on sequence and speed up
		sts_off = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
		for i in range(64):
			sts_cur = sts_off[:]
			sts_cur[7 - (i%8)] = 1
			print 'loop ' + `i`
			nju.cmd(sts_cur)
			sleep(1.0-(i%8)*0.1)

		nju.reset()

if __name__ == '__main__':

	nju = NJU3711()
	nju.reset()

	nju.demo()

	print 'complate'

# vim: ts=4 sw=4 sts=4: 
