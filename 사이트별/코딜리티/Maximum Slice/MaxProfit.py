import math


def solution(A):
    if len(A) == 0:
        return 0

    result = -math.inf
    min_value = A[0]
    for i in range(1, len(A)):
        min_value = min(min_value, A[i])
        result = max(result, A[i] - min_value)

    if result > 0:
        return result
    return 0

print(solution([23171, 21011, 21123, 21366, 21013, 21367]))
print(solution([]))
print(solution([29, 22, 22, 23, 30]))
print(solution([8, 9, 3, 6, 1, 2]))