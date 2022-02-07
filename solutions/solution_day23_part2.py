import logging
import numpy as np
from collections import defaultdict
from math import sqrt

logging.basicConfig(level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s: %(message)s')
#logging.disable(logging.CRITICAL)

def execute_instructions():
    ''' Executes the code of the processor
        The code has been translated to python statements for easier analysis.
        Forward jumps are implemented as if statements.
        Backward jumps are implemented as do while loops.

        Cannot be used to solve the problem but provides insight to find the 
        shortcut that is used in the solution.
    '''

    # dictionary to hold the values of the registers
    registers = defaultdict(int)
    registers['a'] = 1
    registers['b'] = 67
    registers['c'] = registers['b']

    if registers['a'] != 0:
        registers['b'] = registers['b'] * 100 + 100_000
        registers['c'] = registers['b'] + 17_000
    else: 
        pass
    logging.debug(f'Setup complete - {registers}')
    # -------------------------------------------------------------------------
    while True:
        registers['f'] = 1
        registers['d'] = 2
        # ---------------------------------------------------------------------
        while True:
            registers['e'] = 2
            # -----------------------------------------------------------------
            while True:
                registers['g'] = registers['d'] * registers['e'] - registers['b']
                
                if registers['g'] == 0:
                    registers['f'] = 0
                else:
                    pass
                registers['e'] = registers['e'] + 1
                registers['g'] = registers['e'] - registers['b']
                # jump is not executed when value of register is zero
                if registers['g'] == 0:
                    break
            #------------------------------------------------------------------
            registers['d'] = registers['d'] + 1
            registers['g'] = registers['d'] - registers['b']
            # jump is not executed when value of register is zero
            if registers['g'] == 0:
                break
        # ---------------------------------------------------------------------
        if registers['f'] == 0:
            registers['h'] = registers['h'] + 1
        else:
            pass
        registers['g'] = registers['b'] - registers['c']
        if registers['g'] == 0: # program finishes
            break
        registers['b'] = registers['b'] + 17
    #----------------------------------------------------------------------------
    print(f'Program finished: {registers}')

def is_prime(n):

    ''' Checks if the input "n" is a prime number.
        Returns True if the input is a prime number.
        Returns False if the input is a composite number.
    ''' 

    root = sqrt(n)
    for d in range(2, int(root)+1):
        if n % d == 0:
            return False
        else:
            pass 

    return True

def count_composite_numbers(start, end, step=1):
    ''' Counts the composite numbers in the interval [start, end].
        It is possible to ignore values in the interval by setting step>1.
    ''' 
    h = 0
    for n in range(start, end + step, step):
        if is_prime(n) == False:
            h = h + 1 
            logging.debug(f'composite number: {n}')
        else:
            pass
    return h 

def main():

    b = 67
    b = b * 100 + 100_000 
    c = b + 17_000

    h = count_composite_numbers(b, c, 17)
    print(f'Composite numbers found: {h}')
   
if __name__ == '__main__':
    main()
