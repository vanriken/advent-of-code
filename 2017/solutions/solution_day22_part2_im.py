import logging
import numpy as np
from collections import defaultdict
from enum import IntEnum

logging.basicConfig(level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s: %(message)s')
#logging.disable(logging.CRITICAL)

class Direction(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class NodeStatus(IntEnum):
    CLEAN = 0
    WEAKENED = 1
    INFECTED = 2
    FLAGGED = 3

def read_input(filepath):

    with open(filepath) as file: 
        text = file.read()
   
    data = defaultdict(lambda: 0)
    
    rows = text.split()
    center = len(rows) // 2

    for row_idx, row in enumerate(rows):
        for col_idx, node in enumerate(row):
            if node == '#':
                # row gives position on y-axis, col gives position on x-axis
                # y: decrease in row_idx, x: increase in col_idx
                x = col_idx
                y = -row_idx 
                data[x+y*1j] = 2
    
    return data, center


def main():

    data, m = read_input('../input/input_day22.txt')
    
    pos = m-m*1j
    # starting direction is up
    direction = 0+1j   

    n = 10000000
    infections = 0

    for i in range(n):

        # turn right is current node is infected, otherwise turn left
        if data[pos] == NodeStatus.CLEAN:
            direction = direction * 1j
            data[pos] = NodeStatus.WEAKENED

        elif data[pos] == NodeStatus.WEAKENED:
            data[pos] = NodeStatus.INFECTED
            infections += 1

        elif data[pos] == NodeStatus.INFECTED:
            direction = direction * (-1j)
            data[pos] = NodeStatus.FLAGGED

        elif data[pos] == NodeStatus.FLAGGED:
            direction = -direction
            data[pos] = NodeStatus.CLEAN

        else:
            raise Exception('node status is invalid')
                  
        # virus carrier moves forward one step
        pos = pos + direction


    print(f'Number of bursts that caused an infection: {infections}.')


if __name__ == '__main__':
    main()