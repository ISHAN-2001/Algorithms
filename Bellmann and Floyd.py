import sys
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

# Code from here
# 1. Bellmann Ford (DP)
# Used to find path if distances are -ve

# let edge be (source,dest,weight) , no of nodes =n 

def Bellmann(edges,n):

	dist = [float('inf')]*(n)

	source=0

	dist[source]=0

	for i in range(n):

		stop=1

		for src,dest,weight in edges:

			if dist[dest]>dist[src]+weight:
				dist[dest]=dist[src]+weight
				stop=0

		if stop:
			break

	# if one dist is -ve then -ve cycle is present
	print(dist) # shortest distance


# 2.Floyd Warshall(DP)
# all pairs shortest path
# prepare dist matrix dist[i][j] dist between i and j nodes
# n is no. of nodes

def Floyd(dist,n):

	for i in range(n):

		for j in range(n):

			for k in range(n):

				dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])

	return dist

