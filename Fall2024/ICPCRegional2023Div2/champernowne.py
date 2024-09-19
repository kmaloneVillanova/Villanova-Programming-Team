# https://open.kattis.com/problems/champernowneverification
# n < 10^9 which means the largest test case is 
# 123456789
# We don't have to worry about 12345678910 which would make this
# problem harder

import sys
# read in test case
sys.stdin = open('champer.txt','r')

# read in number
n = int(sys.stdin.readline())
digits = []
while n >= 10:
    # first get the remainder % 10, which gives us the last digit of the number. 19 % 10 = 9
    r = n % 10
    digits.append(r)
    # now divide by 10 10 // 19 = 1, which breaks down the number
    n = n // 10

digits.append(n%10)
digits.reverse()
output = len(digits)
for i in range(1,len(digits)):
    if digits[i] - digits[i-1] != 1:
        output = -1
        break
if digits[0] != 1:
    output = -1
#print(digits)
print(output)