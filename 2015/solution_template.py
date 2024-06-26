# solution file for day <day-number>
# puzzle description: https://adventofcode.com/2015/day/<day-number>
# puzzle input: https://adventofcode.com/2015/day/<day-number>/input

from logger_setup import setup_logging
import logging
import time

# Set up logging
setup_logging("DEBUG")

# Create a logger
logger = logging.getLogger(__name__)

with open("<input-file>") as f:
    data = f.read()


def solve_part_1():
    logger.info(f"<part1-solution>")


def solve_part_2():
    logger.info(f"<part2-solution>")


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
