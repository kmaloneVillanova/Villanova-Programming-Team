# https://open.kattis.com/problems/orderedproblemset

import sys
# read in test case
sys.stdin = open('ordered_set.txt','r')

n = int(sys.stdin.readline())
problems = []

for i in range(n):
    problems.append(int(sys.stdin.readline()))

k=[]
for i in range(2,n+1):
    if n % i == 0:
        #start index of section k
        s=0
        #end index of section k
        e=n//i
        flag=True
        while e < n - ((n//i) - 1):
            #compare max of section i with min of section j
            if max(problems[s:e]) > min(problems[e:e+n//i]):
                flag=False
                break
            else:
                s = e
                e = s + n//i
        if flag:
            k.append(i)    
      
if len(k) < 1:
    print(-1)
else:
    for num in k:
        print(num)


