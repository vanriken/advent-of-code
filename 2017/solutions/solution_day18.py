import logging
import re 
from collections import defaultdict
from queue import Queue
from threading import Thread

logging.basicConfig(level=logging.INFO, 
	format='%(asctime)s - %(levelname)s: %(message)s')
#logging.disable(logging.CRITICAL)


def read_input(filepath):

	with open(filepath) as f:
		data = f.read().strip()
	return data 

def parse_input(data):

	# create a regex object
	# group1: instruction, group2: arg1, group3: arg2 (optional)
	instructionRegex = re.compile(r'(\w{3}) (\w) ?(.+)?')
	
	instructions = instructionRegex.findall(data)
	return instructions

def get_value(arg, registers):
	''' 
	Returns the value of the argument of an instruction. 
	Many of the instructions can take either a register (letter) 
	or a number as an argument.
	'''

	try:
		val = int(arg)
	except ValueError:
		val = registers[arg]
	return val

def part1():
	
	data = read_input('../input/input_day18.txt')
	instructions = parse_input(data)
	register_values = defaultdict(lambda: 0)
	freq_last_sound = defaultdict(lambda: 0)

	idx = 0
	n = len(instructions)

	while (idx >= 0) and (idx < n):	
		
		# fetch the next instruction
		next_instruction = instructions[idx]

		# get the instruction type and the arguments
		ins_type = next_instruction[0]
		arg1 = next_instruction[1]
		arg2 = next_instruction[2]

		# execute the instruction
		# many of the instructions can take either a register or a number
		if ins_type == 'snd':
			logging.debug(f'snd {arg1}: a sound is played with freq {register_values[arg1]}')
			freq_last_sound[arg1] = register_values[arg1]		
		
		elif ins_type == 'set':
			register_values[arg1] = get_value(arg2, register_values)
		
		elif ins_type == 'add':
			register_values[arg1] += get_value(arg2, register_values)
		
		elif ins_type == 'mul': 
			register_values[arg1] *= get_value(arg2, register_values)
		
		elif ins_type == 'mod':
			register_values[arg1] %= get_value(arg2, register_values)
		
		elif ins_type == 'rcv':
			if freq_last_sound[arg1] > 0:
				logging.debug(f'rcv {arg1}: value of recovered freq is {freq_last_sound[arg1]}')
				value_recovered = freq_last_sound[arg1]
				break;
			else:
				pass

		elif ins_type == 'jgz':
			if get_value(arg1, register_values) > 0:
				# minus one because at the end of the while loop idx is incremented by one
				idx += get_value(arg2, register_values)-1
			else:
				pass

		else:
			raise Exception(f'"{ins_type}" is an invalid instruction.')

		idx += 1

	print(f'Part1: The value of the recovered frequency is {value_recovered}.')


def run_program(snd, rcv, program_id, instructions):

	register_values = defaultdict(lambda:0)
	register_values['p'] = program_id

	idx = 0
	sent = 0
	received = 0

	while (idx >= 0) and (idx < len(instructions)):	
		
		# fetch the next instruction
		next_instruction = instructions[idx]

		# get the instruction type and the arguments
		ins_type = next_instruction[0]
		arg1 = next_instruction[1]
		arg2 = next_instruction[2]

		# execute the instruction
		# many of the instructions can take either a register or a number
		if ins_type == 'snd':
			logging.debug(f'Program ID {program_id}: "snd" value {get_value(arg1, register_values)}')
			snd.put(get_value(arg1, register_values))
			sent += 1
			if program_id == 1:
				logging.info(f'Program ID {program_id}: number of values sent {sent}')

		elif ins_type == 'set':
			register_values[arg1] = get_value(arg2, register_values)
		
		elif ins_type == 'add':
			register_values[arg1] += get_value(arg2, register_values)
		
		elif ins_type == 'mul': 
			register_values[arg1] *= get_value(arg2, register_values)
		
		elif ins_type == 'mod':
			register_values[arg1] %= get_value(arg2, register_values)
		
		elif ins_type == 'rcv':
			logging.debug(f'Program ID {program_id}: "rcv" size queue {rcv.qsize()}')
			# block if necessary until an item is available in the queue
			# blocks for timeout seconds and raises the Empty exception is no item is available within that time
			register_values[arg1] = rcv.get(block=True, timeout=1)
			received += 1
		
		elif ins_type == 'jgz':
			if get_value(arg1, register_values) > 0:
				# minus one because at the end of the while loop idx is incremented by one
				idx += get_value(arg2, register_values)-1
			else:
				pass

		else:
			raise Exception(f'"{ins_type}" is an invalid instruction.')

		idx += 1


def part2():
	
	data = read_input('../input/input_day18.txt')
	instructions = parse_input(data)

	from_A = Queue() # sent from A
	from_B = Queue() # sent from B

	thread_A = Thread(target=run_program, args=(from_A, from_B, 0, instructions))
	thread_B = Thread(target=run_program, args=(from_B, from_A, 1, instructions))

	thread_A.start()
	thread_B.start()


if __name__ == '__main__':
	part1()
	part2()