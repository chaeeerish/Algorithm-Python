'''
10, 2, 5, 1, 8, 20
1, 2, 5, 8, 10, 20
1, 2, 3, 4, 5, 6, 7, 8, 9, 10
'''
import itertools


def solution(A):
    A.sort()

    for i in range(len(A) - 2):
        if A[i] + A[i + 1] > A[i + 2]:
            if A[i + 1] + A[i + 2] > A[i]:
                if A[i + 2] + A[i] > A[i + 1]:
                    return 1
    return 0


print(solution([10, 2, 5, 1, 8, 20]))
print(solution([10, 50, 5, 1]))