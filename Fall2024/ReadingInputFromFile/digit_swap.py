# https://open.kattis.com/problems/digitswap

import sys
# read in test case
sys.stdin = open('digit_swap.txt','r')
num = sys.stdin.readline().strip()
# the input is read as a string, so can index into it and swap character digits
print(f"{num[1]}{num[0]}")