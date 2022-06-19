import sys
from collections import Counter  #hashmap in python
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

# Start coding..

# Counting frequency of elements  
s= "abcabbbcd"

cntr = Counter(s)

print(cntr)

"""
Counter({'b': 4, 'a': 2, 'c': 2, 'd': 1})

"""

for i in cntr:
    print(i,"-->",cntr[i])

"""
a --> 2
b --> 4
c --> 2
d --> 1
"""


print("---------------")


a=[1,2,1,1,4,6,2,4]  # Valid on a=["car","bus","car"]

cntr1 = Counter(a)

print(cntr1)  # Counter({1: 3, 2: 2, 4: 2, 6: 1})


for i in cntr1:
    print(i,"-->",cntr1[i])

"""
1 --> 3
2 --> 2
4 --> 2
6 --> 1
"""

