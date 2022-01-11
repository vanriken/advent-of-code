import logging

logging.basicConfig(level=logging.DEBUG, 
	format='%(asctime)s - %(levelname)s: %(message)s')
logging.disable(logging.CRITICAL)

def part1():

	max_val = 2017
	circ_buffer = [0]
		
	current_pos = 0
	step = 335
	
	for i in range(1,max_val+1):

		# spinlock steps forward
		length = i
		current_pos = (current_pos + step) % length
		
		# insert the next value after current position
		current_pos += 1
		circ_buffer.insert(current_pos, i)

	target = 2017
	target_idx = circ_buffer.index(target)

	print(f'PART1: The value after {target} is {circ_buffer[target_idx+1]}.')
	
def part2():

	''' 
	The key observation for solving part 2:

	Since the value zero is always at the front (at position 0) we just have to keep track 
	of when a value is added directly after zero. There is no need to generate the buffer.

	'''

	max_val = 50 * 10**6
	current_pos = 0
	step = 335

	val_after_zero = -1

	for i in range(1,max_val + 1):

		# spinlock steps forward
		length = i
		current_pos = (current_pos + step) % length

		# new value is inserted after current position
		current_pos += 1

		# check if the next value is inserted directly after zero
		if current_pos == 1:
			val_after_zero = i

		if i % (5 * 10**6) == 0:
			logging.debug(f'progress: {i//10**6} / {max_val//10**6} (in millions).')
		
		
	print(f'PART2: The value after 0 is {val_after_zero}')



if __name__ == '__main__':
	part1()
	part2()