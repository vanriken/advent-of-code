# choose which part to run {"PART1", "PART2"}
selection = "PART1"

# read the input as a list of integers
with open("../input/input_day01.txt") as file:
	digits = []
	for line in file:
		for character in line:
			try: 
				digits.append(int(character))
			except ValueError: # ignore characters in the input that cannot be converted to ints
				print(f"INFO:Character {repr(character)} cannot be converted to an integer")


if selection == "PART1":

	# test inputs for part 1
	test1 = [1,1,2,2]
	test2 = [1,1,1,1]
	test3 = [1,2,3,4]
	test4 = [9,1,2,1,2,1,2,9]

	# uncomment the next line to check the examples
	#digits = test1

	s = 0

	for i in range(0, len(digits) - 1):
		d_current = digits[i]
		d_next = digits[i+1]

		if d_current == d_next:
			s += d_current

	# check if the last digit matches the first digit
	if digits[-1] == digits[0]:
		s += digits[-1]

	print(f"PART1: The sum is {s}")

elif selection == "PART2":

	# test inputs for part 2
	test1 = [1,2,1,2]
	test2 = [1,2,2,1]
	test3 = [1,2,3,4,2,5]
	test4 = [1,2,3,1,2,3]
	test5 = [1,2,1,3,1,4,1,5]

	# uncomment the next line to check the examples
	#digits = test3

	# calculate size of step to the digit halfway around the list
	length_list = len(digits)
	step = length_list // 2

	s = 0

	for i in range(0, len(digits)):
		d_current = digits[i]
		d_halfway = digits[(i + step) % length_list]

		# alternative solution 
		# 
		# try:
		# 	d_halfway = digits[i + step]
		# except IndexError:
		# 	d_halfway = digits[i - step]

		if d_current == d_halfway:
			s += d_current

	print(f"PART2: The sum is {s}")

else: 
	print("WARNING:The variable 'selection' supports the values {'PART1','PART2'}")
