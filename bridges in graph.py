import sys 
from collections import defaultdict,deque
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

#https://leetcode.com/problems/critical-connections-in-a-network/

#Code from here
class Solution(object):

	def solve(self,n,e,graph):

		self.time =0

		self.vis=[0]*(n+1)

		self.find =[float('inf')]*(n+1)

		self.dfs(1,-1) # or self.dfs(1,1) # own parent

	def dfs(self,vertex,parent):

		self.find[vertex]=self.time 
		self.time+=1
		self.vis[vertex]=1

		#1. Do dfs of unvisited
		for node in graph[vertex]:

			if self.vis[node]==0:
				self.dfs(node,vertex)


		#2. minimize find arr of a vertex by comparing all adjacent nodes
		#   exept parent
		for node in graph[vertex]:

			if node==parent:
				continue

			self.find[vertex]= min(self.find[vertex],self.find[node])

		# bridge condition '>' means no better path 
		if self.find[vertex]>self.find[parent]:       #self.find[-1] at F(1,-1) may break
			print("{}-->{}".format(vertex,parent))

		return


				
if __name__ == "__main__":

	n,e = map(int,input().split())
	graph = defaultdict(list)

	for _ in range(e):
		v1,v2 = map(int,input().split())
		graph[v1].append(v2)
		graph[v2].append(v1)

	a = Solution()
	a.solve(n,e,graph)



"""
Inputs :-
5 6
1 2 
1 4 
2 3 
4 3 
2 5 
5 3 


"""
