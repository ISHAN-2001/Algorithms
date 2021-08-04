import sys
from collections import defaultdict
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

#Code from here
class Solution(object):

	def findBridge(self,n,e,graph):
		self.graph = graph
		self.vis = [0]*(n+1)
		self.low = [0]*(n+1)
		self.discovered = [0]*(n+1)
		self.timer =1
		self.flag =False

		for i in range(1,n+1):
			if(self.vis[i]==False):
				self.dfs(i,-1) 

		if(self.flag==False):
			print("No bridges") 


	def dfs(self,vertex,parent):
		self.vis[vertex]=1
		self.low[vertex] = self.discovered[vertex] = self.timer
		self.timer+=1

		for node in graph[vertex]:
			if(node == parent):
				continue

			if(self.vis[node]==0):

				self.dfs(node,vertex)
				self.low[vertex] = min(self.low[vertex],self.low[node])

				if(self.low[node]> self.discovered[vertex]): 
				 # Main Condition for bridge
					print("{}--{}".format(node,vertex))
					self.flag = True

			else:      
				# this node cannot be a bridge
				self.low[vertex] = min(self.low[vertex],self.discovered[node])
  

if __name__ == "__main__":

	n,e = map(int,input().split())
	graph = defaultdict(list)

	for _ in range(e):
		v1,v2 = map(int,input().split())
		graph[v1].append(v2)
		graph[v2].append(v1)

	a = Solution()
	a.findBridge(n,e,graph)



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
