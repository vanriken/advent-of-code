# solution file for day 7
# puzzle description: https://adventofcode.com/2015/day/7
# puzzle input: https://adventofcode.com/2015/day/7/input

from logger_setup import setup_logging
import logging
import time

# Set up logging
setup_logging("INFO")
# Create a logger
logger = logging.getLogger(__name__)

# get instructions as list of strings
with open("07_input.txt") as f:
    instructions = f.read().splitlines()

# create two empty dictionaries
# calculations contains the instructions to calculate the signals (input)
# results contains the wire signals that have already been calculated
calculations = {}
results = {}

for instruction in instructions:
    (ops, res) = instruction.split("->")
    calculations[res.strip()] = ops.strip().split()

logger.debug(calculations)


def calculate_wire_signal(wire):
    # this is a recursive function used to calculate the signal at a wire

    if wire.isdigit():
        # base case
        return int(wire)

    if wire in results:
        # the value of this wire has already been calculated
        # do not calculate it again (memoization)
        pass
    else:
        # recursive cases
        # get the entire operation, for example ['hv', 'OR', 'hu']
        ops = calculations[wire]
        if len(ops) == 1:  # wire is directly connected to signal
            res = calculate_wire_signal(ops[0])
        else:
            # for all other instructions, the operation is two positions from the end
            op = ops[-2]
            if op == "AND":
                res = calculate_wire_signal(ops[0]) & calculate_wire_signal(ops[2])
            elif op == "OR":
                res = calculate_wire_signal(ops[0]) | calculate_wire_signal(ops[2])
            elif op == "NOT":
                res = 2**16 - 1 - calculate_wire_signal(ops[1])
            elif op == "RSHIFT":
                res = calculate_wire_signal(ops[0]) >> calculate_wire_signal(ops[2])
            elif op == "LSHIFT":
                res = calculate_wire_signal(ops[0]) << calculate_wire_signal(ops[2])
        # store the result to save time the next time it is needed
        results[wire] = res

    return results[wire]


def solve_part_1():

    logger.info(f"Part 1: The signal at wire a is {calculate_wire_signal('a')}")


def solve_part_2():

    # override value of wire b
    calculations["b"] = ["46065"]

    # clear the dictionary with the results
    results.clear()

    # calculate the signal again
    logger.info(f"Part 2: The signal at wire a is {calculate_wire_signal('a')}")


if __name__ == "__main__":

    # Record a start time
    start_time = time.time()

    # Record a start time
    start_time = time.time()
    solve_part_1()
    solve_part_2()

    # Calculate and log the elapsed time
    elapsed_time = time.time() - start_time
    logger.info(f"Script execution time: {elapsed_time:.3f} seconds")
