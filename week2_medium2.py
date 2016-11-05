#Sparse Arrays
#https://www.hackerrank.com/challenges/sparse-arrays

N = int(raw_input())

arr1 = []
for i in range(0, N):
    value = raw_input()
    arr1.append(value)

#['aba', 'baba', 'aba', 'xzxb']
#print array

Q = int(raw_input())

arr2 = []
for i in range(0, Q):
    s1 = raw_input()
    arr2.append(s1)
    
#['aba', 'xzxb', 'ab']
#print arr2

for i in range(0, len(arr2)):
    counter = 0
    for j in range(0, len(arr1)):
        if arr2[i] == arr1[j]:
            counter += 1
    print counter
            
    

