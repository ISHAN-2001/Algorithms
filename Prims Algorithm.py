import sys
from collections import defaultdict
import heapq
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

#Code from here
class Solution(object):

	def Prims(self,n,e,graph):
		key =[10**8]*(n+1)
		mst = [False ]*(n+1)
		parent = [-1]*(n+1)

		pq = []
		src =1
		pq.append((0,src))
		heapq.heapify(pq)

		while pq:

			dist1 , vertex = heapq.heappop(pq)

			mst[vertex] =True

			for node , weight in graph[vertex]:

				if(mst[node] == False and weight < key[node]):
					parent[node] =vertex
					key[node] =weight
					heapq.heappush(pq,(key[node],node))

		sum1 =0
		for node1,node2 in enumerate(parent):
			if(node2==-1):
				continue
			print("{}--{} -->{}".format(node2,node1,key[node1]))
			sum1+=key[node1]

		print("Sum =",sum1)



if __name__ == "__main__":

	n, e = map(int, input().split()) # n is no of vertices and e is no of edges d EdgeWeight
	graph = defaultdict(list)        # adjacency list

	for _ in range(e):
		v1 ,v2 ,d =map(int,input().split())
		graph[v1].append((v2,d))
		graph[v2].append((v1,d))

	# main(n,e,graph)
	a=Solution()
	a.Prims(n,e,graph)


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
