# solution file for day 3
# puzzle description: https://adventofcode.com/2015/day/3
# puzzle input: https://adventofcode.com/2015/day/3/input

import sys
from logger_setup import setup_logging
import logging
import time


def move(x, y, step):
    if step == ">":
        x += 1
    elif step == "<":
        x -= 1
    elif step == "^":
        y += 1
    elif step == "v":
        y -= 1
    else:
        logger.error(f"Invalid step '{step}', check the puzzle input")
        sys.exit(1)  # Exit the program with an error status
    return (x, y)


def solve_part_1():
    with open("03_input.txt") as f:
        radio_instructions = f.read()

    x, y = 0, 0
    # list of visited coordinates
    route = [(x, y)]

    for step in radio_instructions:
        x, y = move(x, y, step)
        # add coordinate to list
        route.append((x, y))

    # remove duplicate coordinates
    houses_visited = len(set(route))

    logger.info(f"Santa visited {houses_visited} unique houses")


def solve_part_2():
    with open("03_input.txt") as f:
        radio_instructions = f.read()

    x1, y1, x2, y2 = 0, 0, 0, 0
    # list of visited coordinates (shared)
    route = [(0, 0)]

    for i, step in enumerate(radio_instructions):

        if i % 2 == 0:
            # Santa takes a step
            x1, y1 = move(x1, y1, step)
            route.append((x1, y1))
        else:
            # Robo-Santa takes a step
            x2, y2 = move(x2, y2, step)
            route.append((x2, y2))

    # remove duplicate coordinates
    houses_visited = len(set(route))

    logger.info(f"Santa and Robo-Santa have visited {houses_visited} unique houses")


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
