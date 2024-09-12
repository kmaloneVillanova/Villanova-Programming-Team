# Start all files with a link to the problem you're solving
# https://open.kattis.com/problems/addtwonumbers

#import sys so you can read the input from a file
import sys
# read in test case
# remember to comment this out before submitting to kattis
sys.stdin = open('add_nums.txt','r')
# reads in both numbers and converts them to integers
x, y = map(int, sys.stdin.readline().split())
# the line above is equivalent to:
# x, y = sys.stdin.readline().split()
# x = int(x)
# y = int(y)
print(x + y)