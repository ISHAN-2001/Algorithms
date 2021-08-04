import sys
from collections import defaultdict
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

# Code from here

class Solution(object):

	def Cycle(self,n,e,graph):
		self.vis= [0]*(n+1)
		self.n = n
		self.e=e
		self.graph = graph

		for vertex in range(1,n+1):

			if(self.vis[vertex]==0):

				if(self.dfs(vertex,-1)):
					return True

		return False

	def dfs(self,vertex,parent):
		self.vis[vertex]=1

		for node in self.graph[vertex]:

			if(self.vis[node]==0):

				if(self.dfs(node,vertex)):
					return True

			elif(node != parent):
				return True

		return False


if __name__ == "__main__":

	n, e = map(int, input().split()) # n is no of vertices and e is no of edges
	graph = defaultdict(list)        # adjacency list

	for _ in range(e):
		v1 ,v2 =map(int,input().split())
		
		graph[v1].append(v2)
		graph[v2].append(v1)

	# main(n,e,graph)
	a=Solution()
	print(a.Cycle(n,e,graph))


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
"""
	
