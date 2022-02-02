import logging
import numpy as np
from math import sqrt

logging.basicConfig(level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s: %(message)s')
#logging.disable(logging.CRITICAL)

def read_data(filepath):

    ''' Processes the input text and returns two dictionaries. 

        :return: Two dictionaries. The dictionary 'input_pattern' contains 
            the input patterns as numpy arrays. The 'output pattern' as
            numpy arrays. The keys of the dictionaries can be used to match
            the input patterns to the corresponding output patterns.
    '''

    input_pattern = dict()
    output_pattern = dict()

    with open(filepath) as f:
        data = f.read()

    # preprocess the data 
    data = data.replace('#','1').replace('.','0').replace('/','')
    lines = data.split('\n')

    i = 0
    for line in lines:
         # get the input and output pattern as one-dimensional list
        p_in, p_out = line.split(' => ')
        p_in = [int(x) for x in list(p_in)]
        p_out = [int(x) for x in list(p_out)]

        dim_in = int(sqrt(len(p_in)))
        dim_out = int(sqrt(len(p_out)))

        p_in = np.array(p_in).reshape(dim_in, -1)
        p_out = np.array(p_out).reshape(dim_out,-1)

        # add the input and output pattern to the corresponding dictionary
        input_pattern[i] = p_in
        output_pattern[i] = p_out
        i+=1

    return input_pattern, output_pattern


def grid_permutations(grid):

    ''' Permutates the input grid by rotating it, flipping it horizontally
        and flipping it vertically. Returns a generator object with all the 
        permutations.

        rotation (degrees): 0, 90, 180, 270
        flip horizontally (left/right): no, yes
        flip vertically (up/down): no, yes 
        number of permutations: 4*2*2 = 16
    '''

    for rot_amount in range(0,4):
        for flip_vert in [False, True]:
            for flip_hor in [False, True]:
                # rotate the matrix
                temp = np.rot90(grid, k=rot_amount)
                # flip vertically
                if flip_vert == True:
                    temp = np.flipud(temp)
                else: 
                    pass
                # flip horizontally
                if flip_hor == True:
                    temp = np.fliplr(temp)
                else:
                    pass
                yield temp


def decompose_grid(grid, size_subgrid):
    ''' Decomposes the a square grid into square sub-grids of 
        size 'size_subgrid'. Returns a generator object.
    '''

    size = len(grid)
    n_subgrids = size//size_subgrid

    for i in range(n_subgrids):
        for j in range(n_subgrids):
            x_start = size_subgrid*i 
            x_end = x_start + size_subgrid
            y_start = size_subgrid*j
            y_end = y_start + size_subgrid
            yield grid[x_start:x_end, y_start:y_end]


def enhance_subgrid(subgrid, input_pattern, output_pattern):
    ''' Applies the enhancement rule to a sub-grid. The function matches
        the sub-grid with an input pattern and then returns the corresponding 
        output pattern.
    '''

    for key in sorted(input_pattern.keys()):
        pattern = input_pattern[key]
        # the matching pattern must have the same size as the subgrid
        if len(subgrid) != len(pattern):
            continue
        else:
            pass
        # to have a match we need the same number of ones and zeros
        if subgrid.sum() != pattern.sum():
            continue
        else:
            pass
        for pattern in grid_permutations(pattern):
            if np.array_equal(subgrid, pattern) == True:
                return output_pattern[key]
            else:
                continue

    raise Exception('no rule exists for this pattern')


def enhance_subgrids(grid, subgrid_gen, input_pattern, output_pattern):
    ''' Applies the enhancement rule to all the sub-grids. Returns a generator
        with the enhanced sub-grids.
    '''

    for subgrid in subgrid_gen:
        yield enhance_subgrid(subgrid, input_pattern, output_pattern)
        

def enhance_grid(grid, input_pattern, output_pattern):
    ''' Performs one enhancement iteration on a grid. The grid is broken up
        into 2x2 squares or 3x3 squares. Then an enhancement rule is applied
        to each square and the results are recomposed to form a new grid.
    '''

    size = len(grid)
    if size % 2 == 0:
        size_subgrid = 2    # 2x2 squares
    elif size % 3 == 0:
        size_subgrid = 3    # 3x3 squares
    else:
        raise Exception('size not divisible by two nor by three')

    # split the grid into sub-grids (return as generator)
    subgrid_gen = decompose_grid(grid, size_subgrid)
    # enhance each of the sub-grids (return as generator)
    enhanced_gen = enhance_subgrids(grid, subgrid_gen, input_pattern, output_pattern)

    subgrids_per_dim = size // size_subgrid     # subgrids per dimension
    size_subgrid += 1                           # 2x2 -> 3x3, 3x3 -> 4x4
    size = size_subgrid * subgrids_per_dim
    grid = np.zeros((size, size), dtype='int')  # initialize as array of zeroes

    for i in range(subgrids_per_dim):
        for j in range(subgrids_per_dim):
            x_start = size_subgrid*i 
            x_end = x_start + size_subgrid
            y_start = size_subgrid*j
            y_end = y_start + size_subgrid

            grid[x_start:x_end, y_start:y_end] = next(enhanced_gen)

    return grid


def main():

    input_pattern, output_pattern = read_data('../input/input_day21.txt')

    grid = np.array([[0,1,0],[0,0,1],[1,1,1]])
    n_iterations = 5

    for i in range(n_iterations):
        grid = enhance_grid(grid, input_pattern, output_pattern)
        logging.debug(f'Progress: {i+1:2}/{n_iterations}')

    pixels_on = grid.sum()
    print(f'Number of pixels that are "ON" after {n_iterations} iterations: {pixels_on}')


if __name__ == '__main__':
    main()