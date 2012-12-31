#!/bin/sh

IPADDR=`/sbin/ifconfig eth0 | grep 'inet addr' | sed 's/.*inet addr:\([^ ]*\).*/\1/'`
sudo python 7seg_print.py $IPADDR
