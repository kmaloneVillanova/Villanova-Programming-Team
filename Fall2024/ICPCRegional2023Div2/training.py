# https://open.kattis.com/problems/training
# this one needs to be read carefully
# make sure to update the skill level after solving a problem
# as the skill level increases, more problems can be solved

import sys
# read in test file
sys.stdin = open('training.txt','r')

# read in n = number of problems, s = skill level
n, s = map(int, sys.stdin.readline().split())

# read in n upper and lower bounds
for i in range(n):
    l, u = map(int, sys.stdin.readline().split())
    if s >=l and s<=u:
        s += 1

print(s)






