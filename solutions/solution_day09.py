import logging

logging.basicConfig(level=logging.DEBUG, 
	format='%(asctime)s - %(levelname)s: %(message)s')
logging.disable(logging.CRITICAL)

def read_stream(filepath):
	""" Reads the stream from a text file and returns it as a string 

		:param filepath: the path of the text file containing the stream
		:return f.read(): a string containing the stream
	"""

	with open(filepath) as f:
		return f.read()


def analyze_stream(stream):
	""" Analyzes the stream and returns the number of groups, the total score 
		and the number of garbage characters in the stream
		
		:param stream: a string representing the stream
		:return n_groups: the number of groups found in the stream
		:return score: the total score for all groups in the stream
		:return n_garbage_chars: the number of garbage chars in the stream
	"""

	depth = 0
	n_groups = 0
	score = 0
	garbage_section = False
	n_garbage_chars = 0

	i = 0
	while i < len(stream):

		char = stream[i]

		if garbage_section:
			if char == '>': 	# current garbage section ends
				garbage_section = False 
			elif char == '!':	# ignore the character after the '!'
				i+=1
			else:
				n_garbage_chars += 1
					
		else:
			if char == '{':		# start of group
				depth += 1
			elif char == '}':	# end of group
				n_groups += 1
				score += depth  # score of group is given by depth
				depth -= 1
			elif char == '<':	# start of a garbage section
				garbage_section = True 

		# increment counter
		i+=1

	logging.debug(f'n_groups = {n_groups}')
	logging.debug(f'score = {score}')
	logging.debug(f'number of garbage characters = {n_garbage_chars}')

	return n_groups, score, n_garbage_chars

def main():
	
	stream = '{{<a!>},{<a!>},{<a!>},{<ab>}}'
	stream = read_stream('../input/input_day09.txt')
	n_groups, score, n_garbage_chars = analyze_stream(stream)

	print(f'stream-analysis result'.upper())
	print(f'1.Number of groups:\t\t{n_groups}')
	print(f'2.Total score:\t\t\t{score}')
	print(f'3.Garbage characters:\t{n_garbage_chars}')
	
if __name__ == '__main__':
	main()