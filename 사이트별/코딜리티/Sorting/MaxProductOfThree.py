def solution(A):
    A.sort()
    return max(A[0] * A[1] * A[-1], A[-1] * A[-2] * A[-3])

print(solution([-3, 1, 2, -2, 5, 6]))
print(solution([1, 2, 3]))
print(solution([0, 1, 2, 3, 4]))
print(solution([0, -1, -2, -3, -4]))