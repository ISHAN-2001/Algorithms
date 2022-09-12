import sys
import bisect
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

#Code from here
class Solution(object):

	def LIS(self,arr):  # Longest Increasing subsequence
		n= len(arr)
		maximum = 1
		lis = [1]*(n)
		cnt[1] =1

		for i in range(1,n):

			for j in range(0,i):

				if(arr[i]>arr[j] and lis[i]<=lis[j]):

					lis[i] = 1+lis[j]
					maximum = max(maximum,lis[i])



		ans = 1
		print(lis)
	
		i = n-1
		s=''
		while(maximum >0):

			if(lis[i]==maximum):
				s+= str(arr[i])
				maximum-=1
			i-=1

		return s[::-1]

	def solve2(self,nums): #Binary Search (Recommended)

		n = len(nums)
		lcs = [nums[0]]

		for i in range(1,n):

			if nums[i]>lcs[-1]:
				lcs.append(nums[i])

			else:
				ind = bisect.bisect_left(lcs, nums[i])
				lcs[ind] =nums[i]

		return len(lcs)





if __name__ == "__main__":

	arr =[1,3,5,4,7]
	a=Solution()
	ans=a.LIS(arr)
	print(ans)