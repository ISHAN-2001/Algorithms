import sys
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

# Start coding...
n=int(input())
for i in range(1,n+1,2):
	a=(n-i)//2
	print(" "*a,"*"*i," "*a)
