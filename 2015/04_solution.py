# solution file for day 4
# puzzle description: https://adventofcode.com/2015/day/4
# puzzle input: https://adventofcode.com/2015/day/4/input

from logger_setup import setup_logging
import logging
import time
from hashlib import md5


def solve_part_1():
    with open("04_input.txt") as f:
        data = f.read()

    i = 1

    while True:
        hexdigest = md5((data + str(i)).encode()).hexdigest()
        if hexdigest[:5] == "00000":
            break
        i += 1

    logger.info(f"hash({data + str(i)}) = {hexdigest}")
    logger.info(f"The number is {i}")


def solve_part_2():
    with open("04_input.txt") as f:
        data = f.read()

    i = 1

    while True:
        hexdigest = md5((data + str(i)).encode()).hexdigest()
        if hexdigest[:6] == "000000":
            break
        i += 1

    logger.info(f"hash({data + str(i)}) = {hexdigest}")
    logger.info(f"The number is {i}")


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
