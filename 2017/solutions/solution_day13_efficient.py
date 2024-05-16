import logging

logging.basicConfig(level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s: %(message)s')
logging.disable(logging.CRITICAL)

def read_data(filename):

    with open(filename) as f:
        data = f.read().strip().split('\n')

    firewall = dict()
    for row in data:
        depth, layer_range = map(int, row.split(': '))
        firewall[depth] = layer_range
    return firewall

def calculate_severity(firewall, start_delay=0, break_when_detected=False):
    """ Calculates the severity of the trip through the firewall 

        Given the range of the scanner, the period of the scanner is (2*range-2)
        Do not simulate the trip through the firewall (very slow for part 2)
        
        Only need to check whether the scanner is at position 0.
        We do not care when it is anywhere else in the range.

        :param firewall: a dictionary with the layer info {depth:range}
        :param start_delay: how many picoseconds to wait before starting the trip
        :param break_when_detected: decides if the calculation stops when we are detected by a scanner 

        :return severity: the total severity of the trip
        :return caught: True if caught by the scanner in at least one layer, False otherwise

    """

    severity = 0
    caught = False

    for t in firewall.keys():
        if (t + start_delay) % (firewall[t]*2 - 2) == 0:
            severity += t * firewall[t]
            caught = True
            if break_when_detected:
                break

    return severity, caught

def main():
    
    firewall = read_data('../input/input_day13.txt')
    severity, caught = calculate_severity(firewall)
    print(f'Start immediately: (severity={severity}, caught={caught})')

    delay = 0
    while True:
        delay += 1
        severity, caught = calculate_severity(
            firewall, start_delay=delay, break_when_detected=True)
        if caught == False:
            break
    print(f'Delay {delay} picosec: (severity={severity}, caught={caught})')
    
if __name__ == '__main__':
    main()