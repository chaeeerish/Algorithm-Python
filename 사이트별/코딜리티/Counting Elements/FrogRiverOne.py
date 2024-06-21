import math


def solution(X, A):
    result = set([n for n in range(1, X + 1)])

    left = 0
    right = len(A)
    time = math.inf
    while left < right:
        mid = (left + right) // 2
        if set(A[:mid + 1]) == result:
            right = mid
            time = min(time, mid)
        else:
            left = mid + 1

    if time == math.inf:
        return -1
    return time


print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))