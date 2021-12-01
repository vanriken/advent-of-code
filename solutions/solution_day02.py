from itertools import combinations

# organize the input data in a matrix 
# 1st dimension: row, second dimension: column
matrix = []
with open("../input/input_day02.txt") as file:
	for line in file:
		row = [int(x) for x in line.split()]
		matrix.append(row)

# PART1
s = 0
for row in matrix:
	s += max(row) - min(row)

print(f"PART1: The checksum of the spreadsheet is {s}")


# PART2
s = 0
for row in matrix:
	# sort the row before getting the combinations
	# this makes sure that pair[1] >= pair[0]
	pairs = combinations(sorted(row), 2)
	for pair in pairs:
		if pair[1] % pair[0] == 0:
			s += pair[1] // pair[0]

print(f"PART2: The sum of the results for each row is {s}")