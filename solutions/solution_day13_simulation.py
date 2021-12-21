import logging

logging.basicConfig(level=logging.DEBUG, 
	format='%(asctime)s - %(levelname)s: %(message)s')
#logging.disable(logging.CRITICAL)

class Firewall():
	''' A class to model the firewall in a computer that was built by elves. '''

	def __init__(self):

		self.firewall_dict = dict()
		self.packet_position = -1 
		self.alarm_triggered = False

	def reset_state(self):
		""" Resets the state of the firewall to the initial state """

		self.packet_position = -1 
		self.alarm_triggered = False
		for key in self.firewall_dict.keys():
			self.firewall_dict[key].scanner_position = 1
			self.firewall_dict[key].scanner_direction = 'DOWN'

	def read_data(self, data):

		data = data.strip().split('\n')
		for row in data:
			layer_depth, layer_range = map(int, row.split(': '))
			self.firewall_dict[layer_depth] = FirewallLayer(layer_depth, layer_range)

	def move_scanners(self):

		for key in self.firewall_dict.keys():
			self.firewall_dict[key].move_scanner()

	def calc_severity(self):

		try:
			# caught by the firewall
			if self.firewall_dict[self.packet_position].scanner_position == 1:
				layer_depth = self.firewall_dict[self.packet_position].layer_depth 
				layer_range = self.firewall_dict[self.packet_position].layer_range
				severity = layer_range * layer_depth
				self.alarm_triggered = True
				return severity
		except:
				pass
		return 0


	def move_through_fw(self, delay=0, break_when_detected=False):

		max_depth = max(self.firewall_dict.keys())
		severity = 0

		# PROBLEM: this for loop slows down the program considerably
		for i in range(delay):
			self.move_scanners()

		while self.packet_position < max_depth:
			self.packet_position += 1
			severity += self.calc_severity()
			self.move_scanners()
			
			if (break_when_detected == True) and (self.alarm_triggered == True):
				break

		return severity

class FirewallLayer():
	''' A class to model a single layer of the firewall of the elves computer. '''

	def __init__(self, layer_depth, layer_range):

		self.layer_depth = layer_depth
		self.layer_range = layer_range
		self.scanner_position = 1
		self.scanner_direction = 'DOWN'

	def __repr__(self):

		string = f'(depth:{self.layer_depth}, range:{self.layer_range}, '
		string += f'scanner_position:{self.scanner_position})'
		return string

	def move_scanner(self):
		
		# move the scanner of the current layer one position
		if self.scanner_direction == 'DOWN':
			self.scanner_position += 1
		elif self.scanner_direction == 'UP':
			self.scanner_position -= 1
		else:
			raise Exception('scanner_direction is invalid.')

		# reverse the direction if the scanner has reached the end/beginning
		if self.scanner_position == 1:
			self.scanner_direction = 'DOWN'
		elif self.scanner_position == self.layer_range:
			self.scanner_direction = 'UP'

def main():
	
	test_data = "0: 3\n1: 2\n4: 4\n6: 4"
	with open('../input/input_day13.txt') as f:
		puzzle_data = f.read()

	# select test_data or puzzle_data
	data = test_data
	
	fw = Firewall()
	fw.read_data(data)
	
	# part 1
	start_delay = 0
	severity = fw.move_through_fw(delay=start_delay)
	print(f'Starting immediately: Severity={severity}, Alarm={fw.alarm_triggered}.')

	# part 2 - too slow if the trip through the firewall is simulated
	while fw.alarm_triggered == True:
		start_delay += 1
		fw.reset_state()
		severity = fw.move_through_fw(
			delay=start_delay, break_when_detected=True)
		if start_delay % 1000 == 0:
			logging.debug(f'Wait {start_delay} picoseconds: Severity={severity}, Alarm={fw.alarm_triggered}.')

	print(f'Wait {start_delay} picoseconds before starting: Severity={severity}, Alarm={fw.alarm_triggered}.')

if __name__ == '__main__':
	main()
