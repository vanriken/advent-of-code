import logging
import numpy as np

logging.basicConfig(level=logging.DEBUG, 
	format='%(asctime)s - %(levelname)s: %(message)s')
logging.disable(logging.CRITICAL)

def get_input(filename):
	""" Reads the input and returns it a list of integers """

	with open(filename) as f:
		return [int(n) for n in f.readline().split()]

def repair_memory(banks):
	""" Executes the reallocation routine on the given memory banks.
		Returns the number of cycles needed for the reallocation.
		
		:param banks: a list of banks (each has a certain amount of blocks)
		:return cycle: the number of redistribution cycles to until loop is detected
		:return loop_length: the length of the detected loop
	"""
	cycle = 0
	loop_length = 0

	banks = np.array(banks)
	num_banks = len(banks)
	seen = {tuple(banks):cycle}
	
	while True:
		max_bank_idx = np.argmax(banks)
		num_blocks = banks[max_bank_idx]

		banks[max_bank_idx] = 0
		idx = max_bank_idx + 1

		for _ in range(num_blocks):
			banks[idx % num_banks] += 1
			idx += 1 
		cycle += 1

		# check if the current configuration has been seen before
		if tuple(banks) in seen.keys():
			length_loop = cycle - seen[tuple(banks)]
			break
		else:
			seen[tuple(banks)] = cycle
			
	return cycle, length_loop

def main():

	assert repair_memory([0,2,7,0])==(5,4), 'test input failed'

	banks = get_input('../input/input_day06.txt')
	cycle, length_loop = repair_memory(banks)
	print(f'Number of cycles until loop is detected: {cycle}')
	print(f'Length of the infinite loop: {length_loop}')

if __name__ == '__main__':
	main()