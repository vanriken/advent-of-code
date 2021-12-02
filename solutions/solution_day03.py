import itertools

class SpiralMemory():
	""" A class to model the spiral memory of the christmas computer """

	def __init__(self):
		self.xy = [0,0]
		self.direction = 'R'
		self.current_square = 1

		self.keep_direction = 1 # steps before changing direction
		self.direction_countdown = self.keep_direction

		# keys: coordinates, values: sum of adjacent squares
		self.values_dict = {(0,0) : 1}

	def take_step(self):
		""" Takes a step in the spiral in a given direction """

		# take a step in the given direction
		if self.direction == 'R':
			self.xy[0] += 1
		elif self.direction == 'U':
			self.xy[1] += 1
		elif self.direction == 'L':
			self.xy[0] -= 1
		elif self.direction == 'D':
			self.xy[1] -= 1
		else:
			print("take step: something went wrong.")

		self.current_square += 1
		self.direction_countdown -= 1

		# check if the direction has to change for the next step
		if self.direction_countdown == 0:
			self.change_direction()

	def change_direction(self):
		""" Changes the direction in which we walk through the spiral """

		if self.direction 	== 	'R':
			self.direction 	= 'U'
		elif self.direction == 	'U':
			self.direction 	= 'L'
		elif self.direction == 	'L':
			self.direction 	= 'D'
		elif self.direction == 	'D':
			self.direction 	= 'R'
		else:
			print("change_direction: something went wrong.")

		# check if the keep_direction has to be incremented
		if self.direction in ['L','R']:
			self.keep_direction += 1
		self.direction_countdown = self.keep_direction

	def get_manhattan_distance(self):
		""" Returns manhattan distance from point (x,y) to the point (0,0) """
		
		return abs(self.xy[0]) + abs(self.xy[1])

	def calculate_value(self):
		""" Calculates the value of a square in the spiral memory 

			The value of a square is equal to the sum of the values in 
			all adjacent squares,including the diagonals.
		"""

		value = 0;
		x,y = self.xy

		for dx,dy in itertools.product([-1,0,1], repeat=2):
			if dx == 0 and dy == 0:
				pass
			else:
				value += self.values_dict.get((x+dx, y+dy), 0)

		return value


	def travel_to_square(self, destination_square, compute_values = False, 
						 stop_value = 0):
		""" Follow the spiral to move to a certain destination square """
		while True:
			if self.current_square == destination_square:
				print("Destination square has been reached")
				break
			else: 
				self.take_step()

				if compute_values == True:
					value = self.calculate_value()
					self.values_dict[tuple(self.xy)] = value
					if value > stop_value:
						break

# PART 1
spiral_memory = SpiralMemory()
spiral_memory.travel_to_square(265149)
print("PART1: Number of steps required to carry the data to access port:", 
	  		f"{spiral_memory.get_manhattan_distance()} steps" )

# PART 2
spiral_memory.__init__()
spiral_memory.travel_to_square(destination_square = 100, compute_values = True, 
							   stop_value = 265149)
values = spiral_memory.values_dict.values()
print(f"PART2: First value larger than stop_value: {sorted(values)[-1]}")
