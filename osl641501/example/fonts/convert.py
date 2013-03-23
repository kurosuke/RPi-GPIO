#!/usr/bin/python

import sys

print '# -*- coding: utf-8 -*-'
print 'codes = {'
data = u''
for line in sys.stdin:
	line = line[0:-1]
	items = line.split(' ')
	value = items[0]
	if value == 'STARTCHAR':
		code_char = items[1]
	if value == 'ENCODING':
		code = items[1]
		data = u''
	elif value == 'ENDCHAR':
		print '	%s: [ %s ],	# %s' % (code, data, code_char)
	elif value[0].isdigit() == True or value[0].islower() == True:
		data += ('0x' + value + ', ')
print '}'

# vim: ts=4 sw=4 sts=4: 

