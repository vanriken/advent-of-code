import logging
from functools import reduce
from operator import xor
import numpy as np 
import networkx as nx

logging.basicConfig(level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s: %(message)s')
#logging.disable(logging.CRITICAL)

def shift_lst(lst, shift_amount):
    """ Rotates a list an arbitrary number of items to the left. """

    for _ in range(shift_amount):
        lst.append(lst.pop(0))

def reverse_sublist(lst, start_idx, end_idx):
    """ Reverses the sublist starting at start_idx and ending at end_idx """
    
    if start_idx < end_idx:
        
        lst[start_idx:end_idx] = lst[start_idx:end_idx][::-1]
    
    else:
        
        # shift left until list is [... START ... END]
        shift_amount = end_idx
        shift_lst(lst,shift_amount)

        # reverse the elements of the sublist
        lst[((start_idx - shift_amount) % len(lst)):] = \
            lst[((start_idx - shift_amount) % len(lst)):][::-1]
        
        # shift left to undo the first shift
        shift_amount = len(lst) - shift_amount
        shift_lst(lst,shift_amount)

def execute_knot_hash_round(lst, lengths, current_pos=0, skip_size=0):
    """ Executes one round of the knot hash algorithm

    :param lst: a list of numbers (modified by the function)
    :param length: a sequence of lengths used for knot hashing
    :param current_pos: start position on the list (default:0)
    :param skip_size: number of numbers skipped after each iteration (default:0)

    :return current_pos: the position after the hashing round has been completed
    :return skip_size: the value of skip_size after the hashing round has been completed 

    """

    for length in lengths:
        
        if length != 0:

            start_idx = current_pos % len(lst)
            end_idx = (start_idx + length) % len(lst)
            reverse_sublist(lst, start_idx, end_idx)

        else:
            # do nothing, the list stays as it is
            pass

        current_pos = (current_pos + length + skip_size) % len(lst)
        skip_size += 1

    return (current_pos, skip_size)

def compute_dense_hash(sparse_hash, block_size=16):
    """ Reduces the sparse hash of the knot hash algorithm to a dense hash 
        
        :param sparse_hash: the sparse hash that is initially computed by the knot hash algorithm
        :param block_size: the block size that is used to reduce the sparse hash to the dense hash
        :return dense_hash: the dense hash after xor reduction
    """ 

    dense_hash = []

    for i in range(0,len(sparse_hash), block_size):
        sublist = sparse_hash[i:i+block_size]
        xor_result = reduce(xor, sublist)
        dense_hash.append(xor_result)

    return dense_hash

def get_hex_string(dense_hash):
    """ Returns the hex-string representation of the dense hash """

    hex_string = ''
    for number in dense_hash:
        hex_string += hex(number).split('x')[1].zfill(2)

    return hex_string

def knot_hash(key, n_rounds=64, binary_output=False):
    """ Computes the knot hash for a given string  

        :param key: a string on which the knot hash is computed
        :param n_rounds: specifies the number of rounds in the hashing process
        :return hashed: the knot hash of the input
    """
    
    lst = [i for i in range(256)]
    lengths = list(map(ord, key)) + [17,31,73,47,23]
    current_pos = 0
    skip_size = 0 

    for _ in range(n_rounds):
        current_pos, skip_size = execute_knot_hash_round(lst, lengths, current_pos, skip_size)
    dense_hash = compute_dense_hash(lst)
    
    # get the hex representation of the hash
    hashed = get_hex_string(dense_hash)

    # get the binary representation of the hash
    if binary_output == True:
        hashed = bin(int(hashed, 16))[2:].zfill(128)

    return hashed

def manhattan_distance(p1, p2):

    x1, y1 = p1
    x2, y2 = p2 
    return abs(x1-x2) + abs(y1-y2)


def main():

    height, width = 128, 128
    key = 'ugkiagan'
    disk = np.zeros((height, width))

    for row in range(height):
        hash_input = key + '-' + str(row)
        hashed_bin = knot_hash(hash_input, binary_output=True)
        disk[row,:] = list(hashed_bin)
    
    # create a dictionary to store the coordinates of the used squares
    # use row-major order for the elements row * width + col
    coordinates = dict()
    for row in range(height):
        for col in range(width):
            if disk[row,col] == 1: 
                coordinates[row*width + col] = (row, col)

    print(f'Number of used squares: {len(coordinates)}')

    # create a graph
    G = nx.Graph()
    sorted_squares = sorted(coordinates.keys())

    # add the nodes to the graph
    for square_id in sorted_squares:
        G.add_node(square_id)

    logging.debug(G)

    # add the edges to the graph
    for square_id1 in sorted_squares:
        p1 = coordinates[square_id1]
        for square_id2 in sorted_squares:
            if square_id2 < square_id1:
                p2 = coordinates[square_id2]
                if manhattan_distance(p1,p2) == 1:
                    G.add_edge(square_id1, square_id2)
            else:
                break

    logging.debug(G)

    # get the number of connected components
    print(f'Number of regions in the disk: {len(list(nx.connected_components(G)))}')

if __name__ == '__main__':
    main()