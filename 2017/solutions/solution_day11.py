import logging

logging.basicConfig(level=logging.DEBUG, 
	format='%(asctime)s - %(levelname)s: %(message)s')
#logging.disable(logging.CRITICAL)

def doubleheight_distance(pos1, pos2=[0,0]):

	""" 
	https://www.redblobgames.com/grids/hexagons/#distances-doubled
	""" 
	
	d_row = abs(pos1[0] - pos2[0])
	d_col = abs(pos1[1] - pos2[1])
	
	return d_row + max(0, (d_col - d_row)//2)


def walk_path(steps):

	"""
	used doubled coordinates for the hexagons (double height)
	the doubled coordinates double the vertical step size
	https://www.redblobgames.com/grids/hexagons/#coordinates-doubled
	"""

	pos = [0,0]
	max_distance = 0 

	for step in steps:
		if step == 'n':
			# double the vertical step size
			pos[1] += 2
		elif step == 'ne':
			pos[0] += 1
			pos[1] += 1
		elif step == 'se':
			pos[0] += 1
			pos[1] -= 1
		elif step == 's':
			# double the vertical step size
			pos[1] -= 2
		elif step == 'sw':
			pos[0] -= 1
			pos[1] -= 1
		elif step == 'nw':
			pos[0] -= 1
			pos[1] += 1
		else:
			raise Exception(f'"{step}" is an invalid step')

		distance = doubleheight_distance(pos)
		max_distance = max(max_distance, distance)

	return distance, max_distance


def main():
	
	# example input
	assert walk_path('ne,ne,ne'.split(','))[0] == 3
	assert walk_path('ne,ne,sw,sw'.split(','))[0] == 0
	assert walk_path('ne,ne,s,s'.split(','))[0] == 2
	assert walk_path('se,sw,se,sw,sw'.split(','))[0] == 3

	with open('../input/input_day11.txt') as f:
		steps = f.read().strip().split(',')

	distance, max_distance = walk_path(steps)
	print(f'Number of steps to reach the child process: {distance}.')
	print(f'Furthest away the child ever got: {max_distance} steps.')

if __name__ == '__main__':
	main()