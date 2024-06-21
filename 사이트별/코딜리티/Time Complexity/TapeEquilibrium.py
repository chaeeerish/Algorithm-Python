import math
import random


def solution(A):
    sum_value = sum(A)
    min_value = math.inf
    before_sum = 0
    for p in range(0, len(A) - 1):
        before_sum += A[p]
        min_value = min(abs(before_sum - (sum_value - before_sum)), min_value)
    return min_value


print(solution([3, 1, 2, 4, 3]))
print(solution([1, 2, 3]))
print(solution([-4, -1, -2]))

# array = [random.randint(-1000, 1000) for _ in range(100000)]
# print(array)
# print(solution(array))