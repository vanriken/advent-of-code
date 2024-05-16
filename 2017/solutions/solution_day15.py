import logging

logging.basicConfig(level=logging.INFO, 
	format='%(asctime)s - %(levelname)s: %(message)s')
#logging.disable(logging.CRITICAL)

def generator(start, factor, N):
	''' Generator function that returns a generator object.

	:param start: the start value of the generator (seed)
	:param factor: the multiplication factor in each round
	:param N: the number of values that the generator produces
	:return: a generator object
	'''

	value = start 
	div = 2147483647

	for n in range(N):
		value *= factor
		value = value % div
		# use a bit mask to get the last 16 bits
		yield value & 0xFFFF

def part1():

	count = 0
	N = 40 * 10**6

	gen1 = generator(start=289, factor=16807, N=N)
	gen2 = generator(start=629, factor=48271, N=N)

	# use enumerate to get an index for the pairs of values
	for n, (bits1, bits2) in enumerate(zip(gen1,gen2)):
		if bits1 == bits2:
			count += 1

		# update on the progress	
		if n % 10**6 == 0:
			logging.info(f'Progress: {n//10**6} / {N//10**6} (in millions)')

	logging.info('Progress: program finished')
	print(f'The final count is {count}')


def generator_v2(start, factor, multiple, N):
	''' Generator function that returns a generator object.

	:param start: the start value of the generator (seed)
	:param factor: the multiplication factor in each round
	:param multiple: the generator only returns values that are multiples this parameter
	:param N: the number of values that the generator produces
	:return: a generator object
	'''

	value = start 
	div = 2147483647
	n = 0

	while n < N:
		value *= factor
		value = value % div
		if value % multiple == 0: 
			n += 1
			# use a bit mask to get the last 16 bits
			yield value & 0xFFFF

def part2():

	count = 0
	N = 5 * 10**6

	gen1 = generator_v2(start=289, factor=16807, multiple=4, N=N)
	gen2 = generator_v2(start=629, factor=48271, multiple=8, N=N)

	for n, (bits1, bits2) in enumerate(zip(gen1,gen2)):
		if bits1 == bits2:
			count += 1

		# update on the progress	
		if n % 10**6 == 0:
			logging.info(f'Progress: {n//10**6} / {N//10**6} (in millions)')
	logging.info('Progress: program finished')
	print(f'The final count is {count}')

if __name__ == '__main__':
	part1()