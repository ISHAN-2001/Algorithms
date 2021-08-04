import sys
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

# Code from here
def main():
	arr = [2,3,5,1,6,4]
	sum=11 ; n=6
	dp =[[0 for _ in range(sum+1)] for _ in range(n+1)]

	for i in range(n+1):
		dp[i][0] = 1
	
	for i in range(1,n+1):
		for j in range(1,sum+1):
			if(arr[i-1]<=j):
				dp[i][j]=dp[i-1][j-arr[i-1]] + dp[i-1][j]
			else:
				dp[i][j] = dp[i-1][j]

	for i in range(n+1):
		print(dp[i])

if __name__ == "__main__":
	main()
