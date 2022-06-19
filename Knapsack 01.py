import sys
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

# Code from here
def main():
	val=[20,5,10,40,15,25]
	weight =[1,2,3,8,7,4]  

	n=6; W=10

	dp=[[0 for _ in range(0,11)] for _ in range(0,7)]
	
	for i in range(1,7):
		for j in range(1,11):

			if(weight[i-1]<=j):
				dp[i][j]= max(val[i-1]+dp[i-1][j-weight[i-1]], dp[i-1][j])

			else:
				dp[i][j]=dp[i-1][j]
				
	print(dp[6][10])

if __name__ == "__main__":
	main()