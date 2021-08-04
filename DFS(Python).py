
import sys
from collections import defaultdict
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

# Code from here

"""def main(n,e,graph):
	
	vis=[0]*(n+1)

	def dfs(v):
		vis[v]=1                                #Function within Function Solution
		print(v,end=" ")
		for i in graph[v]:
			if(vis[i]==0):
				dfs(i)

	dfs(1)
"""

class Solution(object):

	def main(self,n,e,graph):
		self.graph= graph
		self.vis= [0]*(n+1)

		self.dfs(1)								# Class Solution (Recommended)

	def dfs(self,v):
			self.vis[v]=1
			print(v,end=" ")
			for i in self.graph[v]:
				if(self.vis[i]==0):
					self.dfs(i)


if __name__ == "__main__":

	n, e = map(int, input().split()) # n is no of vertices and e is no of edges
	graph = defaultdict(list)        # adjacency list

	for _ in range(e):
		v1 ,v2 =map(int,input().split())
		graph[v1].append(v2)
		graph[v2].append(v1)

	# main(n,e,graph)
	a=Solution()
	a.main(n,e,graph)


""" 
Input are provided as :-

7 6 (n and e)
1 2 (e edges)
1 5
2 3
2 4
5 6
5 7
(or)
1
|___2
|	|___3
|	|___4
|
|___5
	|___6
	|___7

Binary Tree...
"""
	

