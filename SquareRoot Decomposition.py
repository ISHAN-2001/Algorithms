import sys 
from math import sqrt,ceil
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')


# Explanation :- https://leetcode.com/discuss/study-guide/2432715/tutorial-square-root-decomposition-dynamic-range-query
# Question :- https://leetcode.com/problems/range-sum-query-mutable/
#Code from here
class Solution(object):

	def sqrtdecomposition(self,nums):

		self.nums = nums
		self.n = len(nums)

		self.blocksize = ceil(sqrt(self.n))

		self.blocksum = [0]*(self.blocksize)

		blockind =-1

		for i in range(self.n):

			if i%self.blocksize==0:
				blockind+=1

			self.blocksum[blockind]+=nums[i]

		return

	def update(self,ind,newval):

		self.blocksum[ind//self.blocksize] += newval-self.nums[ind]

		self.nums[ind] = newval

		return


	def rangesum(self,left,right):

		ans =0

		while left<=right:

			# calculate sum of whole block and skip the block
			if(left%self.blocksize==0 and left+self.blocksize-1<=right):

				ans+=self.blocksum[left//self.blocksize]
				left+=self.blocksize

			# block cannot be skipped calculte individual elements
			else:
				ans+=self.nums[left]
				left+=1

		return ans

				
if __name__ == "__main__":

	nums = [0,1,2,3,4,5,6,7,8,9,10,11]

	obj = Solution()

	obj.sqrtdecomposition(nums)

	
	left = 2 ; right = 5
	ans = obj.rangesum(left,right)

	print(ans)

	index= 3 ; number = 40
	obj.update(index,number)

	left = 2 ; right = 9
	ans = obj.rangesum(left,right)

	print(ans)
