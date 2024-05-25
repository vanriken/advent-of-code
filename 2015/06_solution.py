# solution file for day 6
# puzzle description: https://adventofcode.com/2015/day/6
# puzzle input: https://adventofcode.com/2015/day/6/input

from logger_setup import setup_logging
import logging
import time
import numpy as np
from enum import Enum
import re


# define enum class
class LightAction(Enum):
    TURN_ON = 1
    TURN_OFF = 2
    TOGGLE = 3


def extractLightAction(string):

    logger.debug(f"{string=}")

    if "turn on" in string:
        action = LightAction.TURN_ON
    elif "turn off" in string:
        action = LightAction.TURN_OFF
    else:
        action = LightAction.TOGGLE

    logger.debug(f"{action=}")

    return action


def extractCoordinates(string):
    # each instruction has four numbers
    # extract these numbers using regular expression
    # the first pair of numbers specifies the start corner
    # the second pair of numbers specifies the end corner

    logger.debug(f"{string=}")
    numbers_as_strings = re.findall(r"\d+", string)
    numbers = [int(x) for x in numbers_as_strings]
    logger.debug(f"{numbers=}")

    start_corner = (numbers[0], numbers[1])
    end_corner = (numbers[2], numbers[3])

    return start_corner, end_corner


def applyLightAction(state_array, action, start_corner, end_corner):
    # This function applies a lighting instruction to the lights (part 1)
    # The state of the lights is represented by the array "state_array"

    # Note: the modification made to state_array inside this function affect the original array

    # Get the start and end coordinates
    x1, y1 = start_corner
    x2, y2 = end_corner

    # Determine the size of the subarray where action will be applied
    subarray_size = (x2 - x1 + 1, y2 - y1 + 1)

    # Create two mask arrays
    mask_ones = np.ones(subarray_size)
    mask_zeros = np.zeros(subarray_size)

    # Get the subbaray from the state_array
    state_subarray = state_array[x1 : x2 + 1, y1 : y2 + 1].copy()

    # Apply the step
    if action == LightAction.TURN_ON:
        # logical OR with mask of ones
        state_array[x1 : x2 + 1, y1 : y2 + 1] = np.logical_or(state_subarray, mask_ones)
    elif action == LightAction.TURN_OFF:
        # logical AND with mask of zeroes
        state_array[x1 : x2 + 1, y1 : y2 + 1] = np.logical_and(
            state_subarray, mask_zeros
        )
    else:
        # action == LightAction.TOGGLE
        # logical XOR with mask of ones
        state_array[x1 : x2 + 1, y1 : y2 + 1] = np.logical_xor(
            state_subarray, mask_ones
        )


def applyLightAction_v2(state_array, action, start_corner, end_corner):
    # This function applies a lighting instruction to the lights (part 2)
    # The brightness of the lights is represented by the array "state_array"

    # Note: the modification made to state_array inside this function affect the original array

    # Get the start and end coordinates
    x1, y1 = start_corner
    x2, y2 = end_corner

    # Determine the size of the subarray where action will be applied
    subarray_size = (x2 - x1 + 1, y2 - y1 + 1)

    # create a mask array
    array_ones = np.ones(subarray_size)

    # Get the subbaray from the state_array
    state_subarray = state_array[x1 : x2 + 1, y1 : y2 + 1].copy()

    # Apply the step
    if action == LightAction.TURN_ON:
        # increase brightness by 1
        state_array[x1 : x2 + 1, y1 : y2 + 1] = state_subarray + array_ones
    elif action == LightAction.TURN_OFF:
        # reduce brightness by 1
        state_array[x1 : x2 + 1, y1 : y2 + 1] = state_subarray - array_ones
        # minimum brightness is zero
        state_array[state_array < 0] = 0
    else:
        # action == LightAction.TOGGLE
        # increase brightness by 2
        state_array[x1 : x2 + 1, y1 : y2 + 1] = state_subarray + 2 * array_ones


def solve_part_1():
    with open("06_input.txt") as f:
        instructions = f.read().splitlines()

    light_state_array = np.zeros((1000, 1000))

    for instruction in instructions:
        # extract the type of action (turn on, turn off, toggle), start coordinate and end coordinate
        action = extractLightAction(instruction)
        start_corner, end_corner = extractCoordinates(instruction)
        logger.debug(f"{start_corner=}, {end_corner=}")

        # modify the array based on action, start_corner and end_corner
        applyLightAction(light_state_array, action, start_corner, end_corner)

    # print with zero decimal points
    logger.info(f"Number of lights turned on: {np.sum(light_state_array):.0f}")


def solve_part_2():
    with open("06_input.txt") as f:
        instructions = f.read().splitlines()

    light_brightness_array = np.zeros((1000, 1000))

    for instruction in instructions:
        # extract the type of action (turn on, turn off, toggle), start coordinate and end coordinate
        action = extractLightAction(instruction)
        start_corner, end_corner = extractCoordinates(instruction)
        logger.debug(f"{start_corner=}, {end_corner=}")

        # modify the array based on action, start_corner and end_corner
        applyLightAction_v2(light_brightness_array, action, start_corner, end_corner)

    # print with zero decimal points
    logger.info(f"The total brightness is: {np.sum(light_brightness_array):.0f}")


if __name__ == "__main__":

    # Set up logging
    setup_logging("INFO")

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
