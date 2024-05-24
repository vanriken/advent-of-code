# solution file for day 5
# puzzle description: https://adventofcode.com/2015/day/5
# puzzle input: https://adventofcode.com/2015/day/5/input

from logger_setup import setup_logging
import logging
import time


def criterion1(string):
    # Returns True if criterion is met, False if not met
    # Criterion: string contains at least three vowels
    nr_of_vowels = 0
    vowels = "aeiou"
    for char in string:
        if char in vowels:
            nr_of_vowels += 1

    return nr_of_vowels >= 3


def criterion2(string):
    # Returns True if criterion is met, False if not met
    # Criterion: string contains at least one letter that appears twice in a row
    found_double_letter = False
    for i in range(len(string) - 1):
        # check whether current letter is the same as next letter
        if string[i] == string[i + 1]:
            found_double_letter = True
            break

    return found_double_letter


def criterion3(string):
    # Returns True if criterion is met, False if not met
    # Criterion: string does NOT contain ab, cd, pq, xy
    does_not_contain = True
    for char_pair in ["ab", "cd", "pq", "xy"]:
        if char_pair in string:
            does_not_contain = False
            break

    return does_not_contain


def criterion4(string):
    # Returns True if criterion is met, False if not met
    # Criterion: string contains a pair of any two letters that appear at
    #   least twice in the string without overlapping

    # get all the pairs
    pairs_of_letters = []
    for i in range(len(string) - 1):
        pairs_of_letters.append(string[i] + string[i + 1])

    logger.debug(f"{pairs_of_letters=}")

    # criterion is met if a pair of letters is included more than once in pairs_of_letters
    # UNLESS the two pairs are next to each other in the list (then they are overlapping)
    # so we first remove overlapping pairs

    filtered_pairs = [pairs_of_letters[0]]

    for i in range(1, len(pairs_of_letters)):
        if pairs_of_letters[i] != pairs_of_letters[i - 1]:
            filtered_pairs.append(pairs_of_letters[i])

    logger.debug(f"{filtered_pairs=}")
    logger.debug(f"{set(filtered_pairs)=}")

    # now check if the list filtered_pairs contain at least one duplicate
    # if it does we have a pair of two letters that appear at least twice in the string
    # without overlapping

    if len(set(filtered_pairs)) != len(filtered_pairs):
        return True
    else:
        return False


def criterion5(string):
    # Returns True if criterion is met, False if not met
    # Criterion: string contains at least one letter which repeats with exactly
    #   one letter between them

    return_value = False
    for i in range(len(string) - 2):
        # compare current letter with the one two positions further
        if string[i] == string[i + 2]:
            return_value = True
            break

    return return_value


def is_string_nice(string):
    # returns True if string passes all criteria (for part 1)
    return criterion1(string) and criterion2(string) and criterion3(string)


def is_string_nice_v2(string):
    # returns True if string passes all criteria (for part 2)
    return criterion4(string) and criterion5(string)


def solve_part_1():

    # some sanity checks
    test_string = "ugknbfddgicrmopn"
    logger.debug(f"{test_string}: {is_string_nice(test_string)}")
    test_string = "aaa"
    logger.debug(f"{test_string}: {is_string_nice(test_string)}")
    test_string = "jchzalrnumimnmhp"
    logger.debug(f"{test_string}: {is_string_nice(test_string)}")
    test_string = "haegwjzuvuyypxyu"
    logger.debug(f"{test_string}: {is_string_nice(test_string)}")
    test_string = "dvszwmarrgswjxmb"
    logger.debug(f"{test_string}: {is_string_nice(test_string)}")

    with open("05_input.txt") as f:
        strings = f.read().split()

    nr_of_nice_strings = 0
    for string in strings:
        nr_of_nice_strings += is_string_nice(string)

    logger.info(f"The input contains {nr_of_nice_strings} nice strings")


def solve_part_2():

    # some sanity checks
    test_string = "qjhvhtzxzqqjkmpb"
    logger.debug(f"{test_string}: {is_string_nice_v2(test_string)}")
    test_string = "xxyxx"
    logger.debug(f"{test_string}: {is_string_nice_v2(test_string)}")
    test_string = "uurcxstgmygtbstg"
    logger.debug(f"{test_string}: {is_string_nice_v2(test_string)}")
    test_string = "ieodomkazucvgmuy"
    logger.debug(f"{test_string}: {is_string_nice_v2(test_string)}")

    with open("05_input.txt") as f:
        strings = f.read().split()

    nr_of_nice_strings = 0
    for string in strings:
        nr_of_nice_strings += is_string_nice_v2(string)

    logger.info(f"The input contains {nr_of_nice_strings} nice strings")


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
