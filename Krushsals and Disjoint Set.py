import sys
from collections import defaultdict
import heapq
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

#Code from here
class Solution(object):
	def Krushkals(self,n,e,edges):

		edges.sort()
		self.n = n
		self.e = e
		self.edges = edges

		self.rank =[0]*(n+1)
		self.parent = [0]*(n+1)
		mst=[]
		cost =0
 
		for i in range(1,n+1):     # Make set
			self.parent[i] = i

		for d,v1,v2 in edges:
			
			if(self.findparent(v1) != self.findparent(v2)):
				cost+=d
				self.Union(v1,v2)
				mst.append((d,v1,v2))
  
		print(cost)
		for d,v1,v2 in mst:
			print(v1,v2)


	def findparent(self,v):
		if(self.parent[v] == v):
			return v

		else:
			self.parent[v] = self.findparent(self.parent[v])
			return self.parent[v]

	def Union(self,v1,v2):
		v1 =self.findparent(v1)
		v2 = self.findparent(v2)

		if(self.rank[v1] < self.rank [v2]):
			self.parent[v1] = v2

		elif(self.rank[v2] < self.rank[v1]):
			self.parent[v2] = v1

		else:
			self.parent[v1]=v2
			self.rank[v2]+=1



if __name__ == "__main__":

	n, e = map(int, input().split()) # n is no of vertices and e is no of edges d EdgeWeight
	edges =[]   # Edges list

	for _ in range(e):
		v1 ,v2 ,d =map(int,input().split())
		edges.append((d,v1,v2))

			# main(n,e,graph)
	#edges.sort()
	a=Solution()
	a.Krushkals(n,e,edges)


"""
Inputs :-
5 6
1 2 2
1 4 1
2 3 4
4 3 3
2 5 5
5 3 1


"""
