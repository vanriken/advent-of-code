import logging

logging.basicConfig(level=logging.DEBUG, 
	format='%(asctime)s - %(levelname)s: %(message)s')
#logging.disable(logging.CRITICAL)

def print_diagram(diagram, pos=None):
	''' Prints the diagram as a multiline string.
		When a 'pos' argument is given with the current position, 
		then the current position is marked with an 'x' on the diagram.
	'''

	if pos == None:
		for row in diagram:
			print(''.join(row))		
	else:
		# copying of a nested list, we do not want to modify the original
		temp = [row[:] for row in diagram]
		temp[pos[0]][pos[1]] = 'X'
		for row in temp:
			print(''.join(row))
	
	print('\n')

def check_step(diagram, pos, direction):
	''' Checks if a step can be taken in the given direction.
		Returns True if the step can be taken, False otherwise. 
	'''
	n_rows = len(diagram)
	n_cols = len(diagram[0])

	# check whether we are at the edge of the diagram
	# we are not allowed to step further then
	if pos[0] == n_rows-1 and  direction == 'down':
		return False
	elif pos[0] == 0 and direction == 'up':
		return False
	elif pos[1] == n_cols-1 and direction == 'right':
		return False
	elif pos[1] == 0 and direction == 'left':
		return False

	if direction == 'down':
		target = diagram[pos[0]+1][pos[1]]
	elif direction == 'right':
		target = diagram[pos[0]][pos[1]+1]
	elif direction == 'up':
		target = diagram[pos[0]-1][pos[1]]
	elif direction == 'left':
		target = diagram[pos[0]][pos[1]-1]
	else:
		raise Exception('invalid direction')

	if target == ' ':
		return False

	return True 

def take_step(pos, direction):
	''' Takes a step in the given direction and updates the position accordingly '''

	if direction == 'down':
		pos[0]+=1
	elif direction == 'right':
		pos[1]+=1
	elif direction == 'up':
		pos[0]-=1
	elif direction == 'left':
		pos[1]-=1
	return pos

def update_direction(diagram, pos, direction):

	end_reached = False 

	# current direction is 'up' or 'down'
	if direction in ['up','down']:
		if check_step(diagram, pos, direction) == True:
			pass
		elif check_step(diagram, pos, 'right') == True:
			direction = 'right'
		elif check_step(diagram, pos, 'left') == True:
			direction = 'left'
		else:
			# no steps are possible, end reached
			end_reached = True

	# current direction is 'left' or 'right'
	elif direction in ['left','right']:
		if check_step(diagram, pos, direction) == True:
			pass 
		elif check_step(diagram, pos, 'up') == True:
			direction = 'up'
		elif check_step(diagram, pos, 'down') == True:
			direction = 'down'
		else:
			# no steps are possible, end reached
			end_reached = True

	return direction, end_reached

def main():

	diagram = []
	letters_seen = []

	with open('../input/input_day19.txt') as f:
		for row in f.read().split('\n'):
			diagram.append(list(row))

	# go to the starting position
	pos = [0, diagram[0].index('|')]
	direction = 'down'
	n_steps = 1

	while True:
		
		pos = take_step(pos, direction)
		n_steps += 1

		# check if current position is a letter, if so add it to letters_seen
		if diagram[pos[0]][pos[1]].isalpha() == True:
			letters_seen.append(diagram[pos[0]][pos[1]])

		# update direction of movement
		# detect if end has been reached
		direction, end_reached = update_direction(diagram, pos[:], direction)

		if end_reached == True:
			print('The end has been reached.')
			break

	# print the encountered letters as a string
	letters_seen = ''.join(letters_seen)
	print(f'The little packet will see the following letters on its journey: {letters_seen}.')
	print(f'Number of steps: {n_steps}')

if __name__ == '__main__':
	main()