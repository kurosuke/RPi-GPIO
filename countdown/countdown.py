#!/usr/bin/python

import RPi.GPIO as GPIO

from hd44780 import HD44780
from datetime import datetime
from time import sleep
import socket

if __name__ == '__main__':
    # init LCD
    lcd = HD44780(24, 23, [22, 10, 9, 11])

    # countdown each 0.05sec
    fact = 0.05
    range_max = int(10/fact)

    # GPIO setup for input
    GPIO.setup(4, GPIO.IN)
    GPIO.setup(17, GPIO.IN)

    # first display host ip
    is_reset = False
    ip = socket.gethostbyname('rpi.local')
    lcd.message(" IP\n " + ip)

    # main loop
    while True:

        # GPIO17 on is game start
        while True:
            sleep(fact)
            if GPIO.input(17) == True:
                break

        # count down 
        is_stop = 0
        for i in range(0, range_max):
            lcd.clear()
            msec = float((range_max-i) * fact)
            bar_size = int((msec % 1) * 10)
            lcd.message(" push yellow \n %.2f %s" % (msec, '.' * bar_size) )
            sleep(fact)
        
            if GPIO.input(4) == True:
                # GPIO4 on is stop
                lcd.clear()
                lcd.message(" STOP %0.2f \n push green" % (msec));
                is_stop = 1
                break
                
        if is_stop == 0:
            # counter over 0
            lcd.clear()
            lcd.message(" LOSE \n push green");
        
# vi:set ts=4 sw=4 sts=4 ft=python et:
