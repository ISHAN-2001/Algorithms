import sys
from collections import defaultdict
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

#Code from here
class Solution(object):

	def solve(self,n):

		self.n =n 

		self.ans = []

		self.backtrack(1,[],n)

		return self.ans  # (x,y) x-cordinate and y-cordinate

	def backtrack(self,no,path,n):  # no is row number y-cordinate

		if(no>n):

			self.ans.append(path)
			return

		for x in range(1,n+1):

			if not path:

				self.backtrack(no+1,path+[(x,no)],n)
				continue

			safe_x=-1

			for xpos,ypos in path:

				if(xpos==x):
					safe_x=-1
					break

				elif(ypos==no):
					safe_x=-1
					break

				elif(abs(xpos-x)==abs(ypos-no)):
					safe_x=-1
					break

				else:
					safe_x=x  

			if(safe_x!=-1):

				self.backtrack(no+1,path+[(safe_x,no)],n)


if __name__ == "__main__":

	n=5
	a=Solution()
	ans=a.solve(n)
	print(ans)
    