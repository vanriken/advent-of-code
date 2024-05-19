# solution day <day-number> https://adventofcode.com/2015/day/<day-number>
from logger_setup import setup_logging
import logging
import time


def solve_part_1():
    with open("<input-file>") as f:
        data = f.read()

    logger.info(f"<solution>")


def solve_part_2():
    with open("<input-file>") as f:
        data = f.read()

    logger.info(f"<solution>")


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
