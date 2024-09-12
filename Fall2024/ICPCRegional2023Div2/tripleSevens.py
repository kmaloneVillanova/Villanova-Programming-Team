# https://open.kattis.com/problems/triplesevens

import sys
# read in test case
#sys.stdin = open('tripleSevens.txt','r')

# read in number of numbers on wheel
n = int(sys.stdin.readline())
output = 777
# read in numbers
for line in sys.stdin:
    line=line.strip()
    line=line.split()
    nums=[int(i) for i in line]#
    hasSeven=False
    for i in nums:
        if i == 7:
            hasSeven=True
            break
    if hasSeven == False:
        output = 0
        break
print(output)






