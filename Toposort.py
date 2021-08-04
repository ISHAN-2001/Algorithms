import sys
from collections import defaultdict
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

# Code from here
# Only applies in directed acyclic graph  
class Solution(object):
	def TopoSort(self,n,e,graph):
		#using dfs
		self.vis=[0]*n
		self.st =[]
		self.graph =graph

		for i in range(n):
			if(self.vis[i]==0):
				self.dfs(i)

		print(self.st[::-1])
		
  
	def dfs(self,v):
		self.vis[v] =1

		for node in self.graph[v]:
			if(self.vis[node]==0):
				self.dfs(node)

		self.st.append(v)


	def TopoSort1(self,n,e,graph):
		#This method uses BFS or (Kahn's Algorithm)
		queue = []
		indeg = [0]*n   # stores indegree of vertices
		ans =[]

		for node in graph:
			for v1 in graph[node]:
				indeg[v1]+=1

		for v in range(n):
			if(indeg[v]==0):
				queue.append(v)

		while queue:

			v= queue.pop(0)
			ans.append(v)
			for node in graph[v]:
				indeg[node]-=1
				if(indeg[node]==0):
					queue.append(node)

		print(ans)



if __name__ == "__main__":

	n, e = map(int, input().split()) # n is no of vertices and e is no of edges
	graph = defaultdict(list)        # adjacency list

	for _ in range(e):
		v1 ,v2 =map(int,input().split())
		graph[v1].append(v2)

	# main(n,e,graph)
	a=Solution()
	a.TopoSort(n,e,graph)

	

""" 
Input are provided as :-

6 6 
5 0
4 0
4 1
5 2
2 3
3 1
"""
	
