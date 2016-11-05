# Poisonous Plants
# https://www.hackerrank.com/challenges/poisonous-plants

N = int(raw_input())
k = []
for i in raw_input().split():
    k.append(int(i))


def find_index(A, count):
    get_rid_of = []
    for i in range(0, len(A)-1):
        if A[i] < A[i+1]:
            get_rid_of.append(i+1)

    if len(get_rid_of) == 0:
        return count

    for j in range(len(get_rid_of)-1, -1, -1):
        A.pop(get_rid_of[j])

    count += 1
    return find_index(A, count)

print find_index(k, 0)

