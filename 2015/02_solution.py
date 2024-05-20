# solution file for day 2
# puzzle description: https://adventofcode.com/2015/day/2
# puzzle input: https://adventofcode.com/2015/day/2/input

from logger_setup import setup_logging
import logging
import time
from functools import reduce


def solve_part_1():
    with open("02_input.txt") as f:
        dimensions = f.read().split()

    paper_ft2 = 0

    for dim in dimensions:
        dim_list = dim.split("x")
        l = int(dim_list[0])
        w = int(dim_list[1])
        h = int(dim_list[2])

        prod_list = [l * w, w * h, h * l]

        # calculate area and slack
        paper_ft2 += 2 * sum(prod_list) + min(prod_list)

    logger.info(f"The elves should order {paper_ft2} square feet of wrapping paper")


def solve_part_2():
    with open("02_input.txt") as f:
        dimensions = f.read().split()

    ribon_ft = 0

    for dim in dimensions:
        # convert string to list of integers
        dim_list = [int(x) for x in dim.split("x")]
        dim_list.sort()

        # ribbon is used to wrap the present and for the bow
        ribon_ft += (
            2 * dim_list[0] + 2 * dim_list[1] + reduce(lambda x, y: x * y, dim_list)
        )

    logger.info(f"The elves should order {ribon_ft} feet of ribbon")


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
