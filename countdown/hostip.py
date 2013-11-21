#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import sys

def hostip(hostname):
    
	try:
		print socket.gethostbyname(hostname)
	except:
		print "0.0.0.0"


if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print "Usage: hostip.py hostname"
        sys.exit()

    hostname = sys.argv[1]
    hostip(hostname)

# vi:set ts=4 sw=4 sts=4 ft=python et:
