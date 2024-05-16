import logging
from collections import defaultdict
from tqdm import tqdm

logging.basicConfig(level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s: %(message)s')

class StateMachine():

    def __init__(self, initial_state='A'):

        self.tape = defaultdict(int)
        self.state = initial_state
        self.cursor_pos = 0

    def execute(self):
        ''' Performs one execution of the state machine. '''

        if self.state == 'A':

            if self.tape[self.cursor_pos] == 0:
                self.tape[self.cursor_pos] = 1
                self.cursor_pos += 1
                self.state = 'B'

            else:
                self.tape[self.cursor_pos] = 0
                self.cursor_pos -= 1
                self.state = 'C'

        elif self.state == 'B':

            if self.tape[self.cursor_pos] == 0:
                self.tape[self.cursor_pos] = 1
                self.cursor_pos -= 1
                self.state = 'A'
            else:
                self.tape[self.cursor_pos] = 1
                self.cursor_pos -= 1
                self.state = 'D'

        elif self.state == 'C':

            if self.tape[self.cursor_pos] == 0:
                self.tape[self.cursor_pos] = 1
                self.cursor_pos += 1
                self.state = 'D'
            else:
                self.tape[self.cursor_pos] = 0
                self.cursor_pos += 1
                self.state = 'C'

        elif self.state == 'D':

            if self.tape[self.cursor_pos] == 0:
                self.tape[self.cursor_pos] = 0
                self.cursor_pos -= 1
                self.state = 'B'
            else:
                self.tape[self.cursor_pos] = 0
                self.cursor_pos += 1
                self.state = 'E'

        elif self.state == 'E':

            if self.tape[self.cursor_pos] == 0:
                self.tape[self.cursor_pos] = 1
                self.cursor_pos += 1
                self.state = 'C'
            else:
                self.tape[self.cursor_pos] = 1
                self.cursor_pos -= 1
                self.state = 'F'

        elif self.state == 'F':

            if self.tape[self.cursor_pos] == 0:
                self.tape[self.cursor_pos] = 1
                self.cursor_pos -= 1
                self.state = 'E'
            else:
                self.tape[self.cursor_pos] = 1
                self.cursor_pos += 1
                self.state = 'A'

        else:

            raise Exception('invalid state')

def main():

    n_steps = 12172063
    machine = StateMachine()

    # execute the state machine for a number of steps
    for i in tqdm(range(n_steps)):
        machine.execute()
    
    print(f'The diagnostic checksum is {sum(machine.tape.values())}.')

if __name__ == '__main__':
    main()
    