# useful python library for next time: https://github.com/networkx/networkx

import logging
from collections import defaultdict
import re

logging.basicConfig(level=logging.DEBUG, 
	format='%(asctime)s - %(levelname)s: %(message)s')
logging.disable(logging.CRITICAL)

class Graph():
	""" Graph data structure """

	def __init__(self, connections, directed=False):
		self._graph = defaultdict(set)
		self._directed = directed
		self.add_connections(connections)

	def __str__(self):
		string =  f'This is a graph with {len(self._graph.keys())} nodes.\n'
		string += f'{self._graph}'
		return string 

	def add_connections(self, connections):
		""" Add connections (list of tuple pairs) to graph. """

		for node1, node2 in connections:
			self.add(node1, node2)

	def add(self, node1, node2):
		""" Add connection between node1 and node2. """

		self._graph[node1].add(node2)
		if not self._directed:
			self._graph[node2].add(node1)

	def dfs(self, start_node, visited):
		
		""" Perform a depth-first search of the graph, given a starting node.
			Returns a list with all the nodes that can be reached from the starting node.
		"""

		if start_node not in visited:
			visited.add(start_node)
			for adj_node in self._graph[start_node]:
				self.dfs(adj_node, visited)
		return visited 

	def get_connected_components(self):

		""" Returns a list with all the connected components of the graph. """

		nodes = set(self._graph.keys())
		groups = []

		while len(nodes) > 0:
			node = list(nodes)[0]
			group = self.dfs(node, visited=set())
			
			nodes = nodes - group
			groups.append(group)

		return groups


def process_input(data):
	""" Processes the input list and returns a list that contains 
		all edges. This list can be used to create the graph.
	"""

	# convert input data to a list of tuples 
	edges = []

	connectionsRegex = re.compile(r'(\d+) <-> (.*)')
	for result in connectionsRegex.findall(data): 
		# the current programs
		program = int(result[0])
		# the programs that are directly connected
		adj_programs = list(map(int, result[1].split(', ')))

		for adj_program in adj_programs:
			edges.append((program, adj_program))

	return edges


def main():

	test_data = """
0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
	"""
	edges = process_input(test_data)
	programGraph = Graph(edges)	
	group_size = len(programGraph.dfs(0, visited=set()))
	connected_components = programGraph.get_connected_components()
	assert group_size == 6
	assert connected_components == [{0, 2, 3, 4, 5, 6}, {1}]


	with open('../input/input_day12.txt') as f:
		data = f.read()
	edges = process_input(data)
	programGraph = Graph(edges)
	group_size = len(programGraph.dfs(0, visited=set()))
	connected_components = programGraph.get_connected_components()
	print(f'Size of the group that contains program ID 0: {group_size}.')
	print(f'Number of connected components: {len(connected_components)}.')
	
if __name__ == '__main__':
	main()
