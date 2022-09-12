import sys 
from collections import deque
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

#Code from here
# leetcode jump game 3 solutions...
# https://leetcode.com/problems/jump-game-ii/
class Solution(object):

	def solve(self,n,arr,ind=0): #recursive/dfs solution

		if ind==n-1:
			return 0

		if arr[ind]==0:
			return float('inf')

		minis = float('inf')

		for i in range(1,arr[ind]+1):

			if ind+i>=n:
				continue

			minis = min(minis, 1+ self.solve(n,arr,ind+i))

		return minis

	def solve1(self,n,arr): #dynamic programming


		dp = [float('inf')]*(n)
		dp[n-1]=0
		
		for i in range(n-2,-1,-1):

			if arr[i]==0:
				continue

			for j in range(1,arr[i]+1):

				if i+j>=n:
					continue

				dp[i] = min(dp[i], 1+dp[i+j])

		return dp[0]

	def solve2(self,n,arr): #bfs

		q= deque([0])

		level =1 

		vis = [-1]*(n)

		while q:

			qlen = len(q)

			for i in range(qlen):

				ind = q.popleft()

				if vis[ind] !=-1:
					continue 

				vis[ind]=level

				for j in range(1,arr[ind]+1):

					if ind+j==n-1:
						return level

					if ind+j<n:
						q.append(ind+j)

			level+=1


		return -1


if __name__ == "__main__":

	arr = [1,4,3,2,6,7]
	n = len(arr)

	print(Solution().solve2(n,arr))