import sys
from collections import defaultdict
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

# Code from here

# This can be done using DFS/BFS.
# In Bipartite graphs no two adjacent nodes have same colour
# There are two colours :- 0 and 1

class Solution(object):

	def Bipartite(self,n,e,graph):
		self.colour= [-1]*(n+1)
		self.n = n
		self.e=e
		self.graph = graph

		for i in range(1,n+1):           # Do Bfs/Dfs for each connected component

			if(self.colour[i]==-1):  
				        
				if(self.BFS(i)==False):  # For Bfs
				 	return False

				"""
				self.colour[i]=0        # For DFS 
				if(self.DFS(i)==False):
						return False
				"""

		return True


	def BFS(self,n):
		queue= []
		queue.append(n)
		self.colour[n]=0

		while queue:
			v=queue.pop(0)

			for node in self.graph[v]:

				if(self.colour[node]==-1):  # If there is no colour then colour the node
					self.colour[node] = 1- self.colour[v]
					queue.append(node)
				elif(self.colour[node] + self.colour[v]==1): # check if nodes are of diffenrent colour
					continue
				else:             #nodes are of same colour
					return False

		return True         #No same colour adjacent nodes are found


	def DFS(self,v):

		for node in self.graph[v]:

			if(self.colour[node]==-1):           # If there is no colour then colour the node
				self.colour[node] = 1- self.colour[v]

				if(self.DFS(node) == False):
					return False

			elif(self.colour[node] + self.colour[v]==1): #opposite colour
				continue

			else:               #nodes are of same colour
				return False

		return True


if __name__ == "__main__":

	n, e = map(int, input().split()) # n is no of vertices and e is no of edges
	graph = defaultdict(list)        # adjacency list

	for _ in range(e):
		v1 ,v2 =map(int,input().split())
		graph[v1].append(v2)
		graph[v2].append(v1)

	# main(n,e,graph)
	a=Solution()
	print(a.Bipartite(n,e,graph))

	# For printing egdes along with colour of nodes 
	for i in graph:
		for j in graph[i]:
			if(i<=j):
				print("{}({}) --- {}({})".format(i,a.colour[i],j,a.colour[j]))


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
8 8
1 2
2 3
2 7
3 4
4 6
5 7
6 8
6 5
"""
	
