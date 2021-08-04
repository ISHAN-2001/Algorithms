import sys
from collections import defaultdict
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

# Start coding...
def Solution(edges):
	graph = defaultdict(list)

	for edge in edges:
		"""x=edge[0]
		y=edge[1]"""
		x,y =edge
		graph[x].append(y)
		graph[y].append(x)

	l= len(graph)
	for vertice in graph:
		if(len(graph[vertice])==l-1):
			print(vertice)

if __name__ == '__main__':
	edges=[[1,2],[2,3],[4,2]]
	Solution(edges)


