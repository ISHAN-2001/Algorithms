import sys
from collections import defaultdict
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

# Code from here
# Shortest path from source src to all other vertices..
# All edges have lenght 1
# BFS approach is used here
class Solution(object):
	def Dist(self,n,e,graph):
		dist =[100000]*(n+1)
		
		
		queue =[]
		src= 1
		dist[src]=0
		queue.append(src)

		while queue:
			v= queue.pop(0)
			for node in graph[v]:
				if(dist[v]+1<dist[node]):
					dist[node]=dist[v]+1
					queue.append(node)

		for i in range(1,n+1):
			print("{} -> {}".format(i,dist[i]))


if __name__ == "__main__":

	n, e = map(int, input().split()) # n is no of vertices and e is no of edges
	graph = defaultdict(list)        # adjacency list

	for _ in range(e):
		v1 ,v2 =map(int,input().split())
		graph[v1].append(v2)
		graph[v2].append(v1)

	# main(n,e,graph)
	a=Solution()
	a.Dist(n,e,graph)

	

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
