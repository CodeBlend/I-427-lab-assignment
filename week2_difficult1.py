#Maximize It!
#https://www.hackerrank.com/challenges/maximize-it

import itertools
k, m = map(int, raw_input().split())
data = [map(int, raw_input().split())[1:] for i in range(k)]
# print k, m
# print data

temp1 = []
for i in itertools.product(*data):
    temp1.append(i)


n = 0
temp2 = []
for i in range(0, len(temp1)):
    for j in range(0, k):
        n = n + temp1[i][j] ** 2
    temp2.append(n % m)
    n = 0
    
print max(temp2)
