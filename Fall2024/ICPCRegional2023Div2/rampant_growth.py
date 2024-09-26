# https://open.kattis.com/problems/rampantgrowth
# You have the number of rows as options for placement for the first column
# For every additional columns you have row-1 options for placement
# Problem says plants in adjacent columns cant' be next to each other

import sys

#sys.stdin = open('test.txt','r')
row,col = map(int, sys.stdin.readline().split())

# start with options for first column
num_plants_options=row
md = 998244353

# for the additional columns 
for i in range(col-1):
    num_plants_options*=(row-1)    

# use mod operator for final result
r = num_plants_options%md
print(r)
