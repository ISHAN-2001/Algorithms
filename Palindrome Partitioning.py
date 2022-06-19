import sys
from collections import defaultdict
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

#Code from here
class Solution(object):

	def Solution(self, s):
		self.s =s
		self.n = len(s)
		n = self.n
		self.dp = [[-1 for _ in range(n)] for _ in range(n)]


		print(self.partition(0,self.n-1))


	def partition(self,i,j):
		n= self.n
		

		if(self.dp[i][j] != -1):
			return self.dp[i][j]

		if(i>=j):             # i>j is invalid and i==j is 0 partition
			self.dp[i][j] = 0
			return 0

		s= self.s[i:j+1]

		if(s==s[::-1]):      # if substring is palindrome then 0 partition
			self.dp[i][j] = 0
			return 0

		ans = 1000000

		for k in range(i,j):  # dp formula.. 

			tempans = 1+ self.partition(i,k)+self.partition(k+1,j)
			ans= min(ans,tempans)
	

		return ans


if __name__ == "__main__":
 
	s= "nititkl"
	a=Solution()
	ans=a.Solution(s)
	#print(ans)
