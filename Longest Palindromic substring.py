import sys
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

# Code from here
def main(s):
	l=len(s)
	dp = [[False for _ in range(l)] for _ in range(l)]

	for i in range(l):     #len =1 is always palindrome
		dp[i][i]=True
	x=1;y=1

	for i in range(l-1):   # checking for len =2
		if(s[i]==s[i+1]):
			dp[i][i+1]=True
			x=i
			y=i+1

	for len1 in range(2,l):        #Checking for len>=3
		for i in range(l):

			if(i+len1 >=l):
				break

			if(s[i]==s[i+len1] and dp[i+1][i+len1-1]==True):   #Main condition
				dp[i][i+len1]=True
				if(len1>y-x):
					x=i
					y=i+len1

	print(s[x:y+1])   #x is starting and y is ending


	

if __name__ == "__main__":

	s = input()
	main(s)

