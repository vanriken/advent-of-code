# solution day 1 https://adventofcode.com/2015/day/1
from logger_setup import setup_logging
import logging
import time


def solve_part_1():
    with open("01-input.txt") as f:
        instructions = f.read()

    go_up_count = instructions.count("(")
    go_down_count = instructions.count(")")

    target_floor = go_up_count - go_down_count

    logger.info(f"The instructions take Santa to floor {target_floor}")


def solve_part_2():
    with open("01-input.txt") as f:
        instructions = f.read()

    position = 0
    floor = 0

    for char in instructions:
        position += 1
        if char == "(":
            floor += 1
        else:
            floor -= 1

        # Check if Santa has entered the basement
        if floor < 0:
            break

    logger.info(f"Santa first enters the basement with character {position}")


if __name__ == "__main__":

    # Set up logging
    setup_logging("DEBUG")

    # Create a logger
    logger = logging.getLogger(__name__)

    # Record a start time
    start_time = time.time()

    # Record a start time
    start_time = time.time()
    solve_part_1()
    solve_part_2()

    # Calculate and log the elapsed time
    elapsed_time = time.time() - start_time
    logger.info(f"Script execution time: {elapsed_time:.3f} seconds")
