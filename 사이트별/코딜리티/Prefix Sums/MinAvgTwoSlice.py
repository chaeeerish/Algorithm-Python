import math
import random


# def solution(A):
#     result = math.inf
#     starting_position = -1
#     for i in range(len(A)):
#         for j in range(i + 1, len(A)):
#             temp = sum(A[i: j + 1]) / (j - i + 1)
#             if temp < result:
#                 result = temp
#                 starting_position = i
#     return starting_position


# def solution(A):
#     result = math.inf
#     starting_position = -1
#
#     i = 0
#     j = 1
#     current_sum = A[i]
#     while i <= len(A) - 2:
#         current_sum += A[j]
#         if current_sum / (j - i + 1) < result:
#             result = current_sum / (j - i + 1)
#             starting_position = i
#
#         j += 1
#         if j == len(A):
#             i += 1
#             j = i + 1
#             current_sum = A[i]
#
#     return starting_position


def solution(A):
    minAvg = (A[0] + A[1]) / 2
    startingPoint = 0

    for i in range(2, len(A)):
        avg = (A[i] + A[i - 1] + A[i - 2]) / 3
        if minAvg > avg:
            minAvg = avg
            startingPoint = i - 2

        avg = (A[i] + A[i - 1]) / 2
        if minAvg > avg:
            minAvg = avg
            startingPoint = i - 1

    return startingPoint


print(solution([4, 2, 2, 5, 1, 5, 8]))
# print(solution([random.randint(-10000, 10000) for _ in range(random.randint(2, 10))]))