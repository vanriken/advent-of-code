import logging
import re
import numpy as np
from collections import Counter
from collections import defaultdict

logging.basicConfig(level=logging.DEBUG, 
	format='%(asctime)s - %(levelname)s: %(message)s')
logging.disable(logging.CRITICAL)

def read_data(filepath):
	""" Reads the input data and returns three arrays that contain
		the positions, velocities, and accelerations of the points.

		Rows: particle
		Columns: dimension (x,y,z)
	"""

	with open(filepath) as f: 
		data = f.read().strip().split('\n')

	n_particles = len(data)
	pos = np.zeros((n_particles, 3))
	vel = np.zeros((n_particles, 3))
	acc = np.zeros((n_particles, 3))

	for i in range(n_particles):
		line = data[i]
		matches = re.findall(r'-?\d+', line)
		pos[i,:] = [int(matches[j]) for j in range(3)]
		vel[i,:] = [int(matches[j]) for j in range(3,6)]
		acc[i,:] = [int(matches[j]) for j in range(6,9)]

	return pos, vel, acc, n_particles

def main():

	pos, vel, acc, n_particles = read_data('../input/input_day20.txt')

	# ------------------------- PART 1 ------------------------------
	# no need to simulate the particle movements
	# 
	# position as function of time: 
	# p = x0 + v0*t + 0.5*a*t^2 
	# for large t the last term will dominate: p ~= 0.5*a*t^2
	# manhattan distance is abs(px) + abs(py) + abs(pz)
	# particle with smallest manhattan distance in the long term is
	# argmin(abs(ax) + abs(ay) + abs(az))
	# ---------------------------------------------------------------

	sum_abs_acc = np.sum(abs(acc), axis=1)
	idx_closest = np.argmin(sum_abs_acc)

	print(f'Particle {idx_closest} will stay closest to <0,0,0> in the long term.')
	print(f'Particle {idx_closest} acceleration values: {acc[idx_closest]}.\n')

	# ------------------------- PART 2 ------------------------------
	# particles that collide are removed
	# more than two particles can collide
	# ---------------------------------------------------------------

	active_particles = list(range(n_particles))

	for i in range(1001):
		
		# key: position, value: particles at this position
		positions = defaultdict(list)

		# loop through active particles and fill the dict
		for j in active_particles:
			positions[tuple(pos[j,:])].append(j)

		# collision when two or more particles are at the same position
		for lst in positions.values():
			if len(lst) > 1: 
				for particle_id in lst: 
					active_particles.remove(particle_id)

		# increase the velocity by the acceleration
		vel = vel + acc
		# increase the position by the velocity
		pos = pos + vel

		logging.debug(f'Step {i}: {len(active_particles)} particles remaining.')

	print(f'After {i} steps, {len(active_particles)} particles are left.\n')

if __name__ == '__main__':
	logging.debug('Program Started')
	main()
	logging.debug('Program Ended')