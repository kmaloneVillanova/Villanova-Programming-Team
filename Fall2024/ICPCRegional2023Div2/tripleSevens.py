# https://open.kattis.com/problems/triplesevens

import sys
# read in test case
sys.stdin = open('tripleSevens.txt','r')

# read in number of numbers on the three wheels
n = int(sys.stdin.readline())
output = 777

# read in numbers on each wheel
# since we know there are three wheels, we could read in the three lines
# or we can use a loop which will read in a line until there is no more input
for line in sys.stdin:
    # read in the numbers and store in nums
    nums = map(int, line.strip().split())
    # must convert nums to a list
    nums = list(nums)
    # check each list for a 7
    hasSeven=False
    for i in nums:
        if i == 7:
            hasSeven=True
            break
    if hasSeven == False:
        output = 0
        break
print(output)






