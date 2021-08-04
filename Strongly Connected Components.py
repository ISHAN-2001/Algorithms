import sys
from collections import defaultdict
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

#Code from here
class Solution(object):

	def strongComponents(self,n,e,graph):
		self.graph  = graph
		self.vis = [0]*(n+1)
		self.stack = []


		for i in range(1,n+1):      #Topsort-like method
			if(self.vis[i]==0):
				self.TopoSort(i)

		self.stack = self.stack[::-1]
		#print(self.stack)

		self.g1 = self.transpose(graph)   # Transpose graph

		self.vis =[0]*(n+1)

		for i in self.stack:          # Final dfs and printing
			if(self.vis[i]==0):
				self.dfs(i)
				print("")


	def dfs(self,vertex):        # Can merge with toposort function

		self.vis[vertex] =1
		print(vertex,end=" ")

		for node in self.g1[vertex]:
			if(self.vis[node]==0):
				self.dfs(node)


	def TopoSort(self,vertex):
		self.vis[vertex]=1

		for node in self.graph[vertex]:
			if(self.vis[node]==0):
				self.TopoSort(node)


		self.stack.append(vertex)


	def transpose(self,graph):

		g1= defaultdict(list)

		for vertex in graph:
			for node in graph[vertex]:
				g1[node].append(vertex)


		return g1

	
  

if __name__ == "__main__":

	n,e = map(int,input().split())
	graph = defaultdict(list)

	for _ in range(e):
		v1,v2 = map(int,input().split())
		graph[v1].append(v2)

	a = Solution()
	a.strongComponents(n,e,graph)



"""
Inputs :-
5 5
1 2
2 3
3 1
2 4
4 5


"""
