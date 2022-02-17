import logging

logging.basicConfig(level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s: %(message)s')

# global variables
max_strength = 0
max_strength_chain = []
max_length = 0
max_length_chain = []

def read_input(filepath):
    ''' Reads the text file and returns a list of available components. '''

    with open('../input/input_day24.txt') as f:
        lines = f.read().splitlines()

    components = []
    for line in lines:
        a,b = line.split('/')
        components.append((int(a),int(b)))

    return components


def can_append(component, chain):
    ''' Checks if a component can be appended to a chain. '''

    if chain == []:
        if component[0] == 0:
            return True
        else:
            return False
    else:
        # check: last element of chain equal to first element of component?
        if chain[-1][1] == component[0]:
            return True
        else:
            return False

def list_chains(chain, components):
    ''' This function uses recursion and backtracking to list all the possible
        bridges of components. It keeps track of the strongest bridge and it 
        also keeps track of the longest bridge that can be formed with the 
        given components.
    '''
    
    global max_strength
    global max_strength_chain
    global max_length
    global max_length_chain

    n_components = len(components)

    # for each component in the collection of components
    for i in range(n_components):

        component = components[i]

        for _ in range(2): # once for component, once for flipped component

            # check if the component can be added to the chain
            if can_append(component, chain):
                
                chain.append(component) # add component to the chain
                del components[i] # component has been used

                # get the strength and length of the chain
                strength = sum([sum(comp) for comp in chain])
                length = len(chain)
                # check if current chain is the strongest
                if strength > max_strength:
                    max_strength = strength
                    max_strength_chain = chain[:]
                else:
                    pass

                # check if current chain is the longest
                if length > max_length:
                    max_length = length
                    max_length_chain = chain[:]
                elif length == max_length:
                    # for chains with equal length, choose the strongest one
                    if strength > sum([sum(comp) for comp in max_length_chain]):
                        max_length_chain = chain[:]
                else:
                    pass

                list_chains(chain, components) # recursive call

                del chain[-1] # delete the last component from the chain
                components.insert(i, component) # make component available again

            # flip the component for the second iteration
            component = (component[1], component[0])

def main():
    
    global max_strength
    global max_strength_chain
    global max_length
    global max_length_chain

    components = read_input('../input/input_day24.txt')
    
    list_chains([], components)

    # print solution part 1
    m1 = f'The strongest bridge is {max_strength_chain}. '
    m1 += f'Strength: {max_strength}.\n'
    print(m1)

    # print solution part 2
    m2 = f'The longest bridge is {max_length_chain}. '
    m2 += f'Length: {max_length}. '
    m2 += f'Strength: {sum([sum(comp) for comp in max_length_chain])}.\n'
    print(m2)

if __name__ == '__main__':
    main()
    