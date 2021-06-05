import sys

"""
Call this program from a command line as

python3 check_Dijkstra_output input_file output_file [endpoint] [> path_file]

Reads the input and output to Dijkstra's algorithm.
First checks whether every vertex's parent is a valid parent.
With an optional given endpoint (index of a vertex), it finds a path backwards to the start,
and writes it to the standard output (which you can redirect to a file via > if you want).
Writes an error message to the console if something invalid is found.
"""

infinity = float('inf')

def main():
	input_stream_1 = sys.argv[1]
	input_stream_2 = sys.argv[2]
	output_stream = sys.stdout

	adj_list = []
	s = 0
	with open(input_stream_1) as f:
		adj_list, s = read_input(f)
	n = len(adj_list)
	
	edge_lengths = {}
	for u in range(n):
		for (v,l) in adj_list[u]:
			edge_lengths[(u,v)] = l
	
	d = n*[infinity]
	parent = n*[None]

	with open(input_stream_2) as f:
		d, parent = read_output(n, f)
	d[s] = 0 # Must be here since the above line overwrites it.

	for u in range(n):
		for (v,l) in adj_list[u]:
			if d[u] + l < d[v]:
				sys.stderr.write("d[{}] is too large\n".format(v))
	
	for v in range(n):
		if d[v] < infinity:
			u = parent[v]
			if None == u:
				if s == v:
					continue
				else:
					sys.stderr.write("{} has no parent.\n".format(v))
					return
			if (u,v) not in edge_lengths:
				sys.stderr.write("({},{}) does not seem to be an edge.\n".format(u,v))
				return
			l = edge_lengths[(u,v)]
			if not d[u] + l == d[v]:
				
				sys.stderr.write("Mismatch between {} and its parent.\n".format(v))
				sys.stderr.write("d[{}] = {}, d[{}] = {}, l = {}\n".format(v,d[v],u,d[u],l))
				return

	if len(sys.argv) < 4:
		return
	t = int(sys.argv[3])
	path = find_path(parent,s,t)
	
	for v in path:
		output_stream.write("{}\n".format(v))
		

def read_input(input_stream):
	# Returns the adjacency list.
	lines = input_stream.read().splitlines()
	n, m, s = [int(i) for i in lines[0].split()]
	edges = [[int(x) for x in line.split()] for line in lines[1:]]
	adj_list = [[] for foo in range(n)]
	for (u,v,l) in edges:
		adj_list[u].append((v, l))
	return adj_list, s


def read_output(n, input_stream):
	# n is the number of vertices, s is the start point.
	# Returns the arrays d, parent
	d = n*[infinity]
	parent = n*[None]
	lines = input_stream.read().splitlines()
	for line in lines:
		v, d1, p = [int(x) for x in line.split()]
		d[v] = d1
		parent[v] = p
	return d, parent


def find_path(parent,s,t):
	# Find the path to the destination t using the parent array.
	path = []
	
	u = parent[t]
	if None == u and s != t:
		sys.stderr.write("{} is unreachable.\n".format(t))
	v = t
	while None != v:
		path.append(v)
		v = parent[v]
		
	return path
	

if "__main__" == __name__:
	main()
