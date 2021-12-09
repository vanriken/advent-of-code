import logging
import re
from collections import Counter

logging.basicConfig(level=logging.DEBUG, 
	format='%(asctime)s - %(levelname)s: %(message)s')
#logging.disable(logging.CRITICAL)

class Program():
	""" A class to model a program in the christmas computer. """

	def __init__(self, name, weight, children):
		""" Constructor for the class Program. """

		self.name = name 
		self.weight = weight
		self.children = children
		self.parent = None

	def __str__(self):
		""" Returns the string representation of a Program object. """

		s = f'Program(name={self.name},weight={self.weight},' 
		s += f'children={self.children},parent={self.parent})'
		return s

class ProgramCollection():
	""" A class to model a tree of programs in the christmas computers. """

	def __init__(self):
		""" Constructor for the class ProgramCollection. """
		self.programs = {}

	def fill_program_tree(self, data):
		""" Uses the data to fill the program tree with Program objects. """

		for match in data:
			name = match[1]
			weight = int(match[2])
			children = match[4].split(', ')
			children = list(filter(lambda x: x != '', children))
			self.programs[name] = Program(name, weight, children)

		for name in self.programs.keys():
			children = self.programs[name].children
			for child in children:
				self.programs[child].parent = name

	def get_root_program(self):
		""" Returns the name of the root program in the program tree. """

		for name in self.programs.keys():
			if self.programs[name].parent == None:
				return name
		return None

	def calculate_weight_subtower(self, name):
		""" Recursively calculates the weight of a subtower starting 
			at the program 'name'. 
		"""

		weight = self.programs[name].weight
		children = self.programs[name].children

		if children == []:
			return weight
		else:
			return weight + sum(
				[self.calculate_weight_subtower(child) for child in children]) 

	def is_program_balanced(self, name):
		""" Returns True if the disc of program 'name' is balanced. 
			Returns False if the the disc in not balanced.

			The disc of a program in the program tree is balanced if 
			the weights of all its subtrees are equal.
		"""

		children = self.programs[name].children
		subtower_weights = [
			self.calculate_weight_subtower(child) for child in children]

		if len(set(subtower_weights)) == 1:
			return True
		else:
			return False

	def locate_wrong_weight(self):
		""" Locates the program in the program tree whose weight must be 
			changed balance the program tree. Returns (name, delta_weight).
			
			:return name: 	The name of the program whose weight must be 
							changed to balance the program tree.
			:return name: 	The amount by which the weight of the program must
							be changed in order to balance the program tree.
		"""

		# start at the root of the program tree
		name = self.get_root_program()

		# get the children and the correspoding subtower weights
		children = self.programs[name].children
		subtower_weights = [
			self.calculate_weight_subtower(child) for child in children]
		delta = max(subtower_weights) - min(subtower_weights)

		# get the least common element in subtower weights and its index
		counter = Counter(subtower_weights)
		least_common_element = min(counter, key=counter.get)
		least_common_idx = subtower_weights.index(least_common_element)
		name = children[least_common_idx]

		# is the needed weight compensation positive or negative?
		if least_common_element == max(subtower_weights):
			weight_delta = -delta
		else:
			weight_delta = delta

		while True:

			# get the children and the correspoding subtower weights
			children = self.programs[name].children
			subtower_weights = [
				self.calculate_weight_subtower(child) for child in children]

			if self.is_program_balanced(name):
				# if the subtree starting from the current program is balanced
				# then the program tree can be balanced 
				# by changing the weight of the current program
				return(name, weight_delta)
			else:
				# else continue in the subtree that contains the wrong weight
				counter = Counter(subtower_weights)
				least_common_element = min(counter, key=counter.get)
				least_common_idx = subtower_weights.index(least_common_element)
				name = children[least_common_idx] # move to subtree

	def get_program_weight(self,name):
		""" Returns the weight of a program in the program tree """

		return self.programs[name].weight


def parse_text(text):
	""" Parses the input text using a regular expression and 
		captures the data in match groups. 
	"""

	towerProgramRegex = re.compile(r'''
	(					# group 0
	([a-z]+) 			# program name, group 1
	.\((\d*)\)			# weight, group 2	
	(.->.)?				# arrow, optional, group 3
	(.*)?				# children programs, group 4
	)
	''', re.VERBOSE)

	data = towerProgramRegex.findall(text)
	return data

def read_file(filepath):
	""" Reads a file and returns the contents as a string. """

	with open(filepath) as f:
		return f.read()

def main():

	test_input = """ 
	pbga (66)
	xhth (57)
	ebii (61)
	havc (66)
	ktlj (57)
	fwft (72) -> ktlj, cntj, xhth
	qoyq (66)
	padx (45) -> pbga, havc, qoyq
	tknk (41) -> ugml, padx, fwft
	jptl (61)
	ugml (68) -> gyxo, ebii, jptl
	gyxo (61)
	cntj (57)
	"""
	data = parse_text(read_file('../input/input_day07.txt'))
	#data = parse_text(test_input)
	program_tree = ProgramCollection()
	program_tree.fill_program_tree(data)
	root_program = program_tree.get_root_program()
	print(f'Name of root program: {root_program}.')

	name, delta = program_tree.locate_wrong_weight()
	current_weight = program_tree.get_program_weight(name)
	print(f'To balance the program tree, the weight of program "{name}"',
	 	f'must be changed from {current_weight} to {current_weight + delta}.')


if __name__ == '__main__':
	main()

