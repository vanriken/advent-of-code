import logging
from collections import defaultdict
import re

logging.basicConfig(level=logging.DEBUG, 
	format='%(asctime)s - %(levelname)s: %(message)s')
#logging.disable(logging.CRITICAL)

test_input = '''
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
'''
test_input = test_input.strip().split('\n')

def evaluate_condition(comp_register, comp_operator, comp_value, register_dict):
	""" Evaluates the condition of an instruction and returns True or False """

	if comp_operator == '>':
		return register_dict[comp_register] > comp_value
	elif comp_operator == '>=':
		return register_dict[comp_register] >= comp_value
	elif comp_operator == '<':
		return register_dict[comp_register] < comp_value
	elif comp_operator == '<=':
		return register_dict[comp_register] <= comp_value
	elif comp_operator == '==':
		return register_dict[comp_register] == comp_value
	elif comp_operator == '!=':
		return register_dict[comp_register] != comp_value
	else:
		raise Exception(f'"{comp_operator}" is an invalid comparison operator.')

def execute_instruction(register, operation, value, register_dict):
	""" Executes the instruction by increasing/decreasing the value the register """

	if operation == 'inc':
		register_dict[register] += value 
	elif operation == 'dec':
		register_dict[register] -= value
	else:
		raise Exception(f'{operation} is not a valid register operation.') 

def get_puzzle_input(filepath):
	""" Read the puzzle input and return it """

	with open(filepath) as f:
		return f.read().split('\n')

def main():
	# registers start at zero
	register_dict = defaultdict(lambda:0)

	'''
		group1: register
		group2: inc/dec
		group3: value
		group4: comp_register
		group5: comp_operator
		group6: comp_value
	'''
	instructionRegex = re.compile(r'(\w+) (inc|dec) (-?\d+) if (\w+) (.{1,2}) (-?\d+)')
	
	instruction_list = test_input
	instruction_list = get_puzzle_input('../input/input_day08.txt')
	
	highest_ever = 0

	for instruction in instruction_list:
		mo = instructionRegex.search(instruction)
		register = mo.group(1)
		operation = mo.group(2)
		value = int(mo.group(3))
		comp_register = mo.group(4)
		comp_operator = mo.group(5)
		comp_value = int(mo.group(6))

		# check if the condition in the instruction is true
		if evaluate_condition(comp_register, comp_operator, comp_value,register_dict) == True:
			execute_instruction(register, operation, value, register_dict)
			# check for new highest value
			highest = max(register_dict.values())
			if highest_ever < highest:
				highest_ever = highest
			else:
				pass

	# get the largest value inside a register 
	print(f'The largest value in any register is {max(register_dict.values())}.')
	print(f'The highest value held in any register during the process was {highest_ever}.')


if __name__ == '__main__':
	main()
	