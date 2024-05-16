import logging
logging.basicConfig(filename='solution_day04.log', filemode='w', level=logging.DEBUG, 
					format='%(asctime)s - %(levelname)s: %(message)s')

# comment the next line to enable logging
#logging.disable(logging.CRITICAL)

def is_valid_part1(passphrase):
	""" Checks if a passphrase is valid (part 1)

		Valid passphrases do not contain duplicate words
	"""

	passphrase = passphrase.split()
	return len(passphrase) == len(set(passphrase))

def is_valid_part2(passphrase):
	""" Checks if a passphrase is valid (part 2) 
		
		Valid passphrases may not contain words, 
		that are anagrams of each other
	"""

	passphrase = passphrase.split()
	wordlist = []

	# add all the words to a list in sorted fashion
	for word in passphrase:
		wordlist.append(tuple(sorted(word)))

	logging.debug(f"\nwordlist={wordlist}, length={len(wordlist)}\n" + 
		f"set(wordlist)={set(wordlist)}, length={len(set(wordlist))}")

	return len(wordlist) == len(set(wordlist))

def main():

	# part 1 -----------------------------------------------------------
	# make sure that is_valid_part1() works for the test cases
	assert is_valid_part1('aa bb cc dd ee'), \
		'Passphrase wrongly classified as invalid'
	assert not is_valid_part1('aa bb cc dd aa'), \
		'Passphrase wrongly classified as valid'
	assert is_valid_part1('aa bb cc dd aaa'), \
		'Passphrase wrongly classified as invalid'

	number_valid_passphrases = 0
	with open('../input/input_day04.txt') as file:
		for passphrase in file:
			if is_valid_part1(passphrase):
				number_valid_passphrases += 1

	print(f'PART1. Number of valid passphrases: {number_valid_passphrases}')

	# part 2 -----------------------------------------------------------
	# make sure that is_valid_part2() works for the test cases
	assert is_valid_part2('abcde fghij'), \
		'Passphrase wrongly classified as invalid'
	assert not is_valid_part2('abcde xyz ecdab'), \
	 	'Passphrase wrongly classified as valid'
	assert is_valid_part2('a ab abc abd abf abj'), \
		'Passphrase wrongly classified as invalid'
	assert is_valid_part2('iiii oiii ooii oooi oooo'), \
		'Passphrase wrongly classified as invalid'
	assert not is_valid_part2('oiii ioii iioi iiio'), \
		'Passphrase wrongly classified as invalid'

	number_valid_passphrases = 0
	with open('../input/input_day04.txt') as file:
		for passphrase in file:
			if is_valid_part2(passphrase):
				number_valid_passphrases += 1

	print(f'PART2. Number of valid passphrases: {number_valid_passphrases}')

if __name__ == '__main__':
	main()