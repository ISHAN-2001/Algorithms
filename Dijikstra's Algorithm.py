import sys
from collections import defaultdict
import heapq
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

#Code from here
class Solution(object):

	def Dijikstra(self,n,e,graph):
		dist = [100000]*(n+1)
		src = 1
		dist[src] =0 

		pq =[]                      # A priority queue
		pq.append((dist[src],src))
		heapq.heapify(pq)

		while pq:
			distvertex , vertex = heapq.heappop(pq)

			for node, edgeweight in graph[vertex]:

				if(dist[node] > dist[vertex]+edgeweight):
					dist[node] =dist[vertex] + edgeweight
					heapq.heappush(pq,(dist[node],node))

		print(dist[1:])


if __name__ == "__main__":

	n, e = map(int, input().split()) # n is no of vertices and e is no of edges d EdgeWeight
	graph = defaultdict(list)        # adjacency list

	for _ in range(e):
		v1 ,v2 ,d =map(int,input().split())
		graph[v1].append((v2,d))
		graph[v2].append((v1,d))

	# main(n,e,graph)
	a=Solution()
	a.Dijikstra(n,e,graph)


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
