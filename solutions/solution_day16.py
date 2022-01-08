import logging

logging.basicConfig(level=logging.INFO, 
	format='%(asctime)s - %(levelname)s: %(message)s')
#logging.disable(logging.CRITICAL)

class ProgramGroup():

	def __init__(self, number_of_programs):

		self.programs = [chr(ord('a')+i) for i in range(number_of_programs)]
		self.starting_order = ''.join(self.programs)

	def execute_dance_move(self, move):

		if move[0] == 's':

			# get the spint amount from the dance move
			spin = int(move[1:])
			logging.debug(f'Spin ({spin})')
			self.execute_spin(spin)

		elif move[0] == 'x':
			# get the indices of the programs that must change position
			idx1, idx2 = map(int, move[1:].split('/'))
			logging.debug(f'Exchange ({idx1},{idx2})')
			self.execute_exchange(idx1, idx2)

		elif move[0] == 'p':
			# get the names of the programs that must change position
			name1, name2 = move[1:].split('/')
			logging.debug(f'Partner ({name1},{name2})')
			self.execute_partner(name1, name2)
		else:
			raise Exception('Invalid dance move')

		logging.debug(self.programs)

	def execute_spin(self, spin):

		for i in range(spin):
			temp = self.programs[-1]
			self.programs[1:] = self.programs[0:-1]
			self.programs[0] = temp

	def execute_exchange(self, idx1, idx2):

		temp = self.programs[idx2]
		self.programs[idx2] = self.programs[idx1]
		self.programs[idx1] = temp

	def execute_partner(self, name1, name2): 

		idx1 = self.programs.index(name1)
		idx2 = self.programs.index(name2)
		self.execute_exchange(idx1, idx2)

def part1():

	with open('../input/input_day16.txt') as f:
		dance_moves = f.read().split(',')

	# test moves
	#dance_moves = ['s10', 'x10/9', 'x9/10', 'x10/11']
	
	number_of_programs = 16
	pg = ProgramGroup(number_of_programs)

	for move in dance_moves:
		pg.execute_dance_move(move)

	order = ''.join(pg.programs)

	print('The dance has been completed.')
	print(f'PART1: The final order is {order}.')

def part2():

	with open('../input/input_day16.txt') as f:
		dance_moves = f.read().split(',')

	# test dance moves
	# dance_moves = ['s1', 'x3/4', 'pe/b']

	number_of_programs = 16
	pg = ProgramGroup(number_of_programs)

	# number of dances that must be executed
	number_of_dances = 10**9

	# counter for the number of dances
	dance_counter = 0

	while True:

		dance_counter += 1

		# loop through the dance moves
		for move in dance_moves:
			pg.execute_dance_move(move)

		# check for a cycle
		if (''.join(pg.programs) == pg.starting_order):
			logging.info(f'Cycle detected after {dance_counter} dances.')
			cycle = dance_counter
			break

	for _ in range(number_of_dances % cycle):
		# loop through the dance moves
		for move in dance_moves:
			pg.execute_dance_move(move)

	order = ''.join(pg.programs)
	print('One billion dances have been completed.')
	print(f'PART2: The final order is {order}.')

if __name__ == '__main__':
	part1()
	part2()
	