import logging
import numpy as np
from math import sqrt
from enum import IntEnum

logging.basicConfig(level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s: %(message)s')
logging.disable(logging.CRITICAL)

class Direction(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class NodeStatus(IntEnum):
    CLEAN = 0
    INFECTED = 1

def read_input(filepath):

    with open(filepath) as file: 
        text = file.read().replace('.','0').replace('#','1')
   
    data = [] 
    for line in text.split():
        data.append(list(line))
    
    data_arr = np.array(data, dtype=int)
    
    return data_arr

def get_grid(arr, n_iter):

    d = int(len(arr)/2)
    # size of grid is limited by number of iterations
    size_grid = 2*n_iter + 1
    grid = np.zeros((size_grid, size_grid), dtype=int)
    grid_center = int(size_grid/2)
    # put arr in the center of the grid
    grid[grid_center-d:grid_center+d+1, grid_center-d:grid_center+d+1] = arr

    return grid

def change_direction(direction, turn_direction):

    if turn_direction == 'RIGHT':
        direction = (direction+1)%4
    elif turn_direction == 'LEFT': 
        direction = (direction-1)%4
    else:
        raise Exception(f'turn_direction "{turn_direction}" is not supported')

    return direction


def main():

    arr = read_input('../input/input_day22.txt')
    logging.debug(arr)
    
    n = 10000
    infections = 0
    grid = get_grid(arr, n)
    grid_center = int(len(grid)/2)
    row, col = [grid_center, grid_center]
    direction = Direction.UP
    
    for i in range(n):

        # turn right is current node is infected, otherwise turn left
        if grid[row,col] == NodeStatus.INFECTED:
            direction = change_direction(direction,'RIGHT')
        elif grid[row,col] == NodeStatus.CLEAN:
            direction = change_direction(direction,'LEFT')
            infections += 1 # clean node will become infected
        else:
            raise Exception('node status is invalid')

        # update the state of the current node
        grid[row,col] = (grid[row,col] + 1) % 2
                               
        # virus carrier moves forward one step
        if direction == Direction.UP:
            row -= 1
        elif direction == Direction.RIGHT:
            col += 1
        elif direction == Direction.DOWN:
            row += 1
        elif direction == Direction.LEFT:
            col -= 1
        else:
            raise Exception('invalid direction')

    print(f'Number of bursts that caused an infection: {infections}.')


if __name__ == '__main__':
    main()