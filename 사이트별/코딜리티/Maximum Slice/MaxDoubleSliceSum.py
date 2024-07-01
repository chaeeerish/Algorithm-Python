def solution(A):
    left_sum = [0] * len(A)
    right_sum = [0] * len(A)

    for i in range(1, len(A)):
        left_sum[i] = max(0, left_sum[i-1] + A[i])

    for i in range(len(A) - 2, -1, -1):
        right_sum[i] = max(0, right_sum[i + 1] + A[i])

    result = 0
    for i in range(1, len(A) - 1):
        result = max(result, left_sum[i - 1] + right_sum[i + 1])
    return result

print(solution([3, 2, 6, -1, 4, 5, -1, 2]))
print(solution([1, 2, 3]))