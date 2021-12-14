import logging
from functools import reduce
from operator import xor

logging.basicConfig(level=logging.DEBUG, 
	format='%(asctime)s - %(levelname)s: %(message)s')
logging.disable(logging.CRITICAL)


def read_input(filepath, mode=None):
	""" Read the input and return it as a list of integers. """
	
	if mode == 'ASCII':
		with open(filepath) as f:
			return list(map(ord, f.read()))
	else:
		with open(filepath) as f:
			return list(map(int, f.read().split(',')))

def shift_lst(lst, shift_amount):
	""" Rotates a list an arbitrary number of items to the left. """

	for _ in range(shift_amount):
		lst.append(lst.pop(0))

def reverse_sublist(lst, start_idx, end_idx):
	""" Reverses the sublist starting at start_idx and ending at end_idx """
	
	if start_idx < end_idx:
		
		lst[start_idx:end_idx] = lst[start_idx:end_idx][::-1]
	
	else:
		
		# shift left until list is [... START ... END]
		shift_amount = end_idx
		shift_lst(lst,shift_amount)

		# reverse the elements of the sublist
		lst[((start_idx - shift_amount) % len(lst)):] = \
			lst[((start_idx - shift_amount) % len(lst)):][::-1]
		
		# shift left to undo the first shift
		shift_amount = len(lst) - shift_amount
		shift_lst(lst,shift_amount)

def execute_knot_hash_round(lst, lengths, current_pos=0, skip_size=0):
	""" Executes one round of the knot hash algorithm

	:param lst: a list of numbers (modified by the function)
	:param length: a sequence of length used for knot hashing
	:param current_pos: start position on the list (default:0)
	:param skip_size: number of numbers skipped after each iteration (default:0)

	:return current_pos: the position after the hashing round has been completed
	:return skip_size: the value of skip_size after the hashing round has been completed 

	"""

	for length in lengths:

		logging.debug(lst)
		
		if length != 0:

			start_idx = current_pos % len(lst)
			end_idx = (start_idx + length) % len(lst)
			logging.debug(f'start_idx: {start_idx}, end_idx: {end_idx}')
			
			reverse_sublist(lst, start_idx, end_idx)
			logging.debug(f'after reversing sublist: {lst}\n')

		else:
			# do nothing, the list stays as it is
			pass

		current_pos = (current_pos + length + skip_size) % len(lst)
		skip_size += 1

	return (current_pos, skip_size)

def compute_dense_hash(sparse_hash, block_size=16):
	"""	Reduces the sparse hash of the knot hash algorithm to a dense hash 
		
		:param sparse_hash: the sparse hash that is initially computed by the knot hash algorithm
		:param block_size: the block size that is used to reduce the sparse hash to the dense hash
		:return dense_hash: the dense hash after xor reduction
	"""	

	dense_hash = []

	for i in range(0,len(sparse_hash), block_size):
		sublist = sparse_hash[i:i+block_size]
		xor_result = reduce(xor, sublist)
		dense_hash.append(xor_result)

	return dense_hash

def get_hex_string(dense_hash):
	""" Returns the hex-string representation of the dense hash """

	hex_string = ''
	for number in dense_hash:
		hex_string += hex(number).split('x')[1].zfill(2)

	return hex_string

def compute_knot_hash(lengths, n_rounds=64):
	""" Computes the knot hash of for a list of ASCII codes 

		:param lengths: a list of ASCII codes
		:param n_rounds: specifies the number of rounds in the hashing process
		:return hex_string: the knot hash of the input
	"""
	
	lst = [i for i in range(256)]
	lengths = lengths + [17,31,73,47,23]
	current_pos = 0
	skip_size = 0 

	for _ in range(n_rounds):
		current_pos, skip_size = execute_knot_hash_round(lst, lengths, current_pos, skip_size)
	dense_hash = compute_dense_hash(lst)
	hex_string = get_hex_string(dense_hash)

	return hex_string

def main():
	
	"""
	PART 1
	"""
	#puzzle input
	lst = [i for i in range(256)]
	lengths = read_input('../input/input_day10.txt')

	#example input
	# lst = list(range(5))
	# lengths = [3, 4, 1, 5]

	current_pos, skip_size = execute_knot_hash_round(lst, lengths)
	print(f'PART1 - Multiplication check: {lst[0]} * {lst[1]} = {lst[0]*lst[1]}')

	"""
	PART 2
	"""
	# get sequence of lengths by using the ASCII codes of the characters

	# tests
	test_input1 = list(map(ord,''))
	test_input2 = list(map(ord,'AoC 2017'))
	test_input3 = list(map(ord,'1,2,3'))
	test_input4 = list(map(ord,'1,2,4'))

	assert compute_knot_hash(test_input1)=='a2582a3a0e66e6e86e3812dcb672a272',\
		f'assertion failed for test_input1'
	assert compute_knot_hash(test_input2)=='33efeb34ea91902bb2f59c9920caa6cd',\
		f'assertion failed for test_input2'
	assert compute_knot_hash(test_input3)=='3efbe78a8d82f29979031a4aa0b16a9d',\
		f'assertion failed for test_input3'
	assert compute_knot_hash(test_input4)=='63960835bcdc130f0b66d7ff4f6a5a8e',\
		f'assertion failed for test_input4'

	# compute knot hash
	lengths = read_input('../input/input_day10.txt',mode='ASCII')
	hex_string = compute_knot_hash(lengths)
	print(f'PART2 - The knot hash is: {hex_string}')

if __name__ == '__main__':
	main()