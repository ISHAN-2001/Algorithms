 import sys
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

# Code from here
def main(s1,s2):
	l1 = len(s1) ; l2 = len(s2)

	dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]

	for i in range(1,l1+1):
		for j in range(1,l2+1):

			if(s1[i-1]==s2[j-1]):
				dp[i][j]=1+dp[i-1][j-1]
			else:
				dp[i][j]= max(dp[i][j-1],dp[i-1][j])
				#dp[i][j] = 0 for subsstring


	#Printing LCS
	i= l1; j= l2
	ans= ""
	while(i>0 and j>0):

		if(s1[i-1]==s2[j-1]):
			ans= ans + s1[i-1]
			i=i-1
			j=j-1

		elif(dp[i][j-1]>dp[i-1][j]):
			j=j-1
		else:
			i=i-1

	print(ans[::-1])


	

if __name__ == "__main__":

	s = input()
	s1= input()
	main(s,s1)

