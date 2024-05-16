import logging
import numpy as np

logging.basicConfig(level=logging.DEBUG, 
	format='%(asctime)s - %(levelname)s: %(message)s')

# comment the next line to enable logging
logging.disable(logging.CRITICAL)

def get_input(filepath):
	""" Reads the input from a file and stores it in a numpy array
		
		:param filepath: the path of the file that contains the input
		:return instructions: a numpy array containing the offsets for each jump  
	"""
	with open(filepath) as f:
		instructions = [int(number) for number in f]

	return instructions
	

def exit_instructions_maze(instructions, complex_rule=False):
	""" Interpret the instructions contained in 'instructions' and exit the
		maze of instructions.

		There are two rules for the jumps, normal and complex. 
		See the implementation for details.

		:param instruction: a list containing the offsets for each jump
		:param complex_rule: when it is True, the function uses the complex rule
		:return steps: the number of steps it takes to reach the exit
	"""
	
	idx = 0
	steps = 0
	instructions = np.array(instructions) # np.array is faster
	length = len(instructions)

	while idx < length and idx >= 0:
		
		jump = instructions[idx]
		logging.debug(f"index: {idx}")
		logging.debug(f"jump: {jump}")

		if complex_rule == True:
			if jump >= 3:
				instructions[idx] -= 1
			else: 
				instructions[idx] += 1
		else:
			instructions[idx] += 1

		# jump to the next index, count this jump
		idx += jump
		steps += 1

	return steps

def main():

	choice = 'P2' # {'P1', 'P2'}

	print(f'Running part {choice[-1]}')

	# test input part1
	assert exit_instructions_maze([0,3,0,1,-3]) == 5, 'Test input failed'
	# test input part2
	assert exit_instructions_maze([0,3,0,1,-3], True) == 10, 'Test input failed'

	# get the input
	instructions = get_input('../input/input_day05.txt')

	if choice == 'P1':
		steps = exit_instructions_maze(instructions)
	else: 
		steps = exit_instructions_maze(instructions, complex_rule=True)

	print(f"Part {choice[-1]}: {steps} steps to reach the exit")

if __name__ == '__main__':
	main()