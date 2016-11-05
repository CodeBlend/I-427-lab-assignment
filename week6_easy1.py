#Equal_Stacks
#https://www.hackerrank.com/challenges/equal-stacks


#!/bin/python

n1, n2, n3 = raw_input().strip().split(' ')
n1, n2, n3 = [int(n1), int(n2), int(n3)]
n1_height = map(int, raw_input().strip().split(' '))
n2_height = map(int, raw_input().strip().split(' '))
n3_height = map(int, raw_input().strip().split(' '))
# print n1_height
# print n1_height.pop()

n1_height.reverse()
n2_height.reverse()
n3_height.reverse()
# print n1_height, n2_height, n3_height

stack_all = [n1_height, n2_height, n3_height]
# print stack_all

s1, s2, s3 = sum(n1_height), sum(n2_height), sum(n3_height)
# print s1, s2, s3

list_sum = [s1, s2, s3]

while (list_sum[0] != list_sum[1]) or (list_sum[0] != list_sum[2]) :
    t = stack_all[list_sum.index(max(list_sum))].pop()
    list_sum[list_sum.index(max(list_sum))] -= t

print list_sum[0]
