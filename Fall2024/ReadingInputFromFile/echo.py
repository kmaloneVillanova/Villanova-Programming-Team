# https://open.kattis.com/problems/echoechoecho

import sys
# read in test case
sys.stdin = open('echo.txt','r')
word = sys.stdin.readline().strip()
print(word,word,word)