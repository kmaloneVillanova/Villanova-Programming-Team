# https://open.kattis.com/problems/fourdierolls
# passed all tests
# Patrick showed me the math to solve this
# First calculate the number of different rolls possible for each n call this X.
# Figure out how many ways for Ashely to win (She wins if all different. Use factorial for this). Then 
# subract that from X and that is the number of different ways for Brandon to win.

# if n = 3 If they are all different then Ashley has 3 ways to win and so does Brandon.
# If one is already matching then Ashley has 0 ways to win and Brandon 6.
 
# if n = 2 there are 36 (6 * 6) ways to roll the die. 
# 4 * 3 (12) ways for Ashley to win. And 36 - 12 ways for Brandon.

# if n = 1 there are 216 (6 * 6 * 6) ways to roll the dice
# 60 (5 * 4 * 3) ways for Ashley to win and 156 (216 - 60) for Brandon.


import sys
# read in test case
#sys.stdin = open('fourdierolls.txt','r')

n = int(sys.stdin.readline())
#rolls = map(int, sys.stdin.readline().split())
rolls = sys.stdin.readline().split()
rolls = [int(x) for x in rolls]
#print(rolls)

if n == 1:
# Roll 3 more times. Possibilities are 6*6*6=216
# Ashley can win if 3 different so 5*4*3=60
# Brandon can win total-Ashley wins = 216-60 = 156
    print(60, 156)
if n == 2:
    if rolls[0] == rolls[1]:
        print(0, 36)
    else:
        print(12, 24)
if n == 3:
    if rolls[0] != rolls[1] and rolls[0] != rolls[2] and rolls[1] != rolls[2]:
        print(3, 3)
    else:
        print(0, 6)
# Note: had an error in the logic above. I wrote a bunch of if elif
# statements trying to account for the possible inputs all of which
# had an output of (0,6). I kept failing test cases. I passed all
# after I simplified to one if else statement.
# Lesson: Keep it simple.