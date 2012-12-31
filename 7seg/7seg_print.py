#
# 7seg print driver 
#
import time
import sys
import RPi.GPIO as GPIO
import 7seg

# GPIO pin for input
io_input = 25

def loop:
	# for scan switch
	GPIO.setup(io_input, GPIO.IN)

	# default status switch off(False)
	cur_status = False

	# push counter
	push_count = 0

	# scan GPIO and lighting string
	while (push_count < 20):
		status = GPIO.input(io_input)

		# check change status
		if cur_status != status:
			if status == True:
				print 'switch on'
				push_count = push_count + 1
			else:
				print str
				seg.light(str)
				seg.light('..')
			cur_status = status
		time.sleep(1)

if __name__ == '__main__':

	seg = Seg(io_pins)

	argvs = sys.argv
	str = ""
	if len(argvs) > 1:
		str = argvs[1]
	else:
		str = 'NONE.'
	
	# light test
	seg.light_test()
	
	# push switch and show string
	loop(seg)

# vim: ts=4 sw=4 sts=4:
