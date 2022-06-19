import sys
from collections import defaultdict
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

#Code from here
class Solution(object):

	def LIS(self,arr):  # Longest Increasing subsequence
		n= len(arr)
		maximum = 1
		lis = [1]*(n)
		cnt= defaultdict(int)
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






if __name__ == "__main__":

	arr =[1,3,5,4,7]
	a=Solution()
	ans=a.LIS(arr)
	print(ans)