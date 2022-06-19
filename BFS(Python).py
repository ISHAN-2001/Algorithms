import sys
from collections import defaultdict
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

# Code from here

class Solution(object):

	def BFS(self,n,e,graph):
		vis= [0]*(n+1)
		
		queue = []
		queue.append(1)

		vis[1]=1

		while queue:
			v=queue.pop(0)
			print(v,end=" ")

			for i in graph[v]:
				if(vis[i]==0):
					queue.append(i)
					vis[i]=1


if __name__ == "__main__":
 
	n, e = map(int, input().split()) # n is no of vertices and e is no of edges
	graph = defaultdict(list)        # adjacency list

	for _ in range(e):
		v1 ,v2 =map(int,input().split())
		graph[v1].append(v2)
		graph[v2].append(v1)

	# main(n,e,graph)
	a=Solution()
	a.BFS(n,e,graph)


""" 
Input are provided as :-

7 6 (n and e)
1 2 (e edges)
1 5
2 3
2 4
5 6
5 7
"""
	

