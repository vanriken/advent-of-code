import logging
import numpy as np
from collections import defaultdict

logging.basicConfig(level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s: %(message)s')
#logging.disable(logging.CRITICAL)

def get_value(arg, registers):
    ''' 
    Returns the value of the argument of an instruction. 
    Many of the instructions can take either a register (letter) 
    or a number as an argument.
    '''

    try:
        val = int(arg)
    except ValueError:
        val = registers[arg]
    return val

def main():

    # list to hold the instructions
    instructions = []
    with open('../input/input_day23.txt') as f:
        for line in f:
            instructions.append(line.split())

    # dictionary to hold the values of the registers
    registers = defaultdict(int)

    i = 0
    n = len(instructions)
    count = 0

    while (i>=0 and i<n):

        ins = instructions[i]
        keyword = ins[0]
        arg1 = ins[1]
        arg2 = ins[2]

        if keyword == 'set':
            registers[arg1] = get_value(arg2, registers)

        elif keyword == 'sub':
            registers[arg1] = registers[arg1] - get_value(arg2, registers)

        elif keyword == 'mul':
            registers[arg1] = registers[arg1] * get_value(arg2, registers)
            count += 1

        elif keyword == 'jnz':
            # jnz X Y: jumps with an offset of the value of Y,
            # but only if the value of X is not zero
            if get_value(arg1, registers) != 0:
                i += get_value(arg2, registers)
                continue # move to the next iteration
            else:
                pass

        else:
            raise Exception('instruction type not recognized')

        # move to the next instruction
        i += 1

    print(f'The "mul" instruction is invoked {count} times.')
    print(f'Register values: {registers}')

if __name__ == '__main__':
    main()