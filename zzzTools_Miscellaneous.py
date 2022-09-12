import sys 
import bisect
from functools import cmp_to_key
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

#Code from here..

#1.Binary Search...

#sort list
l=[0,1,1,2,2,4,5,6]
x=2
print(bisect.bisect_left(l, x)) 
# returns smallest index so that x in inserting list remains sorted similarly...
print(bisect.bisect_right(l,x)) #largest index


###################################################################################33


#2.Comparator func for comparing tuples, objects
def cmp(a,b):

	if a[0]<b[0]: #first<second
		return -1 #-1 = first pos

	elif a[0]>b[0]:
		return 1 #1 = second pos

	elif a[1]>b[1]:
		return -1 #first pos

	else:
		return 1 #second pos

arr = [(7,8),(7,10),(1,3),(2,5),(1,6),(4,5),(4,3)]

#Requirement first element ascending second element descending
arr2 =sorted(arr,key=cmp_to_key(cmp))
print(arr2)