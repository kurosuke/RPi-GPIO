#!/usr/bin/python
#
# 8 x 8 matrix
#
import time

DEBUG=0

class OSL641501:
	# matrix size
	nrow = 8
	ncol = 8

	# anode (col)
	anodes = [ 13, 3, 4, 10, 6, 11, 15, 16 ]

	# cathode (row)
	cathodes = [ 9, 14, 8, 12, 1, 7, 2, 5 ]

	# matrix led status
	matrix = []

	# pins status
	pins_status = {}

	def __init__(self):
		# all matrix is off
		self.matrix = [['.' for j in range(self.ncol)] for i in range(self.nrow)]

		# set anodes LOW
		for col in range(self.ncol):
			# check anodes pin status
			anode_pin_no = self.anodes[col]
			self.pins_status[anode_pin_no] = 'L'

		# set cathode HI
		for row in range(self.nrow):
			# check cathode pin status
			cathode_pin_no = self.cathodes[row]
			self.pins_status[cathode_pin_no] = 'H'
		
	# change pin HI/LOW status
	def change_pin(self, pin_no, status):
		self.pins_status[pin_no] = status

		for col in range(self.ncol):
			# check anodes pin status
			anode_pin_no = self.anodes[col]
				
			for row in range(self.nrow):
				# check cathodes pin status
				cathode_pin_no = self.cathodes[row]
				if self.pins_status[anode_pin_no] == 'H' and self.pins_status[cathode_pin_no] == 'L':
					self.matrix[col][row] = 'o'
				else:
					self.matrix[col][row] = 'o'
		
	# set matrix pattern (by char .:off o:on array)
	def set_pattern_char(self, pattern):
		for row in range(self.nrow):
			line = pattern[row]
			for col in range(self.ncol):
				self.matrix[col][row] = line[col]

	# set matrix pattern (by hex array)
	def set_pattern_hex(self, pattern):
		for row in range(self.nrow):
			hex_value = pattern[row]
			for col in range(self.ncol):
				if hex_value & 0x80 > 0:
					self.matrix[col][row] = 'o'
				else:
					self.matrix[col][row] = '.'
				hex_value = hex_value <<1

	# get matrix pattern
	def get_matrix_pins_pattern(self):
		matrix_size = 8

		pins_pattern = matrix_size*matrix_size*[0]
		for row in range(matrix_size):
			for col in range(matrix_size):
				# get matrix dot status
				status = self.matrix[col][row] 

				# set each pins status 
				matrix_pins = range(matrix_size*2)
				for n in range(len(self.anodes)):
					anode_pin_no = self.anodes[n]
					if status == 'o' and col == n:
						matrix_pins[anode_pin_no-1] = True
					else:
						matrix_pins[anode_pin_no-1] = False
				for n in range(len(self.cathodes)):
					cathode_pin_no = self.cathodes[n]
					if status == 'o' and row == n:
						matrix_pins[cathode_pin_no-1] = False
					else:
						matrix_pins[cathode_pin_no-1] = True
				if DEBUG == 1:
					print '(%d, %d) %s' % (row, col, status)
					print matrix_pins
				pins_pattern[row*matrix_size + col] = matrix_pins
		return pins_pattern		
		

	#
	# for debug
	#

	# output matrix on/off image by text 
	def output_text(self):
		for row in range(self.nrow):
			line = ''
			for col in range(self.ncol):
				line = line + self.matrix[col][row]
			print line.replace('.', ' ')
		print '--------'

	# output each pins status
	def output_pins_status(self):
		print ' - anode -'
		for n in range(len(self.anodes)):
			pin_no = self.anodes[n]
			print '%02d pin is %s' % (pin_no, self.pins_status[pin_no])
		print ' - cathode -'
		for n in range(len(self.cathodes)):
			pin_no = self.cathodes[n]
			print '%2d pin is %s' % (pin_no, self.pins_status[pin_no])
				
if __name__ == '__main__':

	mtx = OSL641501()
	mtx.change_pin(13, 1)
	mtx.change_pin(3, 1)
	mtx.change_pin(9, 0)
	mtx.change_pin(15, 1)
	mtx.change_pin(1, 0)

	mtx.output_pins_status()

	print 'complate'


# vim: ts=4 sw=4 sts=4: 

