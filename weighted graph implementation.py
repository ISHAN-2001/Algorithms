import sys
from collections import defaultdict
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

# Code from here
# Shortest path from source src to all other vertices..
# All edges have lenght 1
# BFS approach is used here
class Solution(object):
	def Dir(self,n,e,graph):

		for v1 in graph:
			for v2,d in graph[v1]:
				print("{} -> {} = {}".format(v1,v2,d))


if __name__ == "__main__":

	n, e = map(int, input().split()) # n is no of vertices and e is no of edges
	graph = defaultdict(list)        # adjacency list

	for _ in range(e):
		v1 ,v2 ,d =map(int,input().split())
		graph[v1].append((v2,d))
		graph[v2].append((v1,d))

	# main(n,e,graph)
	a=Solution()
	a.Dir(n,e,graph)

	

""" 
Input are provided as :-

7 6 (n and e)
1 2 (e edges)
1 5
2 3
2 4
5 6
5 7

1
|___2
|	|___3
|	|___4
|
|___5
	|___6
	|___7

or

9 10
1 2
2 3
3 4
4 5
3 6
6 5
7 2
7 8 
8 9
7 9
"""
	
