import sys
from collections import defaultdict
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

# Code from here
# Detecting Cycle in directed graph using DFS

class Solution(object):
	def Cycle(self,n,e,graph):
		self.vis = [0]*(n+1)
		self.dfsvis = [0]*(n+1)
		self.graph = graph
		self.n= n
		self.e =e 

		for i in range(1,n+1):
			
			if(self.DFS(i)==True):
				return True

		return False

	def DFS(self,v):

		self.vis[v]=1
		self.dfsvis[v]=1

		for node in graph[v]:

			if(self.vis[node]==0):

				if(self.DFS(node)==True):
					return True

			elif(self.dfsvis[node]==1):# Condition:- vis[node]=1 and dfsvis[node] =1
				return True

		self.dfsvis[v] =0 
		return False


if __name__ == "__main__":

	n, e = map(int, input().split()) # n is no of vertices and e is no of edges
	graph = defaultdict(list)        # adjacency list

	for _ in range(e):
		v1 ,v2 =map(int,input().split()) #v1-> Source v2->Destination
		graph[v1].append(v2)             

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
	
