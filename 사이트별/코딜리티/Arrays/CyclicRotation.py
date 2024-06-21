'''
배열의 회전
Array A를 K번 회전
'''

def solution(A, K):
    new_A = [0] * len(A)

    while len(A) != 0 and K >= len(A):
        K %= len(A)

    for i in range(len(A)):
        if i + K >= len(A):
            new_A[((i + K) - len(A))] = A[i]
        else:
            new_A[(i + K)] = A[i]
    return new_A

print(solution([3, 8, 9, 7, 6], 3))
print(solution([0, 0, 0], 1))
print(solution([1, 2, 3, 4], 4))
print(solution([], 0))
print(solution([1, 2, 3, 4], 80))