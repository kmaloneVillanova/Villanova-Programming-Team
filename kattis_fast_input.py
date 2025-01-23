# Use sys.stdin to read in input
# It is faster than input() and it allows us to read input from a file
# This is beneficial for testing purposes

import sys
# make sure to comment out this line before submitting to kattis
sys.stdin = open('test.txt','r')

# use this to read in a single integer
n=int(sys.stdin.readline())

# use this to read in 2 or more integers from the same line
m,n=map(int,sys.stdin.readline().split())

# use this to read in a line of integers and store them in a list
bats=[int(x) for x in sys.stdin.readline().split()]

# use this to read in integers line by line and store them in a list
lst=[]
for _ in range(n):
    lst.append(int(sys.stdin.readline()))

# use this if there is no known end to the input
for line in sys.stdin:
    # do something with line
    n=int(line.strip())
